from tqdm import tqdm
from pathlib import Path
import requests

local_path = './models/ggml-mpt-7b-chat.bin'

Path(local_path).parent.mkdir(parents=True, exist_ok=True)
# Example model. Check https://github.com/nomic-ai/gpt4all for the latest models.
url = 'http://gpt4all.io/models/ggml-mpt-7b-chat.bin'
# send a GET request to the URL to download the file. Stream since it's large
response = requests.get(url, stream=True)
# open the file in binary mode and write the contents of the response to it in chunks
# This is a large file, so be prepared to wait.
with open(local_path, 'wb') as f:
    for chunk in tqdm(response.iter_content(chunk_size=8192)):
        if chunk:
            f.write(chunk)
