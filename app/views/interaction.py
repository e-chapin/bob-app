# packages
from flask import request, make_response
from slack.errors import SlackApiError

# local
from app import app
from app import slack_client


@app.route('/slack/interactive-endpoint', methods=['POST'])
def slack_interaction():
    payload = json.loads(request.form["payload"])

    # Check to see what the user's selection was and update the message
    selection = form_json["actions"][0]["selected_options"][0]["value"]

    if selection == "war":
        message_text = "The only winning move is not to play.\nHow about a nice game of chess?"
    else:
        message_text = "response"

    response = client.api_call(
      "chat.update",
      channel=form_json["channel"]["id"],
      ts=form_json["message_ts"],
      text=message_text,
      attachments=[]
    )

    return make_response("", 200)
