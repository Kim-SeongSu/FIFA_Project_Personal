# preparation
import sys
import subprocess

def pip_install(package):
    subprocess.check_call(["sudo", sys.executable, "-m", "pip", "install", package])


def pip_install_requirements(requirements_dir):
    subprocess.check_call(["sudo", sys.executable, "-m", "pip", "install", "-r", requirements_dir.rstrip(".txt")+".txt"])

    
    

