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
    # if NPV >= 0:
    #     print("Project made the required annual rate of return of " + str(i) + "%")
    #     print("Project go ahead approved")
    # else:
    #     print("Project did not make the required annual rate of return of " + str(i) + "%")
    #     print("Project denied")
    return NPV

@app.route('/npv', methods = ['POST','GET'])
def npvMult():
    r = request.get_json()
    x19 = int(r["x2019"])
    print(x19)
    x18 = int(r["x2018"])
    x17 = int(r["x2017"])
    x16 = int(r["x2016"])
    x15 = int(r["x2015"])
    xDR = float(r["xdr"])
    # avg = computeAvg(x19, x18, x17, x16, x15, xDR)
    netProfitVal = netProfit(x19, x18, x17, x16, x15, xDR)
    return jsonify(npv=netProfitVal,success=True,dRate=xDR)
