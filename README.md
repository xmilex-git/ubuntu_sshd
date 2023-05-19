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
