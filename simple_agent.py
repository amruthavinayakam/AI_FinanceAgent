from phi.agent import Agent
from phi.model.groq import  Groq
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

agent.print_response("write me a poem that pasta sings to dal chaawal")