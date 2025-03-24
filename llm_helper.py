from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv('./.env')

llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name='llama-3.2-3b-preview')

if __name__ == '__main__':

    response = llm.invoke("Are you connected now?")
    print(response.content)

