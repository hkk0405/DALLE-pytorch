#ARG IMG_TAG=1.8.1-cuda10.2-cudnn7-devel
#ARG IMG_REPO=pytorch

#FROM pytorch/$IMG_REPO:$IMG_TAG

FROM nvcr.io/nvidia/pytorch:22.05-py3

#RUN apt-get -y update && apt-get -y install git gcc llvm-9-dev cmake libaio-dev vim wget
RUN apt-get -y install llvm-9-dev libaio-dev openssh-server poppler-utils

RUN git clone https://github.com/microsoft/DeepSpeed.git /tmp/DeepSpeed
#RUN cd /tmp/DeepSpeed && DS_BUILD_OPS=1 ./install.sh -r
RUN cd /tmp/DeepSpeed && pip install .
RUN pip install git+https://github.com/lucidrains/DALLE-pytorch.git

WORKDIR dalle

# docker run cmd
# docker run -dit --name dvae2 \
#     -p 9222:22 -p 9888:8888 -p 9606:6006 \
#     -v /home/hkk/DALLE-pytorch:/dalle -v /disk:/disk -v /data:/data \
#     -w /dalle \
#     --gpus all \
#     --shm-size=32G \
#     nvcr.io/nvidia/pytorch:22.05-py3