import sys
sys.path.append("../../Config/etcd.py")
from Config.etcd import *

MAC_ADDRESS_USED = []
NETWORK_IN_USED = []
BRIDGE_ID = []


def list_virtualnetwork():
    return list_service("virtualnetwork")

def get_virtualnetwork(name: str):
    return get_service("virtualnetwork", name)

def add_virtualnetwork():
    json_data = request.get_json()
    return add_service("virtualnetwork", json_data["name"], get_virtualnetwork_json(json_data))

def delete_virtualnetwork(name: str):
    delete_service("virtualMachine", name)

def get_virtualnetwork_json(json_data):
    if "name" in json_data:
        name = json_data["name"]
    else:
        abort(
            406,
            f"parameter 'name' not defined",
        )
        return json.dumps({"message": "you must specify the 'name' of the network"})
    if "network" in json_data:
        network = iprange(json_data["network"])
    else:
        abort(
            406,
            f"parameter 'network' not defined",
        )
        return json.dumps({"message": "you must specify the 'image' of the service"})
    network = json_data["name"] if "network" in json_data else DEFAULT_NETWORK
    mode = json_data["mode"] if "mode" in json_data else "nat"
    mac = generate_mac()
    tag = json_data["tag"] if "tag" in json_data else ["default"]
    return (
        {
            "name": name,
            "bridge_name": random_bridgeID(),
            "mode": mode,
            "mac": mac,
            "iprange": network.with_prefixlen,
            "network": network.network_address,
            "mask": network.netmask,
            "first_address": network[1],
            "last_address": network[-2],
            "tag": tag
        })

def generate_mac():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)])
    if mac in MAC_ADDRESS_USED:
        return generate_mac()
    else:
        MAC_ADDRESS_USED.append(mac)
        return mac
    
def iprange(network):
    try:
        net = ip_network(network, strict=False)
        if net in NETWORK_IN_USED:
            abort(
                406,
                f"Network {network} already in use",
            )
            return json.dumps({"message": "network already in use"})
        return net
    except:
        abort(
            406,
            f"parameter 'network' is not defined as it must be",
        )
        return json.dumps({"message": "you must specify the 'network' in format 'XXX.XXX.XXX.XXX/XX'"})
    
def random_bridgeID():
    name = "virbr" + str(random.randint(0, 1000))
    if name in BRIDGE_ID:
        return random_bridgeID()
    else:
        BRIDGE_ID.append(name)
        return name