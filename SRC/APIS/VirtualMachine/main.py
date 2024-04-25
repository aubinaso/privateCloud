import sys
sys.path.append("../../Config/etcd.py")
from Config.etcd import *

#virtualmachine_blueprint = Blueprint('virtualmachine_blueprint', __name__)

#@virtualmachine_blueprint.route('/v1/virtualmachine', methods=['GET'])
def list_virtualmachine():
    return list_service("virtualMachine")

#@virtualmachine_blueprint.route('/v1/virtualmachine/<string:name>', methods=['GET'])
def get_virtualmachine(name: str):
    return get_service("virtualMachine", name)

#@virtualmachine_blueprint.route('/v1/virtualmachine', methods=['POST'])
def add_virtualmachine():
    json_data = request.get_json()
    return add_service("virtualMachine", json_data["name"], get_virtualmachine_json(json_data))

def delete_virtualmachine(name: str):
    delete_service("virtualMachine", name)

def get_virtualmachine_json(json_data):
    if "name" in json_data:
        name = json_data["name"]
    else:
        abort(
            406,
            f"parameter 'name' not defined",
        )
        return json.dumps({"message": "you must specify the 'name' of the service"})
    if "image" in json_data:
        image = json_data["image"]
    else:
        abort(
            406,
            f"parameter 'image' not defined",
        )
        return json.dumps({"message": "you must specify the 'image' of the service"})
    network = json_data["network"] if "network" in json_data else DEFAULT_NETWORK
    cpus = json_data["cpus"] if "cpus" in json_data else 2
    memory = json_data["memory"] if "memory" in json_data else 2048
    tag = json_data["tag"] if "tag" in json_data else ["default"]
    return (
        {
            "name": name,
            "network": network,
            "image": image,
            "cpus": cpus,
            "memory": memory,
            "tag": tag
        })