from phi.agent import Agent
from phi.model.groq import  Groq
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
from phi.playground import Playground, serve_playground_app

load_dotenv()

web_agent=Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    #model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()], #Uses for fetching the latest news
    instructions=["Always include sources"],
    storage=SqlAgentStorage(table_name="web_agent", db_file="agents.db"),
    add_history_to_messages=True,
    show_tool_calls=True,
    markdown=True,
)

finance_agent=Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    #model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    storage=SqlAgentStorage(table_name="finance_agent", db_file="agents.db"),
    add_history_to_messages=True,
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data."],
    debug_mode=True,
)



app= Playground(agents=[finance_agent, web_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app", reload=True)