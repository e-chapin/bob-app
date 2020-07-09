import os
import datetime
from dateutil import relativedelta


def get_setlist_reminder(leader='Jason'):

    second_sunday = datetime.datetime.now() + relativedelta.relativedelta(weekday=relativedelta.SU(2))
    message_date = second_sunday.strftime('%Y-%m-%d')

    # this is redudent until we haave more leaders, but do this just use the leader variable
    if leader == 'Jason':
        asignee = os.environ.get('JASON_USER')
    else:
        asignee = os.environ.get('JASON_USER')

    block = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Confirm setlist for two weeks from tomorrow:"
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "datepicker",
                    "initial_date": message_date,
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select a date",
                        "emoji": True
                    }
                }
            ]
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Assigned to:"
            },
            "accessory": {
                "type": "users_select",
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
                }
            ]
        }
    ]
    return block
