from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
import openai

from dotenv import load_dotenv
load_dotenv()


openai.api_key=os.getenv("OPENAI_API_KEY")
Groq.api_key=os.getenv("GROQ_API_KEY")
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

## Multi AI Agent combining both agents

multi_AI_Agent= Agent(
    team=[web_serach_agent,finance_agent],
    instructions=["Always include the sources", "use table to display the data"],
    show_tool_calls=True,
    markdown=True,

)

multi_AI_Agent.print_response("Summarize the analyst recommendation and share the latest news for NVIDIA", stream=True)