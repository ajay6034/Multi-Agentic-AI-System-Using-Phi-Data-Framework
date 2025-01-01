## Building Multi Agentic AI System

### Overview
- The project involves the implementation of agentic AI using the phi library, focusing on creating AI agents with specific roles that interact with various data sources like financial data from YFinance and web search results from DuckDuckGo. These agents are integrated into a user-friendly interface using the phi Playground.

### Agents Implementation
#### Common Setup
- Each agent is implemented using the phi.agent module. The basic setup involves:

**Model Assignment:** Each agent is assigned a model. In this case, Groq's Llama model (llama-3.2-1b-preview) is used due to its capability to process and understand complex queries and data.
**Tools Configuration:** Agents are equipped with specific tools (YFinanceTools and DuckDuckGo) to fetch data according to their roles.
**Environment Variables:** API keys and other sensitive data are loaded using the dotenv package to maintain security and ease of configuration changes.
#### Web Search Agent
**Role:** This agent is designed to search the web for information.
**Tools:** Uses DuckDuckGo to perform web searches.
**Instructions:** It is instructed to always include sources from where it retrieves information to ensure transparency and reliability.
**Output:** Configured to show tool calls and render results in Markdown for better readability and integration in web-based displays.
#### Finance Agent
**Role:** Focuses on fetching financial data.
**Tools:** Utilizes YFinanceTools to access a wide array of financial data such as stock prices, analyst recommendations, fundamentals, and latest company news.
**Instructions:** The agent is configured to use tables to display the data neatly, which is essential for financial data readability.
**Interaction:** Similar to the Web Search Agent in terms of showing tool calls and using Markdown for output formatting.
#### Multi AI Agent
**Role:** Combines the capabilities of both the Web Search and Finance agents to provide a comprehensive response to queries that require both financial and general web information.
**Configuration:** Inherits the team of agents and aggregates their capabilities, ensuring that all outputs follow the given instructions about source inclusion and data display.
**Functionality:** Capable of handling complex queries that involve summarizing and cross-referencing information from both financial and web domains.
#### Playground Integration
The playground.py script sets up a phi Playground environment which allows for the interactive utilization of the defined agents.

**App Configuration:** A Playground instance is created with both agents added. This configuration allows users to interact with the agents through a web interface.
**Server Setup:** The script uses Flask-like commands to serve the Playground app, enabling real-time interaction and immediate display of agent outputs.
**Interactivity:** Users can input queries directly into the Playground interface, and the app dynamically utilizes the appropriate agents to fetch and display the information.
#### Security and Configuration
**Environment Variables:** Security-sensitive data such as API keys are managed through environment variables, ensuring that they remain secure and are easily configurable without altering the codebase.
**Dotenv Integration:** The use of a .env file streamlines the process of managing environment variables, making it easy to update and maintain without touching the core script.
#### Conclusion
- The implementation of agentic AI in this project demonstrates a sophisticated use of AI models and tools to create a responsive, data-driven application. By leveraging the phi library and configuring AI agents with specific roles and capabilities, the project efficiently handles diverse data retrieval tasks, offering a robust solution for financial data analysis and web search integration.

- This detailed explanation provides a comprehensive view of your agentic AI implementation and can be useful for users or collaborators looking to understand or contribute to your project.