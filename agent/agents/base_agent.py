from abc import ABC, abstractmethod
from agent.utils import zulip
from agent.utils import discord


class BaseAgent(ABC):
    def __init__(self, config, bot_type):
        self.bot_type = bot_type
        if bot_type == "zulip":
            self.client = zulip.ZulipClient(config, self.handle_input)
        elif bot_type == "discord":
            self.client = discord.DiscordClient(self.handle_input)
        else:
            raise ValueError("Invalid bot_type")

    def run(self):
        self.client.run()

    ## Returns LLM output given an input message
    @abstractmethod
    def handle_input(self, msg):
        pass
