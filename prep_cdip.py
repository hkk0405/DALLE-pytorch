import os
import glob
import math
import subprocess
import shutil
import tqdm
import PIL
from PIL import Image
from multiprocessing import Pool

# # decompsiton tar file
# cdip_tars = glob.glob('/disk/nvme2/donut-origin/data/cdip-images/images.*.tar')


# def decomp_tar(f):
#     _ = subprocess.run(f'tar -xvf {f} -C /disk/nvme2/cdip-images', shell=True, capture_output=True)


# for idx in tqdm.tqdm(range(math.ceil(len(cdip_tars)))):
#     in_list = cdip_tars[idx:(idx+1)]
#     with Pool() as p:
#         for _ in p.imap(decomp_tar, in_list):
#             _


# # remove bug img
# file_paths = glob.glob('/disk/nvme2/cdip-images/*/*/*/*/*/*.tif')
# len(file_paths)


# def rm_crashed_img(file_path):
#     # Identify and delete corrupted image in each of the file
#     try:
#         _ = Image.open(file_path)
#     except PIL.UnidentifiedImageError as e:
#         print(f"Error in file {file_path}: {e}")
#         os.remove(file_path)
#         print(f"Removed file {file_path}")


# with Pool() as p:
#     for _ in tqdm.tqdm(p.imap(rm_crashed_img, file_paths), total=len(file_paths)):
#         _


# convert tif to png
folder_paths = glob.glob('/disk/nvme2/cdip-images/*/*/*/*')


def get_file_list(folder_path, extension=''):
    return glob.glob(os.path.join(folder_path, extension))


from functools import partial

folder_fn = partial(get_file_list, extension='')
file1_fn = partial(get_file_list, extension='*.png')
file2_fn = partial(get_file_list, extension='*/*.png')

folder_list = []
with Pool() as p:
    for fol_l in tqdm.tqdm(p.imap(folder_fn, folder_paths), total=len(folder_paths)):
        folder_list.extend(fol_l)

file_paths = []
with Pool() as p:
    for fl in tqdm.tqdm(p.imap(file1_fn, folder_paths), total=len(folder_paths)):
        file_paths.extend(fl)
print('num_tif_files: ', len(file_paths))

with Pool() as p:
    for fl in tqdm.tqdm(p.imap(file2_fn, folder_list), total=len(folder_list)):
        file_paths.extend(fl)
print('num_tif_files: ', len(file_paths))


def convert_tif2png(tif_file_path):
    try:
        with Image.open(tif_file_path) as tif:
            tif.save(tif_file_path.split('.tif')[0]+'.png')
            os.remove(tif_file_path)
    except:
        os.remove(tif_file_path)


# for fp in tqdm.tqdm(file_paths):
#     convert_tif2png(fp)

# with Pool() as p:
#     for _ in tqdm.tqdm(p.imap(convert_tif2png, file_paths), total=len(file_paths)):
#         _

def check_and_remove_img(fp):
    try:
        _ = Image.open(fp)
    except:
        _ = fp
        os.remove(fp)
    return _


rm_files = []
with Pool() as p:
    for _ in tqdm.tqdm(p.imap(check_and_remove_img, file_paths), total=len(file_paths)):
        rm_files.append(_)


# remove empty folder
folder_paths = glob.glob('/disk/nvme2/cdip-images/*/*/*/*/*')
len(folder_paths)

rm_folders = []
for pp in tqdm.tqdm(folder_paths):
    if os.path.isdir(pp):
        # if len(glob.glob(pp+'/*.tif')) == 0:
        if len(glob.glob(pp+'/*.png')) == 0:
            try:
                # shutil.rmtree(pp)
                rm_folders.append(pp)
            except:
                pass

n=0
for i in rm_folders:
    if os.path.isdir(i):
        n += 1
        # os.listdir(i)
        shutil.rmtree(i)
    
n