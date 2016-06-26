from fabric.api import sudo,env,run
from fabric.context_managers import cd
from fabric.contrib.files import exists
from fabric.context_managers import shell_env,prefix

env.hosts = ['192.168.0.119']
env.user = "ubuntu"
env.password = "ubuntu"

scalaTmp = 'scala-tmp';
url = "http://www.scala-lang.org/files/archive/scala-2.10.4.tgz";
fileName = "scala-2.10.4"

def deploy():
#     downloadScala();
    installScala();
#     removeScalTmp();
    
def downloadScala():
    with cd('~'):
        if exists(scalaTmp, use_sudo=True):
            with cd(scalaTmp):
                print(scalaTmp + " Directory exist");
        else:
            run('mkdir ' + scalaTmp)
            with cd(scalaTmp):
                downloadFile(url);
                run("tar -zxvf scala-2.10.4.tgz");
                run("mv scala-2.10.4 scala")

def installScala():
    with cd('/usr/local'):
        if exists('scala', use_sudo=True):
            print("scala  exists");
        else:
            with cd("~/"+ scalaTmp):
                print();
#                 sudo("mv scala /usr/local");
#     run("export SCALA_HOME=/usr/local/scala && export PATH=\"$PATH:$SCALA_HOME/bin\" && /bin/bash source ~/.bashrc",pty=True)
#     run("export PATH=\"$PATH:$SCALA_HOME/bin\"")
#     run("#!/bin/bash && exec bash");
    with cd('~'):
        sudo("./schel.sh")
        

def removeScalTmp():
   with cd('~'):
       if exists(scalaTmp, use_sudo=True):
           sudo("rm -r " + scalaTmp);

# private method
def downloadFile(url):  
    run("wget '{}'".format(url))
            
    