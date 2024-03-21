from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt import App
from config import Config
from flask import Flask

# Initialize the Slack app
app = App(token=Config.SLACK_BOT_TOKEN)

# Initialize the Flask app
# Flask is a web application framework written in Python
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)