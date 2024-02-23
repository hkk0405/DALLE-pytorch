#!/bin/bash

deepspeed --include localhost:0,1 train_vae.py \
    --image_folder /disk/nvme2/cdip-images \
    --image_size 224 \
    --epochs 12 \
    --batch_size 100 \
    --learning_rate 5e-4 \
    --lr_decay_rate 0.9999 \
    --temp_min 1e-10 \
    --num_images_save 4 \
    --num_layers 3 \
    --num_resnet_blocks 3 \
    --emb_dim 512 \
    --hidden_dim 256 \
    --kl_loss_weight 6.6 \
    --anneal_rate  1. \
    --distributed_backend deepspeed 


# horovodrun -np 3 python train_vae.py \
#     --image_folder /disk/nvme2/report_images \
#     --image_size 224 \
#     --epochs 3 \
#     --batch_size 16 \
#     --learning_rate 5e-4 \
#     --temp_min 1e-10 \
#     --num_images_save 4 \
#     --num_layers 4 \
#     --emb_dim 768 \
#     --hidden_dim 256 \
#     --distributed_backend horovod


#python train_vae.py \
#    --image_folder /disk/nvme2/report_images \
#    --image_size 224 \
#    --epochs 3 \
#    --batch_size 48 \
#    --learning_rate 5e-4 \
#    --temp_min 1e-10 \
#    --num_images_save 4 \
#    --num_layers 4 \
#    --emb_dim 768 \
#    --hidden_dim 256 \
