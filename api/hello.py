from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


def computeAvg(a,b,c,d,e):
    return ((a+b+c+d+e)/5)

@app.route('/npv', methods = ['POST','GET'])
def npvMult():
    r = request.get_json()
    x19 = r["a"]
    x18 = r["b"]
    x17 = r["c"]
    x16 = r["d"]
    x15 = r["e"]
    avg = computeAvg(x19, x18, x17, x16, x15)
    return jsonify(NPV=str(avg))
