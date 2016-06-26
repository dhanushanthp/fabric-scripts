from fabric.api import sudo,env

env.hosts = ['192.168.0.119']
env.user = "ubuntu"
env.password = "ubuntu"

def deploy():
    install_java();

def system_update():
    sudo("apt-get update");

def install_java():
    system_update();
    sudo("apt-get install python-software-properties");
    sudo("add-apt-repository ppa:webupd8team/java");
    system_update();
    sudo("apt-get install -y oracle-java8-installer");