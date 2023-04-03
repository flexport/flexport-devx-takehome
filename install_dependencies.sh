#!/bin/zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.9.12 using Homebrew package manager
brew install python@3.9

pip install --upgrade pip
pip install Flask==2.2.3 pytest==7.2.2 black==23.3.0 pylint==2.17.1 coverage==7.2.2

