import sys
sys.path.append("../config.py")
from config import *

# service : virtualMachine, virtualNetwork, virtualStorage
# name : name of an object
# data : json data of an object

def list_service(service):
    path = os.path.join(parent_dir, service + "/")
    elements = []
    for element in os.listdir(path):
        elements.append(element)
    return json.dumps(elements)

def get_service(service, name: str):
    path = os.path.join(parent_dir, service + "/" + name + "/")
    element = None
    with open(os.path.join(path, "data.json"), 'r') as f:
        element = json.load(f)
    return json.dumps(element)

def add_service(service, name: str, data):
    path = os.path.join(parent_dir, service + "/" + name + "/")
    if os.path.exists(path):
        abort(
            406,
            f"Name {name} of {service} already in use",
        )
        return json.dumps({"message": "name of the resource already taken"})
    os.makedirs(path)
    with open(os.path.join(path, "data.json"), 'w') as f:
        json.dump(data, f)
    return json.dumps({"message": "Creation successful"})

def delete_service(service, name: str):
    path = os.path.join(parent_dir, service + "/" + name + "/")
    if os.path.exists(path):
        shutil.rmtree(path)
        return json.dumps({"message": "Deletion successful"})