from application_factory import flask_app, app, handler,assistant
from config import Config
from modules.functions_factory import draft_email
from flask import request, Blueprint


action_bp = Blueprint("action", __name__)

@app.event("message")
def handle_message_events(body, logger):
    print(body)

@app.event("app_mention")
def handle_mentions(body, say):
    """
    Event listener for mentions in Slack.
    When the bot is mentioned, this function processes the text and sends a response.

    Args:
        body (dict): The event data received from Slack.
        say (callable): A function for sending a response to the channel.
    """
    text = body["event"]["text"]

    mention = f"<@{Config.SLACK_BOT_USER_ID}>"
    text = text.replace(mention, "").strip()

   # response = my_function(text)
    if text:
        resp = assistant.run_assistant(text)
    #else:
    #    assistant.delete_thread()
    #    response = "Closed chat"
    say(resp)


@action_bp.route("/slack/events", methods=["POST"])
def slack_events():
    """
    Route for handling Slack events.
    This function passes the incoming HTTP request to the SlackRequestHandler for processing.

    Returns:
        Response: The result of handling the request.
    """
    return handler.handle(request)
