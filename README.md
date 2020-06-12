chss
---

Simple python script changes emoji and message to Slack status.

- Runtime: Python 3.8



# Usage

## Preparing

### Create config.json

Create a `config.json` by copying `config.json.sample` .

```bash
$ cp config.json.sample config.json
```

```json
{
  "slack": {
    "user_id": "XXXXXXXX",
    "api_token": "xoxp-********-********-********",
    "default_status_emoji": ":ghost:",
    "default_status_message": "I'm a ghost."
  }
}
```

- `user_id` : your Slack user ID
- `api_token` : your Slack API token
- `default_status_emoji` : default status emoji when the `-e` option is omitted
- `default_status_message` : default status message when the `-m` option is omitted

### Build docker image.

```bash
$ docker build -t michimani/chss .
```

## Execution

```bash
$ docker run michimani/chss -h
usage: change_status.py [-h] [-e EMOJI] [-m MESSAGE]

optional arguments:
  -h, --help            show this help message and exit
  -e EMOJI, --emoji EMOJI
                        Slack emoji code for status icon. (e.g) :ghost:
  -m MESSAGE, --message MESSAGE
                        message for status.
```

#### example

```bash
$ docker run michimani/chss -e ":monkey:" -m "I am a monkey."
```

<img width="262" alt="sc__2020-06-12_234840" src="https://user-images.githubusercontent.com/9986092/84515448-7060f480-ad07-11ea-9f1c-49ebf599a2db.png">
