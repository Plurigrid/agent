from enum import Enum

import json
import os


class Config:
    def __init__(self, config_path="~/agent_config.json"):
        config_file = os.path.expanduser(config_path)
        if not os.path.exists(config_file):
            raise ValueError("agent_config.json not found")
        with open(config_file) as f:
            config_data = json.load(f)
        self.__dict__ = config_data
