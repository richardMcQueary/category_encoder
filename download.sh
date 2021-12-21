#!/bin/bash


rm -rf ./category_encoder
git clone https://github.com/richardMcQueary/category_encoder.git

cd ./category_encoder

python3 -m pip uninstall -y category_encoder
python3 -m pip install --user .

cd ..
