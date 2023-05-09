#!/bin/bash

# Get the full path to the directory containing the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Set the destination directory for the binary
DEST_DIR="$HOME/.local/bin"

# Create the destination directory if it doesn't exist
mkdir -p $DEST_DIR

# Copy the binary to the destination directory
cp $DIR/binary_search $DEST_DIR

# Make the binary executable
chmod +x $DEST_DIR/binary_search

# Check if the destination directory is already in the PATH
if [[ ":$PATH:" != *":$DEST_DIR:"* ]]; then
    # Add the directory to the system $PATH
    echo "export PATH=\$PATH:$DEST_DIR" >> ~/.bashrc
    source ~/.bashrc
fi

echo "Setup complete! You can now run the 'binary_search' command from anywhere in the terminal."
