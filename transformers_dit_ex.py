from transformers import BeitImageProcessor, BeitForMaskedImageModeling
import torch
from PIL import Image

image = Image.open('/disk/hdd2/iit_cdip/cdip-images/imagesa/a/a/a/aaa00a00/60008366.tif').convert('RGB')
image = Image.open('900038069_유진20220704시장.pdf_0.png').convert('RGB')

processor = BeitImageProcessor.from_pretrained("microsoft/dit-base")
model = BeitForMaskedImageModeling.from_pretrained("microsoft/dit-base")

model.config

num_patches = (model.config.image_size // model.config.patch_size) ** 2
pixel_values = processor(images=image, return_tensors="pt").pixel_values

import numpy as np

Image.fromarray((pixel_values[0].permute(1,2,0)*255).numpy().astype(np.uint8)).save('test2.png')
# create random boolean mask of shape (batch_size, num_patches)
bool_masked_pos = torch.randint(low=0, high=2, size=(1, num_patches)).bool()

outputs = model(pixel_values, bool_masked_pos=bool_masked_pos)
loss, logits = outputs.loss, outputs.logits

