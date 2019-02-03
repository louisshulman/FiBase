from flask import Flask, render_template, request, jsonify
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)


def computeAvg(a,b,c,d,e,f):
    return ((a+b+c+d+e)/5)

@app.route('/npv', methods = ['POST','GET'])
def npvMult():
    print("something")
    r = request.get_json()
    x19 = int(r["x2019"])
    print(x19)
    x18 = int(r["x2018"])
    x17 = int(r["x2017"])
    x16 = int(r["x2016"])
    x15 = int(r["x2015"])
    xDR = int(r["xdr"])
    avg = computeAvg(x19, x18, x17, x16, x15, xDR)
    return jsonify(npv=avg,success=True)
