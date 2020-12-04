#! /bin/bash

cd service_1/
pip3 install -r requirements.txt
python3 -m pytest --cov .

cd .. 

cd service_2/
pip3 install -r requirements.txt
python3 -m pytest --cov .

cd .. 

cd service_3/
pip3 install -r requirements.txt
python3 -m pytest --cov .

cd .. 

cd service_4/
pip3 install -r requirements.txt
python3 -m pytest --cov .
