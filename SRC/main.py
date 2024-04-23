from config import *
from APIS.VirtualMachine.main import *

#app = Flask(__name__)

app = connexion.App(__name__, specification_dir='./swagger')
app.add_api('swagger.yml')

for directory_name in resourcesObjects.keys():
    path = os.path.join(parent_dir, directory_name)
    if not os.path.exists(path):
        os.makedirs(path)

## Registering Blueprints
#app.register_blueprint(virtualmachine_blueprint)

## Create home file
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)