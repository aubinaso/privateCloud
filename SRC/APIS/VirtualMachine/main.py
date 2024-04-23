import sys
sys.path.append("../../config.py")
from config import *

virtualmachine_blueprint = Blueprint('virtualmachine_blueprint', __name__)

@virtualmachine_blueprint.route('/v1/virtualmachine', methods=['GET'])
def list_virtualmachine():
    path = os.path.join(parent_dir, "virtualMachine/")
    virtualMachine = []
    for vm in os.listdir(path):
        with open(os.path.join(path, vm + "/data.json"), 'r') as f:
            data = json.load(f)
            virtualMachine.append(data["name"])
    return json.dumps(virtualMachine)

@virtualmachine_blueprint.route('/v1/virtualmachine/<string:name>', methods=['GET'])
def get_virtualmachine(name: str):
    path = os.path.join(parent_dir, "virtualMachine/" + name + "/")
    virtualMachine = None
    with open(os.path.join(path, "data.json"), 'r') as f:
        virtualMachine = json.load(f)
    return json.dumps(virtualMachine)

@virtualmachine_blueprint.route('/v1/virtualmachine', methods=['POST'])
def add_virtualmachine():
    json_data = request.get_json()
    path = os.path.join(parent_dir, "virtualMachine/" + json_data["name"])
    if os.path.exists(path):
        return json.dumps({"message": "name of the resource already taken"})
    os.makedirs(path)
    virtualMachine = (
        {
            "id": "vm-" + uuid.uuid4().hex,
            "name": json_data["name"],
            "tag": json_data["tag"],
            "hostname": json_data["hostname"],
            "provider": json_data["provider"],
            "cpus": json_data["cpus"],
            "memory": json_data["memory"],
            "box": json_data["box"],
            "box_url": json_data["box_url"],
            "box_version": json_data["box_version"],
            "private_network": json_data["private_network"]
        }
    )
    with open(os.path.join(path, "data.json"), 'w') as f:
        json.dump(virtualMachine, f)
    return json.dumps({"message": "Creation successful"})