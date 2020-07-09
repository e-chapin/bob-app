import json

# packages
from flask import request, make_response, jsonify
from slack.errors import SlackApiError

# local
from app import app
from app import slack_client
from .setlist import handle_finalize_setlist


@app.route('/slack/interactive-endpoint', methods=['POST'])
def slack_interaction():
    payload = json.loads(request.form["payload"])

    # this seems fragile
    action = payload['actions'][0]
    if action['type'] == 'button':
        if action['value'] == 'finalize_setlist_button':
            handle_finalize_setlist(payload)

    return make_response({}, 200)