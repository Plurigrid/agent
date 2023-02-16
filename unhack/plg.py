from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from IPython.display import Markdown, display
import os

index_path='plurigrid.json'

if os.path.exists(index_path):
    index = GPTSimpleVectorIndex.load_from_disk(index_path)
else:
    print('initializing index, this may take a moment...')
    documents = SimpleDirectoryReader('data/plurigrid').load_data()
    index = GPTSimpleVectorIndex(documents)
    index.save_to_disk(index_path)

print('ask any questions, press CTRL+C to quit...')
while True:
    question = input(">>> ")
    print('querying response...')
    res = index.query(question)
    print(res.response)
