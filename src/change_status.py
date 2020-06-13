import argparse
import json
import os
import urllib.parse
import urllib.request

# define config value
with open(os.path.dirname(os.path.abspath(__file__)) + '/../config.json') as j:
    config = json.load(j)

USER_ID = config['slack']['user_id']
API_TOKEN = config['slack']['api_token']
DEFAULT_STATUS_EMOJI = config['slack']['default_status_emoji']
DEFAULT_STATUS_MESSAGE = config['slack']['default_status_message']
PROFILE_SET_URL = 'https://slack.com/api/users.profile.set'

# CLI option setting
p = argparse.ArgumentParser()
p.add_argument('-e', '--emoji',
               help='Slack emoji code for status icon. (e.g) :ghost:',
               default=DEFAULT_STATUS_EMOJI)
p.add_argument('-m', '--message',
               help='message for status.',
               default=DEFAULT_STATUS_MESSAGE)
args = p.parse_args()


def set_status(emoji, message):
    # type: (str) -> ()
    """Set Slack status."""
    headers = {
        'Authorization': 'Bearer %s' % API_TOKEN,
        'X-Slack-User': USER_ID,
        'Content-Type': 'application/json; charset=utf-8'
    }
    params = {
        'profile': {
            'status_emoji': emoji,
            'status_text': message
        }
    }

    req = urllib.request.Request(
        PROFILE_SET_URL,
        method='POST',
        data=json.dumps(params).encode('utf-8'),
        headers=headers
    )

    with urllib.request.urlopen(req) as res:
        print(json.dumps(json.loads(res.read().decode('utf-8')), indent=2))


if __name__ == '__main__':
    status_emoji = args.emoji
    status_message = args.message

    set_status(status_emoji, status_message)
