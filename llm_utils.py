from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# Intilaize LLMA LLM for query
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.2-90b-text-preview")


if __name__ == "__main__":
    response = llm.invoke("How to play cricket? ")
    print(response.content)