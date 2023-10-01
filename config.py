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

    #if SLACK_BOT_TOKEN == None:
    #    SLACK_BOT_TOKEN = "xoxb-5346423705716-5338666388310-My48fTKtsPFOcjda0H1uH8Ya"

    #if SLACK_APP_TOKEN == None:
    #    SLACK_APP_TOKEN = "xapp-1-A05A400GY83-5373369356882-beb4ef52a65b5e07183a0624397b6b8cfe24e2f141bb7fa57eaac014556f9b60"

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