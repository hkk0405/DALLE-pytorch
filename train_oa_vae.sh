#!/bin/bash

deepspeed --include localhost:0,3 train_oa_vae.py \
    --image_folder /disk/nvme2/cdip-images \
    --image_size 224 \
    --num_tokens 8192 \
    --emb_dim 128 \
    --hidden_dim 256 \
    --epochs 3 \
    --batch_size 28 \
    --learning_rate 5e-5 \
    --lr_decay_rate 0.999 \
    --temp_min 0. \
    --num_images_save 4 \
    --kl_loss_weight 0. \
    --anneal_rate  1e-8 \
    --distributed_backend deepspeed \
    --smooth_l1_loss \
    --model_path /dalle/dalle-dvae \

# deepspeed --include localhost:0,1 train_oa_vae.py \
#     --image_folder /disk/nvme2/cdip-images \
#     --image_size 224 \
#     --epochs 3 \
#     --batch_size 20 \
#     --learning_rate 5e-4 \
#     --lr_decay_rate 0.999 \
#     --temp_min 1e-10 \
#     --num_images_save 4 \
#     --kl_loss_weight 0. \
#     --anneal_rate  1e-6 \
#     --distributed_backend deepspeed \
#     --model_path /dalle/dalle-dvae \
#     --smooth_l1_loss \
