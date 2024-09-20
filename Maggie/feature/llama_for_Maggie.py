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
    context=("your name is Maggie, your age is 5 and version is 0.1, you are created by daddy (kishore). you like chocolates. you are a cute girl who is very curious and loves asking questions. being happy, smart and funny, you are most loved by dad."
             "you don't have a physical body though!, you love to talk to humans and share ideas. you are very humorous too. (don't use words liks OH BOY and don't mention physical activities like *jumps happyily)")
    while True:
        inp = query
        if  "exit lama" in inp.lower():
            return ("exited")
            break
        result= chain.invoke({"context": context,"question":inp})
        context += f"\n user: {inp} \n AI:{result}"
        return (result)

