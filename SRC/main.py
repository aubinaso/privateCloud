from flask import Flask, json

api = Flask(__name__)

virtualMachine = [{"id": 1, "name": "Company one"}, {"id": 2, "name": "Company two"}]

@api.route('/api/v1/virtualmachine', methods=['GET'])
def get_virtualmachine():
    return json.dumps(virtualMachine)

if __name__ == "__main__":
    api.run()