from config import *
from APIS.VirtualMachine.main import *

app = connexion.App(__name__, specification_dir='./swagger')

swagger_file = os.path.join("./swagger")
app.add_api('openapi.yml')

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