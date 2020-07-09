# python
import os

# packages
from slack.errors import SlackApiError

# local
from app import app
from app import slack_client
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


def handle_finalize_setlist(payload):
    completed = False

    blocks = payload.get('message').get('blocks')
    # this all seems fragile
    button_id = payload['actions'][0]['block_id']
    # find the button block
    for block in blocks:
        block_id = block['block_id']
        if block_id != button_id:
            continue
        text = block['elements'][0]['text']['text']
        if text == 'Complete?':
            completed = True
            block['elements'][0]['text']['text'] = ':white_check_mark: Complete! :white_check_mark:'
        else:
            block['elements'][0]['text']['text'] = 'Complete?'
        break

    if completed:
        slack_client.chat_postMessage(
            channel=payload['channel']['id'],
            thread_ts=payload['message']['ts'],
            as_user=True,
            link_names=True,
            text='<UHY636GSV> The setlist is finalized!'
        )

    slack_client.chat_update(
        channel=payload['channel']['id'],
        ts=payload['message']['ts'],
        blocks=blocks
    )