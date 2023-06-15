# Introduction to Code Development

## Section 1: Environment Setup

- The first task is creating a virtual environment and installing all of the dependencies from the requirements file.
- Add the OpenAI key to the .env File.

## Section 2: Technologies

- The technologies we will be using today are python, Langchain, and FastAPI.
- FastAPI is a simple web framework which we will use to serve the API.

## Section 3: Models

- There are two models we will be using today: ChatOpenAI and OpenAI.
- The differences between the two models is the API that is in front of the LLM.
- The ChatOpenAI uses the Chat API and expects multiple messages.
- The OpenAI uses the Completion API and expects a single message.

## Section 4: Prompt Engineering

- Let's create our first basic example of prompt engineering using LangChain.
- First, we need a string template that expects the variable 'input' to be injected into it.
- Now let's add it to a PromptTemplate, which represents a prompt to the LLM.
- Now we can use the PromptTemplate to generate a prompt using the user input and send it to ChatGPT.

## Section 5: Translator Route

- Let's make a translator route.
- The Translation prompt is going to initially follow the same path as the basic example.
- First, let's create our system template string.
- Notice we are using a tactic here, asking ChatGPT to pretend to be an assistant, which helps focus the LLM on the specific task.
- Next, let's use a SystemMessagePromptTemplate to denote instructions for the LLM.
- Next, define the human string template, which takes a single variable and is injected into the string.
- Then, add it to the HumanMessagePromptTemplate.
- Next, combine the System and Human prompt templates together using the ChatPromptTemplate.
- Now we can use the translator prompt and send it off to ChatGPT.

## Section 6: Few Shot Prompts

- We can use Few Shot Prompts to provide examples to ChatGPT on how to behave given the question.
- Let's define the examples and wrap them in an example_prompt.
- We add the suffix to inject the user input.
- Now we can use the FewShotPrompt with ChatGPT.

## Section 7: Advanced Features - Exposing Tools to ChatGPT

- Agents are used to expose tools to ChatGPT for usage.
- Let's create a function and expose it to ChatGPT to use.
- This is a basic add function that takes two parameters and adds them together.
- Next, we define the parameter schema of the function using Pydantic.
- The argument schema and function are wrapped into a prompt using the StructuredTool.

## Section 8: Testing with the Add Function

- Finally, we create an agent that acts as the glue between our tool and ChatGPT.
- Now we can test it out with the add function.

## Section 9: Data Extraction using Prompts

- We can define a structure and ask ChatGPT to extract information from the input and return the information in the defined structure.
- Let's define a structure to extract information about a document using prompts.
