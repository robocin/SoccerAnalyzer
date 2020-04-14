#!/bin/sh

wget http://repo.continuum.io/miniconda/Miniconda3-3.7.0-Linux-x86_64.sh -O ~/miniconda.sh

cd ~

chmod 777 miniconda.sh 

./miniconda.sh -b

rm miniconda.sh

conda --version

yes | conda update conda

yes | conda create --name ambiente_analyzer pandas

source activate ambiente_analyzer
#Deu "./install.sh: 25: source: not found", como resolver?

yes | sudo apt install python3-pip

pip3 install --upgrade pip setuptools

pip3 install PyQt5
