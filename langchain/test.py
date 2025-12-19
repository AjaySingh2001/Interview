from decouple import config
from langchain_groq import ChatGroq

GROQ_AI_KEY = config("GROQ_AI_KEY")

llm = ChatGroq(groq_api_key = GROQ_AI_KEY)

response = llm.invoke("Lamborghini CEO")
print(response)