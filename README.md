# ubuntu_sshd

How to Use

1. Install docker, python, C compiler(VS, GCC or etc)
2. Clone this repository
```Shell
$ git clone https://github.com/xmilex-git/ubuntu_sshd.git
```
4. Run Setting.py to make setting
```Shell
$ cd ubuntu_sshd
$ python3 Setting.py
Make sure your machine can run 'docker' command.
Make sure your machine can compile C
Make sure ubuntu image present. (run 'docker pull ubuntu:latest')
input your username : username <- enter your username
input your password : password <- enter your password
input your external port : 8334 <- enter your host port to forward
Do you want to set port forwarding by UPnP? (y/n) : n
Skip UPnP Setting...
run 'docker build -t ubuntu_ssh . ; docker run -d -p 8334:22 --name ubuntu_ssh_container ubuntu_ssh'
and try 'ssh username@localhost -p8334'
```
5. Build Docker Image and run
```Shell
$ docker build -t ubuntu_ssh .
$ docker run -d -p {port}:22 --name ubuntu_ssh_container ubuntu_ssh
```
6. Connect via SSH to container
```Shell
$ ssh {user}@localhost -p{port}
```
