# python
import os

# packages
from slack.errors import SlackApiError

# local
from app import app
from app import client
from .blocks import get_setlist_reminder



@app.route('/setlistreminder/create', methods=['GET'])
def hello():

    try:
        response = slack_client.chat_postMessage(
            channel='#testbob',
            text="Reminder: Finalize the setlist",
            blocks=get_setlist_reminder()
        )

        assert response["message"]["text"] == "Reminder: Finalize the setlist"
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")

    return 'Hello Slack!'
