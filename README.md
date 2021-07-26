# swarmpie

## Setup Raspberry Model 4B V1.2 - 4G RAM

- connect to 4G hotspot
- sudo apt update
- sudo apt install code
- sudo apt install git
- git --version
- git config --global user.name ''
- git config --global user.email ''
- git config --global core.autocrlf input
- git config --global core.editor 'code --wait'
- git clone https://github.com/osamahasanone/swarmpie.git
- sudo pip3 install pipenv
- cd repo
- delete files named 'pipfile' and 'pipfile.lock'
- sudo apt-get install libatlas-base-dev
- pipenv install numpy==1.21.1
- pipenv install pyserial==3.5
- pipenv install pytest==6.2.4

## Enable UART interface
1- sudo raspi-config
2- interfacing options
3- p6 serial
4- Would you like a login shell to be accessable over serial?
    NO
5- Would you like the serial port hardware to be enabled?
    YES
6- Reboot
