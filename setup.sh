#!/bin/bash

sudo apt-get update && sudo apt-get upgrade

sudo apt-get install -y screen
sudo apt-get install -y python3
sudo apt-get install -y python3-pip

pip3 install psutil


chmod 777 start.sh
./start.sh

rm -r /root/stresser/setup.sh