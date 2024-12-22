# Architecture Overview

## Database-Agent-LLM Pattern
This project uses a modular approach:
1. **Database**: Stores raw financial and crypto data.
2. **Agents**: Fetch data from APIs, clean, and store it in the database.
3. **LLM**: Processes user queries and provides intelligent responses.

## Components
- **Database**: SQLite for prototyping (can scale to PostgreSQL or DynamoDB).
- **Agents**: Python scripts for:
  - Fetching API data (e.g., Binance, Tiingo).
  - Querying the database for specific data.
- **LLM**: OpenAI GPT handles analysis and natural language queries.
- **API**: FastAPI exposes endpoints for users and external tools.

## Data Flow
1. User submits a query via the API.
2. The LLM interprets the query and requests data from the agent.
3. The agent fetches data from the database or APIs.
4. The LLM processes the data and returns a response.

## Future Enhancements
- Web3 integration with Ethereum/Polygon.
- Real-time notifications for portfolio changes.
- Teaching dashboards for users to learn about crypto and Web3.
