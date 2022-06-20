
from flask import Flask, request
import subprocess

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/vm")

def hello():
    resourcegroup =request.args.get('resourcegroup')  
    vmname=request.args.get('vmname') 
    # cmd = (["az", "vm", "list", "--resource-group", str(resourcegroup) , "--show-details" ])
    cmd = (["az", "vm",  "show", "--name", str(vmname), "--resource-group", str(resourcegroup), "--show-details" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out

@app.route("/deployment")

def index():
    resourcegroup =request.args.get('resourcegroup')   
    cmd = (["az", "deployment", "operation", "group", "list", "--resource-group", str(resourcegroup), "--name", "vmnetworkinterface_template" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out    
  
if __name__ == "__main__" :


 app.run(port=3004, host='0.0.0.0', debug=True)