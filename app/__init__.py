import os

from flask import Flask
from slack import WebClient

app = Flask(__name__)

slack_client = WebClient(token=os.environ['SLACK_API_TOKEN'])

from . import views


@app.route('/')
def hello_world():
    return 'Hello World!'
