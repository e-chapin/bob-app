import os

from flask import Flask
from slack import WebClient
from pypco import PCO
# from slackeventsapi import SlackEventAdapter

app = Flask(__name__)

slack_client = WebClient(token=os.environ['SLACK_API_TOKEN'])
# slack_events_adapter = SlackEventAdapter(os.environ["SLACK_SIGNING_SECRET"], "/slack/events", app)

pco_client = PCO(os.environ['PCO_ID'], os.environ['PCO_SECRET'])

from . import views


@app.route('/')
def hello_world():
    return 'Hello World!'
