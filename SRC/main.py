from config import *
from APIS.VirtualMachine.main import *

app = connexion.App(__name__, specification_dir='./swagger')

swagger_file = os.path.join("./swagger")
for element in os.listdir(swagger_file):
    app.add_api(element)
#app.add_api('swagger.yml')

for directory_name in resourcesObjects.keys():
    path = os.path.join(parent_dir, directory_name)
    if not os.path.exists(path):
        os.makedirs(path)

## Create home file
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)