import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())


class Config:

    # Set Slack API credentials
    SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN_SOCKET"]
    SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
    SLACK_BOT_USER_ID = os.environ["SLACK_BOT_USER_ID"]
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    CLIENT_ID = os.environ["CLIENT_ID"]
    CLIENT_SECRET = os.environ["CLIENT_SECRET"]
    SECURE_CONNECT_BUNDLE = os.environ["CONNECTION_FILE_PATH"]
    KEYSPACE = os.environ["KEYSPACE"]
    ASSISTANT_ID = os.environ["ASSISTANT_ID"]
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
