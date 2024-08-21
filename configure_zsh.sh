#!/bin/bash

# Update package list and install Zsh, Git, and Font Awesome
sudo apt update
sudo apt install -y zsh git fonts-font-awesome

# Start Zsh and create an empty .zshrc file
zsh -c "echo '' > ~/.zshrc"

# Install Oh My Zsh
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)" --unattended

# Clone Zsh plugins for auto-suggestions and syntax highlighting
ZSH_CUSTOM=${ZSH_CUSTOM:-~/.oh-my-zsh/custom}
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting

# Enable plugins in .zshrc
sed -i 's/^plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/' ~/.zshrc

# Restart Zsh to apply changes
exec zsh
