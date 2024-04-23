import sys
sys.path.append("../../config.py")
from config import *

#virtualmachine_blueprint = Blueprint('virtualmachine_blueprint', __name__)

#@virtualmachine_blueprint.route('/v1/virtualmachine', methods=['GET'])
def list_virtualmachine():
    path = os.path.join(parent_dir, "virtualMachine/")
    virtualMachine = []
    for vm in os.listdir(path):
        with open(os.path.join(path, vm + "/data.json"), 'r') as f:
            data = json.load(f)
            virtualMachine.append(data["name"])
    return json.dumps(virtualMachine)

#@virtualmachine_blueprint.route('/v1/virtualmachine/<string:name>', methods=['GET'])
def get_virtualmachine(name: str):
    path = os.path.join(parent_dir, "virtualMachine/" + name + "/")
    virtualMachine = None
    with open(os.path.join(path, "data.json"), 'r') as f:
        virtualMachine = json.load(f)
    return json.dumps(virtualMachine)

#@virtualmachine_blueprint.route('/v1/virtualmachine', methods=['POST'])
def add_virtualmachine():
    json_data = request.get_json()
    name = json_data["name"]
    path = os.path.join(parent_dir, "virtualMachine/" + json_data["name"])
    if os.path.exists(path):
        abort(
            406,
            f"Name {name} of Virtual Machine already in use",
        )
        return json.dumps({"message": "name of the resource already taken"})
    provider = json_data["provider"] if "provider" in json_data else "virtualbox"
    tag = json_data["tag"] if "tag" in json_data else []
    hostname = json_data["hostname"] if "hostname" in json_data else json_data["name"]
    cpus = json_data["cpus"] if "cpus" in json_data else 2
    memory = json_data["memory"] if "memory" in json_data else 2048
    private_network = json_data["private_network"] if "private_network" in json_data else ""
    box = json_data["box"] if "box" in json_data else "bento/ubuntu-20.04"
    box_url = json_data["box_url"] if "box" in json_data else ""
    box_version = json_data["box_version"] if "box" in json_data else ""
    virtualMachine = (
        {
            "id": "vm-" + uuid.uuid4().hex,
            "name": json_data["name"],
            "tag": tag,
            "hostname": hostname,
            "provider": provider,
            "cpus": cpus,
            "memory": memory,
            "box": box,
            "box_url": box_url,
            "box_version": box_version,
            "private_network": private_network
        }
    )
    os.makedirs(path)
    with open(os.path.join(path, "data.json"), 'w') as f:
        json.dump(virtualMachine, f)
    return json.dumps({"message": "Creation successful"})