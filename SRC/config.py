import os, uuid
#from flask import Flask, json, request, Blueprint, render_template
from flask import render_template, json, request, Blueprint, abort
import connexion
from datetime import datetime

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