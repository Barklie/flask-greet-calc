from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Returns Welcome Greeting"""
    html = "<html><body><h1>Welcome</h1></body></html>"
    return html

@app.route('/welcome/home')
def say_welcome_home():
    """Returns Welcome Home Greeting"""
    html = "<html><body><h1>Welcome Home</h1></body></html>"
    return html

@app.route('/welcome/back')
def say_welcome_back():
    """Returns Welcome Back Greeting"""
    html = "<html><body><h1>Welcome Back</h1></body></html>"
    return html