
from flask import Flask, request
import subprocess

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/publicip")

def hello():
    resourcegroup =request.args.get('resourcegroup') 
    publicipname =request.args.get('publicipname')  
    # cmd = (["az", "network", "public-ip", "list", "--resource-group", str(resourcegroup) ])
    cmd = (["az", "network", "public-ip", "show", "--name", str(publicipname), "--resource-group", str(resourcegroup) ]) 
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out

@app.route("/deployment")

def index():
    resourcegroup =request.args.get('resourcegroup')   
    cmd = (["az", "deployment", "operation", "group", "list", "--resource-group", str(resourcegroup), "--name", "publicip_template" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out    
  
if __name__ == "__main__" :


 app.run(port=3002, host='0.0.0.0', debug=True)