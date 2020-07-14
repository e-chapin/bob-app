import os
import datetime
from dateutil import relativedelta

from app import pco_client

from app.helpers import pco_helper, get_rehearsal_date_from_block


def get_third_tuesday():
    return datetime.datetime.now() + relativedelta.relativedelta(weekday=relativedelta.TU(3))


def get_setlist_reminder(leader='Jason', payload=None, refresh=False):

    if refresh:
        rehearsal_date_str = get_rehearsal_date_from_block(payload)
        rehearsal_date =  datetime.datetime.strptime(rehearsal_date_str, '%Y-%m-%d')
    else:
        rehearsal_date = get_third_tuesday()
        rehearsal_date_str = rehearsal_date.strftime('%Y-%m-%d')

    type_id = pco_helper.get_online_type()
    plan_id, song_list = pco_helper.get_songs_for_date(type_id, rehearsal_date)

    # this is redudent until we haave more leaders, but do this just use the leader variable
    if leader == 'Jason':
        asignee = os.environ.get('JASON_USER')
    else:
        asignee = os.environ.get('JASON_USER')

    song_text = "*Songs: * \n\n"
    for song in song_list:
        song_text += '- {}\n'.format(song)

    if payload:
        # only refresh song list block
        blocks = payload['message']['blocks']
        for block in blocks:
            if block['block_id'] == 'songs':
                block['text']['text'] = song_text
                return blocks

    block = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<@{}> Confirm setlist for <https://planningcenteronline.com/plans/{}|{}>".format(asignee, plan_id, rehearsal_date_str)
            }
        },
        {
            "type": "actions",
            "block_id": "datepick",
            "elements": [
                {
                    "type": "datepicker",
                    "initial_date": rehearsal_date_str,
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select a date",
                        "emoji": True
                    }
                }
            ]
        },
        {
            "block_id": "user_assign",
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Assigned to:"
            },
            "accessory": {
                "type": "users_select",
                "action_id": "setlist_assigned_user",
                "initial_user": asignee,
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select a user",
                    "emoji": True
                }
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Set list status:"
            },
            "accessory": {
                "type": "static_select",
                "initial_option": {
                    "text": {
                        "type": "plain_text",
                        "text": "unconfirmed",
                        "emoji": True
                    },
                    "value": "value-0"
                },
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select an item",
                    "emoji": True
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "unconfirmed",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "waiting on feedback",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "songs confirmed",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "keys confirmed",
                            "emoji": True
                        },
                        "value": "value-3"
                    }
                ]
            }
        },
        {
            "block_id": "songs",
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": song_text
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Complete?",
                        "emoji": True
                    },
                    "value": "finalize_setlist_button"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": ":arrows_clockwise:",
                        "emoji": True
                    },
                    "value": "refresh_card"
                }
            ]
        }
    ]
    return block
