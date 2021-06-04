#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request, jsonify
#from flask_cors import CORS, cross_origin
import json
import requests
import pandas as pd
import random

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def que():
    res = requests.get("https://powerful-island-81116.herokuapp.com/")
    # Convert data to dict
    data = json.loads(res.text)
 
    # Convert dict to string
    data = json.dumps(data)
 
    print(data)
    print(type(data))
    x=open("que.txt",'a')
    print(data,file=x)
    x.close()
    data = json.dumps(data)
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=False)


# In[ ]:



