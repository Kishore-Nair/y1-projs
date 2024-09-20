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

def handle_convo():
    context=""
    while True:
        inp = input("you: ")
        if inp.lower() == "\exit":
            print("exited")
            break
        result= chain.invoke({"context": context,"question":inp})
        print(f"bot {result}")
        context += f"\n user: {inp} \n AI:{result}"


if __name__ == "__main__":
    handle_convo()
