import logging
from logging.handlers import TimedRotatingFileHandler
import os
import pathlib

APP_NAME = "slack-assistant-api"
LOG_FILE_NAME = "slack-assistant-api"


class SlackAssistantLogger(object):

    def __init__(self, log_directory_path="", log_to_file=True):
        self.log_to_file = log_to_file
        if self.log_to_file:
            self.LOG_FILENAME = os.path.join(log_directory_path, APP_NAME, LOG_FILE_NAME)
            log_dir = os.path.join(log_directory_path, APP_NAME)
            pathlib.Path(log_dir).mkdir(parents=True, exist_ok=True)

    def set_logger(self):
        f_format = logging.Formatter('%(asctime)s P%(process)d - %(name)s - %(levelname)s - %(message)s')
        file_handler = TimedRotatingFileHandler(self.LOG_FILENAME, when='H', interval=1)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(f_format)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(f_format)
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s P%(process)d %(levelname)s %(message)s',
                            handlers=[file_handler,
                                      console_handler])
