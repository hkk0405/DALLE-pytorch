import os
import glob
import math
import torchvision.transforms.functional as TF

from PIL import Image
from tqdm import tqdm
from multiprocessing import Pool
from functools import partial


def get_file_list(folder_path, extension=''):
    return glob.glob(os.path.join(folder_path, extension))

# (inode)인노드 고갈 문제 - 폴더 하나에 파일이 지나치게 많은 경우 발생(유닉스, 리눅스 시스템에서)
def preprocess_for_resize(img_path):
    main_folder = img_path[0][:5]
    sub_folder = img_path[0][5:7]
    
    img_name = img_path[0]+'.png'
    
    img = Image.open(img_path[1])
    
    s = min(img.size)
    if s >= target_image_size:
        # raise ValueError(f'min dim for image {s} < {target_image_size}')    
        r = target_image_size / s
        s = (round(r * img.size[1]), round(r * img.size[0]))
        img = TF.resize(img, s, interpolation=Image.LANCZOS)
    
    os.makedirs(os.path.join(save_path, main_folder, sub_folder), exist_ok=True)
    img.save(os.path.join(save_path, main_folder, sub_folder, img_name))
    

target_image_size = 256

save_path = f'/disk/nvme1/rs_imgs/pretrain_imgs/'
# os.makedirs(save_path, exist_ok=True)

# exist_file_list = os.listdir(save_path)

# cdip_folder_paths = glob.glob('/disk/nvme2/cdip-images/*/*/*/*')

# folder_fn = partial(get_file_list, extension='')
# file1_fn = partial(get_file_list, extension='*.png')
# file2_fn = partial(get_file_list, extension='*/*.png')

# folder_list = []
# with Pool() as p:
#     for fol_l in tqdm(p.imap(folder_fn, cdip_folder_paths), total=len(cdip_folder_paths)):
#         folder_list.extend(fol_l)

# file_paths = []
# with Pool() as p:
#     for fl in tqdm(p.imap(file1_fn, cdip_folder_paths), total=len(cdip_folder_paths)):
#         file_paths.extend(fl)
# print('num_cdip_imgs: ', len(file_paths))

# with Pool() as p:
#     for fl in tqdm(p.imap(file2_fn, folder_list), total=len(folder_list)):
#         file_paths.extend(fl)
# print('num_cdip_imgs: ', len(file_paths))

# reports_file_paths = glob.glob('/disk/nvme2/report_images/*/*.jpg')
# print('num_reports_imgs: ', len(reports_file_paths))

# total_file_paths = file_paths + reports_file_paths
# print('total_imgs:', len(total_file_paths))

import json
# json.dump(total_file_paths_dict, open('pretrain_data_path.json', 'w'))
total_file_paths_dict = json.load(open('pretrain_data_path.json'))
print(len(total_file_paths_dict))
idf_path = '/disk/hdd2/preproc_docs/reports_pdf'
origin_files = set(list(total_file_paths_dict.keys()))



import glob
# resized_files = os.listdir('/disk/nvme1/rs_imgs/pretrain_imgs')
# resized_files_ = [i.split('.')[0] for i in resized_files]
resized_files = glob.glob('/disk/nvme1/rs_imgs/pretrain_imgs/*/*/*')
resized_files_ = [i.split('/')[-1].split('.')[0] for i in resized_files]
set_resized_files = set(resized_files_)
print(len(set_resized_files))
ccc = origin_files - set_resized_files
print(len(ccc), '=', len(origin_files), '-', len(set_resized_files))
print(len(ccc) == len(total_file_paths_dict)-len(resized_files))

rest_dict = {i: total_file_paths_dict.get(i) for i in ccc}
print(len(rest_dict))


#for i in tqdm(rest_dict.items(), total=len(rest_dict)):
#    preprocess_for_resize(i)


with Pool() as p:
    for _ in tqdm(p.imap(preprocess_for_resize, rest_dict.items()), total=len(rest_dict)):
        _

# 리사이즈 폴더 구조 변경
# resized_file_paths = os.listdir('/disk/nvme1/rs_imgs/pretrain_imgs')

# import shutil

# for i in tqdm(resized_file_paths):
#     try:
#         main_folder = i[:5]
#         sub_folder = i[5:7]
#         os.makedirs(os.path.join(save_path, main_folder, sub_folder), exist_ok=True)
#         org_path = os.path.join(save_path, i)
#         mv_path = os.path.join(save_path, main_folder, sub_folder, i)
#         shutil.move(org_path, mv_path)
#     except:
#         continue
