from email.mime import application
from flask import Flask, jsonify, request
import pickle
import numpy as np
application = Flask(__name__)


@application.route("/")
def index():
    return "<p>Hello, World!</p>"


@application.route("/login",methods=['GET'])
def login():
    
    data=request.get_json(force=True)
    model=pickle.load(open('mippl.pkl','rb'))
    
    print([np.array(list(data.values()))])
    reqObj=[np.array(list(data.values()))]

    pred=model.predict(reqObj)

    print(data.values())
    print(pred[0])

    output=pred[0]
    return jsonify(output)

if __name__ == "__main__":
    application.run(debug=True)