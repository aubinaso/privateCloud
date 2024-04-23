import os, uuid
from flask import Flask, json, request, Blueprint
resourcesObjects = {
    "virtualMachine": None,
    "virtualNetwork": None,
}

parent_dir = "./etcd/"