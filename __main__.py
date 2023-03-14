import argparse
from agent.agents.digital_twin import DigitalTwin
from agent.config import config


def run():
    parser = argparse.ArgumentParser(description="Agent")
    parser.add_argument(
        "--bot-type",
        choices=["zulip", "discord"],
        help="Specify the type of bot to run",
        required=True,
    )
    args = parser.parse_args()
    agent = DigitalTwin(config.Config(), bot_type=args.bot_type)
    agent.run()


if __name__ == "__main__":
    run()
