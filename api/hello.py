from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/npv', methods = ['POST','GET'])
def npvMult():
    r = request.get_json()
    foo = r["a"]+1
    return jsonify(newA=foo)
