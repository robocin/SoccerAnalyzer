#!/bin/sh

cp 2.sh ~/2.sh

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

chmod 777 miniconda.sh 

./miniconda.sh -b

rm miniconda.sh

conda --version

yes | conda update conda

yes | conda create -n analyzer pandas

yes | python3 -m pip install pyautogui

apt-get install python3-tk python3-dev

python3 autogui.py
