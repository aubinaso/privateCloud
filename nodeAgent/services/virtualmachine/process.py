import sys, subprocess
# Importing config.py from nodeAgent directory
sys.path.append("../../config.py")
from config import *
# Rest of the code...

name = sys.argv[1]
path = os.path.realpath(__file__)
path = os.path.dirname(path)

def create(name):
    result = subprocess.run([path + "/create.sh", name ], capture_output=True)
    print(name)

def delete(name):
    print(name)

def update(name):
    print(name)

def get(name):
    print(name)