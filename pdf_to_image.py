import os
from pdf2image import convert_from_path
from multiprocessing import Pool
from tqdm import tqdm

#pdf_path = '/disk/hdd2/preproc_docs/reports_pdf'
pdf_path = '/data/s3/kb.ai.text/financial_report/2021_02_10'
fs = os.listdir(pdf_path)
img_path = '/disk/nvme2/report_images'


def convert_pdf_to_images(f):
    try:
        f_name = f.split('.pdf')[0].strip()
        images = convert_from_path(os.path.join(pdf_path, f))
        os.makedirs(f'{img_path}/{f_name}', exist_ok=True)
        for i, image in enumerate(images):
            image_path = f'{img_path}/{f_name}/{f_name}_{i}.jpg'
            image.save(image_path)
    except:
        print(f_name)
        pass


with Pool(16) as p:
    for _ in tqdm(p.imap(convert_pdf_to_images, fs), total=len(fs), desc='converting...'):
        _
