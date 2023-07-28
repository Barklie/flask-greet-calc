# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add():
    """Substract a from b."""
    a = request.args['a']
    b = request.args['b']
    res = eval(a) + eval(b)
    # print(res)
    return str(res)

@app.route('/multiply')
def multiple():
    """Multiply a & b."""
    a = request.args['a']
    b = request.args['b']
    res = eval(a) * eval(b)
    # print(res)
    return str(res)

@app.route('/subtract')
def subtract():
    """Subtract b from a."""
    a = request.args['a']
    b = request.args['b']
    res = eval(b) - eval(a)
    # print(res)
    return str(res)

@app.route('/divide')
def divide():
    """Divide a from b."""
    a = request.args['a']
    b = request.args['b']
    res = eval(a) / eval(b)
    # print(res)
    return str(res)