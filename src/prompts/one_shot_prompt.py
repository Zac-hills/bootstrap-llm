from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

template = """{question}"""

prompt = PromptTemplate(template=template, input_variables=["question"])

# replace with your desired local file path
local_path = '../models/ggml-mpt-7b-chat.bin'

# Callbacks support token-wise streaming
callbacks = [StreamingStdOutCallbackHandler()]
# Verbose is required to pass to the callback manager
llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True)

llm_chain = LLMChain(prompt=prompt, llm=llm)


def one_shot(question: str):
    return llm_chain.run(question)
