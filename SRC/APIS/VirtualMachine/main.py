import uuid
from dataclasses import dataclass

@api.route('/v1/virtualmachine', methods=['GET'])
def get_virtualmachine(path: str):
    path = os.path.join(path, "virtualMachine/")
    virtualMachine = []
    for vm in os.listdir(path):
        with open(os.path.join(path, vm + "/data.json"), 'r') as f:
            virtualMachine.append(json.load(f))
    return json.dumps(virtualMachine)

@api.route('/v1/virtualmachine/<str:name>', methods=['GET'])
def get_virtualmachine(name: str, path: str):
    path = os.path.join(path, "virtualMachine/" + name + "/")
    virtualMachine = None
    with open(os.path.join(path, "data.json"), 'r') as f:
        virtualMachine = json.load(f)
    return json.dumps(virtualMachine)

@api.route('/v1/virtualmachine', methods=['POST'])
def add_virtualmachine(json_data: dict, path: str):
    path = os.path.join(path, "virtualMachine/" + json_data["name"])
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
            "cpu": json_data["cpu"],
            "memory": json_data["memory"],
            "box": json_data["box"],
            "box_url": json_data["box_url"],
            "box_version": json_data["box_version"],
            "private_network": json_data["private_network"]
        }
    )
    f = open(os.path.join(path, "data.json"), 'w')
    f.write(json.dumps(virtualMachine))
    return json.dumps({"message": "Creation successful"})

@dataclass
class networkConfig():
    name: str
    ip: str
    guest_port: list(int)
    host_port: list(int)

@dataclass
class storageConfig():
    synced_folder: list(str)
    shell: str

@dataclass
class VirtualMachine():
    name: str
    tag: list(str)
    hostname: str
    provider: str
    cpu: int
    memory: int
    box: str
    box_url: str
    box_version: str
    private_network: str