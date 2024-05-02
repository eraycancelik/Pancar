#!/bin/bash

# xcb ve libxcb-cursor0 paketlerini kontrol edin ve eksikse yükleyin
echo "Checking xcb and libxcb-cursor0 packages..."
if ! dpkg -l | grep -qw "libxcb-cursor0"; then
    echo "libxcb-cursor0 package not found. Installing..."
    sudo apt update
    sudo apt install -y libxcb-cursor0
fi

# pipenv ile bağımlılıkları yükleyin
echo "Installing dependencies with pipenv..."
pipenv install

# Qt uygulamanızı çalıştırın
echo "Running Qt application..."
pipenv run python main.py

