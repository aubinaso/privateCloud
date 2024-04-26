from config import *

HOST = "0.0.0.0"
PORT = "8300"
DEBUG = True

service_path= "services"
for element in os.listdir(service_path):
    sys.path.append("" + service_path + "." + element)
    from Config.etcd import *

app = Flask(__name__)

path = os.path.realpath(__file__)
PATH = os.path.dirname(path)

os.system("python3 " + path + "/../test2.py")

@app.route('/<string:service>/<string:name>', methods=['GET'])
def get(service: str, name: str):
    json_data = os.system("python3 " + path + "/" + service + "/" + "process.py " + name)
    return json_data

@app.route('/<string:service>/<string:name>', methods=['POST'])
def post(service: str, name: str):
    data = request.get_json()
    json_data = os.system("python3 " + path + "/" + service + "/" + "process.py " + name + " " + data)
    return json_data

@app.route('/<string:service>/<string:name>', methods=['PUT'])
def put(service: str, name: str):
    data = request.get_json()
    json_data = os.system("python3 " + path + "/" + service + "/" + "process.py " + name)
    return json_data

@app.route('/<string:service>/<string:name>', methods=['DELETE'])
def delete(service: str, name: str):
    json_data = os.system("python3 " + path + "/" + service + "/" + "process.py " + name)
    return json_data

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)