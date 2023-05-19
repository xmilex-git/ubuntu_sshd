
def main():
    print("Make sure your machine can run 'docker' command.")
    print("Make sure your machine can compile C")
    print("Make sure ubuntu image present. (run 'docker pull ubuntu:latest')")
    
    user=input("input your username : ")
    pw=input("input your password : ")
    port=int(input("input your external port : "))

    make_dockerfile(user,pw)

    # docker run -d -p 27027:22 ubuntu_ssh
    # ssh song@localhost -p 27027

    is_upnp=input("Do you want to set port forwarding by UPnP? (y/n) : ")
    if is_upnp=='y':
        print("UPnP Setup...")
        #upnp(port)
    else:
        print("Skip UPnP Setting...")

    print(f"run 'docker build -t ubuntu_ssh . ; docker run -d -p {port}:22 --name ubuntu_ssh_container ubuntu_ssh'")
    print(f"and try 'ssh {user}@localhost -p{port}'")


def upnp(port:int):
    import miniupnpc
    # Create a UPnP object
    upnp = miniupnpc.UPnP()

    # Discover UPnP devices, and select an IGD (Internet Gateway Device)
    upnp.discoverdelay = 200
    upnp.discover()
    upnp.selectigd()

    # Add a new port mapping
    result = upnp.addportmapping(
        external_port=port,  # The external (public) port
        protocol='TCP',      # The protocol (TCP or UDP)
        internal_port=port,  # The internal (private) port
        internal_client=upnp.lanaddr,  # The internal IP address
        description='Docker container SSH port',  # A description
    )

    if result:
        print("Port forwarding was successful")
    else:
        print("Failed to add port mapping")

def make_dockerfile(user,pw):
    txt=f'''FROM ubuntu:latest

RUN sed -i 's/archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list

RUN apt-get update && apt-get install -y openssh-server sudo
RUN mkdir /var/run/sshd

# Create new user
RUN useradd -rm -d /home/{user} -s /bin/bash -g root -G sudo -u 1001 {user}
RUN echo '{user}:{pw}' | chpasswd

# Give the new user sudo rights
RUN echo '{user} ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Update sshd_config
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

'''
    with open("Dockerfile","w") as f:
        f.write(txt)
    

if __name__=='__main__':
    main()