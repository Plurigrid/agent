import discord
import os


class DiscordClient(discord.Client):
    def __init__(self, msg_handler):
        token = os.getenv("DISCORD_TOKEN")
        if token is None:
            raise ValueError("DISCORD_TOKEN not set")
        self.token = token
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        intents.dm_messages = True
        intents.messages = True
        intents.guilds = True
        super().__init__(intents=intents)
        self.msg_handler = msg_handler

    async def on_ready(self):
        print("Discord bot is live!")

    async def on_message(self, message):
        if self.user.mentioned_in(message):
            await message.channel.send(self.msg_handler(message.content))

    def run(self):
        print("waiting for messages..")
        super().run(self.token)
