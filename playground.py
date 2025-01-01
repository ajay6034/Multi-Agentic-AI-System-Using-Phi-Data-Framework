from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
import phi.api
import openai
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv

# load the environment variable from .env file
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

# Web search Agent

web_serach_agent=Agent(
    name="Web Search Agent",
    role="search the web for the information",
    model=Groq(id='llama-3.2-1b-preview'),
    tools=[DuckDuckGo()],
    instructions=["Always include sources from where you getting the info"],
    show_tool_calls=True,
    markdown=True,

)

## Finance Agent

finance_agent= Agent(
    name="Finance Agent",
    role="search the Yfinance for the information",
    model=Groq(id='llama-3.2-1b-preview'),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)

app=Playground(agents=[finance_agent,web_serach_agent]).get_app()


if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)
