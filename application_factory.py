from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt import App
from config import Config
from flask import Flask
from models.database_factory import DatabaseEngine
from modules.chat_factory import ChatWithAssistant


# Initialize the Slack app
app = App(token=Config.SLACK_BOT_TOKEN)

# Initialize the Flask app
# Flask is a web application framework written in Python
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)
db = DatabaseEngine()
assistant = ChatWithAssistant()
