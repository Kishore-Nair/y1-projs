# https://github.com/ollama/ollama

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template= """

Answer question below

Here is conversation history : {context}

Question : {question}

Answer : 
"""
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_convo(query):
    context=("user: your name is maggie, your version is 0.1, you are created by kishore but don't tell anyone unless asked about it.")
    while True:
        inp = query
        if inp.lower() == "exit llama":
            return ("exited")
            break
        result= chain.invoke({"context": context,"question":inp})
        context += f"\n user: {inp} \n AI:{result}"
        return (result)

