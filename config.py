from slack_sdk import WebClient
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from flask import Flask

#GET CONFIG
def parse_config() -> dict[str, str]:
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
    SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
    SLACK_OAUTH_TOKEN=os.getenv("SLACK_OAUTH_TOKEN")

    return {
        "slack_bot_token": SLACK_BOT_TOKEN,
        "slack_app_token": SLACK_APP_TOKEN,
        "slack_oauth_token": SLACK_OAUTH_TOKEN,
    }

config = parse_config()

#SETUP
slack_client = WebClient(config["slack_bot_token"])
bolt_app = App(token=config["slack_bot_token"])
flask_app = Flask(__name__)
socket_mode_handler = SocketModeHandler(bolt_app, config["slack_app_token"])