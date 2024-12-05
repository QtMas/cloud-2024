sudo apt update
sudo apt upgrade -y
sudo apt install curl
sudo apt install vim
sudo snap install microk8s --classic
sudo snap alias microk8s.kubectl kubectl
sudo snap alias microk8s.helm helm
sudo usermod -a -G microk8s $USER
mkdir -p ~/.kube
chmod 0700 ~/.kube
newgrp microk8s
