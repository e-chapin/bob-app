import json

# packages
from flask import request, make_response, jsonify
from slack.errors import SlackApiError

# local
from app import app
from app import slack_client


@app.route('/slack/interactive-endpoint', methods=['POST'])
def slack_interaction():
    return jsonify({
      "response_type": "ephemeral",
      "replace_original": False,
      "text": "Sorry, that didn't work. Please try again."
    })


@app.route('/slack/get-interactive-endpoint', methods=['GET'])
def get_slack_interaction():
    # payload = json.loads(request.form["payload"])

    payload = {'type': 'block_actions', 'user': {'id': 'UJ49GA8TY', 'username': 'ericjamesjameson', 'name': 'ericjamesjameson', 'team_id': 'TF3748UHH'}, 'api_app_id': 'A0176SWC5ND', 'token': '8lh92420oJ16qPqeV3o4KK16', 'container': {'type': 'message', 'message_ts': '1594324839.027900', 'channel_id': 'C016SRYHJ2X', 'is_ephemeral': False}, 'trigger_id': '1233060777347.513242300595.d46dc6f6dbb532430d03cb1409dea5a8', 'team': {'id': 'TF3748UHH', 'domain': 'ecc-worship'}, 'channel': {'id': 'C016SRYHJ2X', 'name': 'testbob'}, 'message': {'bot_id': 'B016UL398F5', 'type': 'message', 'text': 'Reminder: Finalize the setlist', 'user': 'U0170K9K5PW', 'ts': '1594324839.027900', 'team': 'TF3748UHH', 'blocks': [{'type': 'section', 'block_id': '/=5qM', 'text': {'type': 'mrkdwn', 'text': 'Confirm setlist for two weeks from tomorrow:', 'verbatim': False}}, {'type': 'actions', 'block_id': 'jEm', 'elements': [{'type': 'datepicker', 'action_id': 'ag/m', 'initial_date': '2020-07-19', 'placeholder': {'type': 'plain_text', 'text': 'Select a date', 'emoji': True}}]}, {'type': 'section', 'block_id': 'G6cnu', 'text': {'type': 'mrkdwn', 'text': 'Assigned to:', 'verbatim': False}, 'accessory': {'type': 'users_select', 'initial_user': 'UFB1L07L7', 'placeholder': {'type': 'plain_text', 'text': 'Select a user', 'emoji': True}, 'action_id': '0yMQc'}}, {'type': 'section', 'block_id': 'oj66t', 'text': {'type': 'mrkdwn', 'text': 'Set list status:', 'verbatim': False}, 'accessory': {'type': 'static_select', 'placeholder': {'type': 'plain_text', 'text': 'Select an item', 'emoji': True}, 'initial_option': {'text': {'type': 'plain_text', 'text': 'unconfirmed', 'emoji': True}, 'value': 'value-0'}, 'options': [{'text': {'type': 'plain_text', 'text': 'unconfirmed', 'emoji': True}, 'value': 'value-0'}, {'text': {'type': 'plain_text', 'text': 'waiting on feedback', 'emoji': True}, 'value': 'value-1'}, {'text': {'type': 'plain_text', 'text': 'songs confirmed', 'emoji': True}, 'value': 'value-2'}, {'text': {'type': 'plain_text', 'text': 'keys confirmed', 'emoji': True}, 'value': 'value-3'}], 'action_id': 'l=uu'}}, {'type': 'actions', 'block_id': 'axpI', 'elements': [{'type': 'button', 'action_id': '8nOb', 'text': {'type': 'plain_text', 'text': 'Complete?', 'emoji': True}, 'value': 'click_me_123'}]}]}, 'response_url': 'https://hooks.slack.com/actions/TF3748UHH/1218109697783/jIgFFxgUVXMfWYavYGtZiGUO', 'actions': [{'action_id': '8nOb', 'block_id': 'axpI', 'text': {'type': 'plain_text', 'text': 'Complete?', 'emoji': True}, 'value': 'click_me_123', 'type': 'button', 'action_ts': '1594324850.639958'}]}

    # from pprint import pprint
    # pprint(payload)

    # # Check to see what the user's selection was and update the message
    # selection = payload["actions"][0]["selected_options"][0]["value"]
    #
    # if selection == "war":
    #     message_text = "The only winning move is not to play.\nHow about a nice game of chess?"
    # else:
    #     message_text = "response"
    #
    # response = client.api_call(
    #   "chat.update",
    #   channel=payload["channel"]["id"],
    #   ts=payload["message_ts"],
    #   text=message_text,
    #   attachments=[]
    # )

    # response = slack_client.chat_postMessage(
    #     channel='#testbob',
    #     text="testing   ```{}```".format(payload)
    # )
    return {
      "response_type": "ephemeral",
      "replace_original": false,
      "text": "Sorry, that didn't work. Please try again."
    }
    # return payload
