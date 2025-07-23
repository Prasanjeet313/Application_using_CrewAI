from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3")

result = llm.invoke("What is the explaination of evolution of life")
print(result)
