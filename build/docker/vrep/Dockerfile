FROM --platform=linux/amd64 nvidia/cuda:12.1.0-base-ubuntu18.04

# RUN wget https://www.coppeliarobotics.com/files/V-REP_PRO_EDU_V3_6_2_Ubuntu18_04.tar.xz

RUN apt-get update && apt-get install -y \
  wget \
  libglib2.0-0  \
  libgl1-mesa-glx \
  xcb \
  "^libxcb.*" \
  libx11-xcb-dev \
  libglu1-mesa-dev \
  libxrender-dev \
  libxi6 \
  libdbus-1-3 \
  libfontconfig1 \
  xvfb \
  xz-utils \
  liblua5.1-0-dev \
  libqt5gui5 \
  libavcodec-dev \
  libavformat-dev \
  libswscale-dev \
  && rm -rf /var/lib/apt/lists/*

RUN wget https://www.coppeliarobotics.com/files/V-REP_PRO_EDU_V3_6_2_Ubuntu18_04.tar.xz
RUN tar -xJf V-REP_PRO_EDU_V3_6_2_Ubuntu18_04.tar.xz

RUN echo 'export QT_DEBUG_PLUGINS=1' >> ~/.bashrc
RUN echo 'export LD_LIBRARY_PATH=/V-REP_PRO_EDU_V3_6_2_Ubuntu18_04' >> ~/.bashrc

WORKDIR /V-REP_PRO_EDU_V3_6_2_Ubuntu18_04