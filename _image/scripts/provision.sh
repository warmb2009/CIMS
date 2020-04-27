#!/bin/bash
set -e
  
#python的一些依赖
yum install -y \
    kde-l10n-Chinese\
    glibc-common\
    git\
    wget\
    mysql-devel\
    gcc\
    swig\
    pulseaudio\
    pulseaudio-libs\
    pulseaudio-libs-devel\
    zlib-devel\
    bzip2-devel\
    openssl-devel\
    ncurses-devel\
    sqlite-devel\
    readline-devel\
    tk-devel\
    gdbm-devel\
    db4-devel\
    libpcap-devel\
    xz-devel\
    libffi-devel\
    ncurese-devel\
    automake\
    autoconf\
    libtool\
    make\
    alsa-lib-devel\
    poppler-utils\
  
#python3.7
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
tar -zxvf Python-3.7.4.tgz
cd Python-3.7.4
./configure
make && make install
rm -rf Python-3.7.4*
  
#pip3
wget --no-check-certificate https://github.com/pypa/pip/archive/9.0.1.tar.gz
tar -zvxf 9.0.1.tar.gz
cd pip-9.0.1
python3.7 setup.py install
rm -rf pip-9.0.1*
pip3 install --upgrade setuptools
