from llama_index import DiscordReader, GPTSimpleVectorIndex, SimpleDirectoryReader
from llama_index.readers.obsidian import ObsidianReader
from agent.config import config
import gradio as gr
import os


class IndexModel:
    def __init__(self, config):
        # Check if index already exists
        index_path = os.path.abspath(
            os.path.join(os.getcwd(), config.index["INDEX_PATH"])
        )
        if os.path.exists(index_path):
            print("loading index from disk...")
            self.index = GPTSimpleVectorIndex.load_from_disk(index_path)
        else:
            print("initializing index, this may take a moment...")

        if index_path is None:
            raise ValueError("INDEX_PATH config variable not set.")
        index_mode = config.index["INDEX_MODE"]
        if index_mode is None:
            raise ValueError("INDEX_MODE config variable not set.")
        if index_mode == "directory":
            documents = self.read_directory(config)
        elif index_mode == "discord":
            documents = self.read_discord(config)
        else:
            raise ValueError("unrecognized INDEX_MODE config variable.")

        index = GPTSimpleVectorIndex(documents)
        index.save_to_disk(index_path)
        print("index finished.")
        self.index = index

    def read_directory(self, config):
        data_dir = config.index["DATA_DIR"]
        if data_dir is None:
            raise ValueError("DATA_DIR config variable not set.")
        print(f"directory source: {data_dir}")
        return SimpleDirectoryReader(data_dir).load_data()

    def read_discord(self, config):
        print("reading discord channels...")
        token = os.getenv("DISCORD_TOKEN")
        if token is None:
            raise ValueError("DISCORD_TOKEN not set")
        channel_ids = config.discord["CHANNEL_IDS"]
        if token is None:
            raise ValueError("CHANNEL_IDS config variable not set")
        return DiscordReader(discord_token=None).load_data(channel_ids=channel_ids)

    def get_index(self):
        return self.index

    def query(self, question):
        print("question received: ", question)
        return self.index.query(question)
