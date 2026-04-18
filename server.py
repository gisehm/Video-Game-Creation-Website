# import flask
from flask import Flask, render_template, request, jsonify

# create an app instance
app = Flask(__name__)

# this is a base route
@app.route('/')

# this is the home method
def hello_world():
  return render_template('homepage.html')