from flask import Flask, render_template, request, jsonify
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)

def computeAvg(a,b,c,d,e,f):
    return ((a+b+c+d+e)/5)

def netProfit(a, b, c, d, e, i):
    lst = [a, b, c, d, e]
    dcilst = []
    for num in range(len(lst)):
        dci = lst[num] / (1 + i)**(num)
        dcilst.append(dci)
    NPV = round((sum(dcilst)), 2)
    print("NPV = " + str(NPV))
    return NPV

def listCal(lst, rate):
    i = rate
    dcilst = []
    for num in range(len(lst)):
        dci = lst[num] / (1 + i)**(num)
        dcilst.append(dci)
    NPV = round((sum(dcilst)), 2)
    print("NPV = " + str(NPV))
    return NPV

@app.route('/npv', methods = ['POST','GET'])
def npvMult():
    r = request.get_json()
    x19 = float(r["x2019"])
    print(x19)
    x18 = float(r["x2018"])
    x17 = float(r["x2017"])
    x16 = float(r["x2016"])
    x15 = float(r["x2015"])
    xDR = float(r["xdr"])
    # avg = computeAvg(x19, x18, x17, x16, x15, xDR)
    netProfitVal = netProfit(x19, x18, x17, x16, x15, xDR)
    return jsonify(npv=netProfitVal,success=True,dRate=xDR)


@app.route('/mnpv', methods = ['POST','GET'])
def npvList():
    r = request.get_json()
    a = r["cFlows"].split(',')
    a = [float(val) for val in a]
    print(a);
    xDR = float(r["xdr"])
    netProfitVal = listCal(a, xDR)
    return jsonify(npv=netProfitVal,success=True,dRate=xDR)
