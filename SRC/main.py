from config import *
from APIS.VirtualMachine.main import virtualmachine_blueprint

resourcesObjects = {
    "virtualMachine": None,
    "virtualNetwork": None,
}

app = Flask(__name__)

parent_dir = "./etcd/"
for directory_name in resourcesObjects.keys():
    path = os.path.join(parent_dir, directory_name)
    if not os.path.exists(path):
        os.makedirs(path)

app.register_blueprint(virtualmachine_blueprint)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)