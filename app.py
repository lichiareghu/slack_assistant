from application_factory import flask_app
from modules.logger_factory import SlackAssistantLogger
from routes.action import action_bp

logger = SlackAssistantLogger(log_directory_path='log/', log_to_file=True)
logger.set_logger()

# register endpoint for the enquiry api
flask_app.register_blueprint(action_bp)

# Run the Flask app
if __name__ == "__main__":
    flask_app.run()
