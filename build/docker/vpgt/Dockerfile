FROM --platform=linux/amd64 nvidia/cuda:12.0.0-base-ubuntu18.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip python3-opencv git wget unzip

RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

RUN pip install --upgrade pip

RUN pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install numpy scipy opencv-python matplotlib pyzmq==24.0.1

WORKDIR /usr/src