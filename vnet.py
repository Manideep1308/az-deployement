# import os

# from flask import Flask, request, jsonify


# from flask_cors import CORS
 
 
# app = Flask(__name__)
# CORS(app)
# @app.route('/')
# def func():
#     # # cmd = 'az network vnet list --resource-group demo-arm  '
#     # os.system('az network vnet list --resource-group demo-arm  ')

#     return (os.system('az network vnet list --resource-group demo-arm  '))

#!/usr/bin/env python
from flask import Flask, request
import subprocess

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/vnet")

def hello():
    resourcegroup =request.args.get('resourcegroup')
    vnetname =request.args.get('vnetname')  
    # cmd = (["az", "network", "vnet", "list", "--resource-group", str(resourcegroup) ])
    cmd = (["az", "network", "vnet", "show", "--name", str(vnetname), "--resource-group", str(resourcegroup) ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out

@app.route("/deployment")

def index():
    resourcegroup =request.args.get('resourcegroup')   
    cmd = (["az", "deployment", "operation", "group", "list", "--resource-group", str(resourcegroup), "--name", "vpc_template" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out    
  
if __name__ == "__main__" :


 app.run(port=3000, host='0.0.0.0', debug=True)