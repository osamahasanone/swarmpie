# swarmpie

## Setup Raspberry Model 4B V1.2 - 4G RAM

- connect to 4G hotspot
- sudo apt update
- sudo apt install git
- git --version
- git config --global user.name ''
- git config --global user.email ''
- git config --global core.autocrlf input
- git clone https://github.com/osamahasanone/swarmpie.git
- sudo pip3 install pipenv
- cd repo
- delete files named 'pipfile' and 'pipfile.lock'
- sudo apt-get install libatlas-base-dev
- pipenv install numpy==1.21.1
- pipenv install pyserial==3.5
- pipenv install pytest==6.2.4
