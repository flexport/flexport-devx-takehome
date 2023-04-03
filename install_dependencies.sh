#!/bin/zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.9.12 using Homebrew package manager
brew install python@3.9

# Download the get-pip.py script
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Install pip with sudo
sudo python3 get-pip.py

pip install --upgrade pip

# Install all dependencies on remote server
pip install flask==2.2.3 pytest==7.2.2 black==23.3.0 pylint==2.17.1 coverage==7.2.2

