#!/bin/bash

if command -v black &> /dev/null
then
    echo "Black is installed. Version:"
    black --version
else
    echo "Black is not installed."
fi

