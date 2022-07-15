from email.mime import application
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import pickle
import numpy as np

application = Flask(__name__)
CORS(application, support_credentials=True)

@application.route("/")
def index():
    return "<p>Hello, World!</p>"


@application.route("/login",methods=['GET'])
@cross_origin(supports_credentials=True)
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