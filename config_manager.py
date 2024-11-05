import yaml
from typing import Dict

class ConfigManager:
    def __init__(self, config_path: str):
        self.config_path = config_path

    def load_config(self) -> Dict:
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)
