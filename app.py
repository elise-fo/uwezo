import requests
from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for, render_template
from flask.json import jsonify
from pprint import pformat
from time import time
import os
import json
from os.path import join
from dotenv import load_dotenv
from requests.structures import CaseInsensitiveDict

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# This allows us to use a plain HTTP callback
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

app.secret_key = os.urandom(24)
app.run(debug=True)


from jinja2 import Environment, FileSystemLoader
e = Environment(loader=FileSystemLoader('templates/'))

base_redirect_uri = 'http://localhost:5000'

@app.route("/")
def website():
    """"""
    return render_template("test.html")
