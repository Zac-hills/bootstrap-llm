from fastapi import FastAPI
from prompts.one_shot_prompt import one_shot
app = FastAPI()


@app.post("/")
async def root(input: str):
    return one_shot(input)
