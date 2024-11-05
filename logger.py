import logging
from typing import Dict

class Logger:
    def __init__(self, config: Dict):
        self.logger = logging.getLogger("PointCloudLogger")
        self.logger.setLevel(logging.DEBUG)
        self.file_log = config.get("file_log", False)
        self.print_log = config.get("print_log", True)
        if self.file_log:
            handler = logging.FileHandler(config.get("path", "app.log"))
            handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            self.logger.addHandler(handler)

    def info(self, message: str):
        if self.print_log:
            print(message)
        if self.file_log:
            self.logger.info(message)

    def error(self, message: str):
        if self.print_log:
            print("ERROR:", message)
        if self.file_log:
            self.logger.error(message)
