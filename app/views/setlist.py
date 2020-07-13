# python
import os

# packages
from slack.errors import SlackApiError

# local
from app import app
from app import slack_client
from app import pco_client

from .blocks import get_setlist_reminder, get_third_tuesday


@app.route('/setlistreminder/create', methods=['GET'])
def hello():

    try:
        slack_client.chat_postMessage(
            channel=os.environ.get('SLACK_CHANNEL'),
            text='<@{}>: Finalize the setlist'.format(os.environ.get('JASON_USER')),
            blocks=get_setlist_reminder()
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response['ok'] is False
        assert e.response['error']  # str like 'invalid_auth', 'channel_not_found'
        print('Got an error: {e.response["error"]}')

    return 'Hello Slack!'


def handle_setlist_refresh(payload):
    slack_client.chat_update(

        channel=payload['channel']['id'],
        ts=payload['message']['ts'],
        blocks=get_setlist_reminder(payload=payload)

    )


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
            text='<@{}> The setlist is finalized!'.format(os.environ.get('MIKE_USER'))
        )

    slack_client.chat_update(
        channel=payload['channel']['id'],
        ts=payload['message']['ts'],
        blocks=blocks
    )


def handle_tag_new_user(payload):
    action = payload['actions'][0]

    new_user = action['selected_user']
    old_user = action['initial_user']

    if new_user != old_user:

        # update user block
        for block in payload['message']['blocks']:
            if block['block_id'] == 'user_assign':
                block['accessory']['initial_user'] = new_user
                break

        slack_client.chat_update(

            channel=payload['channel']['id'],
            ts=payload['message']['ts'],
            blocks=payload['message']['blocks']

        )

        slack_client.chat_postMessage(
            channel=payload['channel']['id'],
            thread_ts=payload['message']['ts'],
            as_user=True,
            link_names=True,
            text='<@{}>, this has been assigned to you.'.format(new_user, old_user)
        )
