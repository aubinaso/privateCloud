import json
from dataclasses import dataclass

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
    disk: int
    box: str
    box_url
    network: networkConfig
    storage: storageConfig