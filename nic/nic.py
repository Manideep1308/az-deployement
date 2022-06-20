
from flask import Flask, request
import subprocess

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/nic")

def hello():
    resourcegroup =request.args.get('resourcegroup')
    nicname = request.args.get('nicname')   
    # cmd = (["az", "network", "nic", "list", "--resource-group", str(resourcegroup) ])
    cmd = (["az", "network", "nic", "show","--name", str(nicname), "--resource-group", str(resourcegroup) ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out

@app.route("/deployment")

def index():
    resourcegroup =request.args.get('resourcegroup')   
    cmd = (["az", "deployment", "operation", "group", "list", "--resource-group", str(resourcegroup), "--name", "nic_template" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out    
  
if __name__ == "__main__" :


 app.run(port=3003, host='0.0.0.0', debug=True)