import os, uuid
#from flask import Flask, json, request, Blueprint, render_template
from flask import render_template, json, request, Blueprint, abort
import connexion, random
from ipaddress import ip_network
from datetime import datetime
from jinja2 import Template
import shutil

resourcesObjects = {
    "virtualMachine": None,
    "virtualNetwork": None,
}

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

parent_dir = "./etcd/"

HOST = "localhost"
PORT = "5000"
DEBUG = True
DEFAULT_NETWORK = "aubinnet"