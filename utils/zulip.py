import zulip
from PIL import Image


class ZulipClient:
    def __init__(self, config):
        self.client = zulip.Client(config_file=config.ZULIP_CONFIG_PATH)
        self.config = config

    def send_message(self, stream, topic, content):
        request = {
            "type": "stream",
            "to": f"{stream}",
            "topic": f"{topic}",
            "content": f"{content}",
        }
        return self.client.send_message(request)

    def upload_image(self, stream, topic, image):
        image.save("tmp", "PNG")
        with open("./tmp", "rb") as fp:
            result = self.client.upload_file(fp)
            print(result)
            result = self.client.send_message(
                {
                    "type": "stream",
                    "to": f"{stream}",
                    "topic": f"{topic}",
                    "content": "Check out [your generated color]({}{})!".format(
                        self.config.ZULIP_BASE_URL, result["uri"]
                    ),
                }
            )
            print(result)

    def send_stream_message(self, stream, topic, content):
        return self.send_message("stream", stream, topic, content)

    def send_private_message(self, user_id, content):
        return self.send_message("private", [user_id], None, content)

    def send_help_message(self, message):
        help_text = """
        Here are some things you can ask me to do:
        - Add me to your DAO
        - Curate your lamp configuration
        """
        self.send_reply(message, help_text)

    def handle_message(self, message):
        content = message["content"]
        sender_email = message["sender_email"]

        if content == "!help":
            self.send_help_message(message)
        elif content == "Add me to your DAO":
            self.add_to_dao(sender_email)
        elif content == "Curate my lamp configuration":
            self.curate_lamp(sender_email)
        else:
            self.send_reply(message, "Sorry, I didn't understand that.")

    def send_reply(self, message, content):
        response = {"type": "private", "to": message["sender_id"], "content": content}
        return self.client.send_message(response)

    def add_to_dao(self, sender_email):
        # logic to add the sender's email to the DAO goes here
        response = (
            f"Thanks for your interest, {sender_email}! You've been added to the DAO."
        )
        self.send_private_message(sender_email, response)

    def curate_lamp(self, sender_email):
        # logic to curate the sender's lamp configuration goes here
        response = f"Thanks, {sender_email}! Your lamp configuration has been updated."
        self.send_private_message(sender_email, response)
