# Email Inbox Summarizer Agent using MCP

An AI-powered Email Inbox Summarizer Agent built using **LangChain, Google Gemini, and MCP (Model Context Protocol)**.

## Features

- Fetch unread emails from Gmail
- Summarize emails using AI
- Categorize emails as:
  - URGENT
  - NEEDS REPLY
  - FYI / INFORMATIONAL
- Create draft replies for important emails
- Use MCP to connect external tools
- Powered by Google Gemini

## Tech Stack

- Python
- LangChain
- Google Gemini
- MCP (Model Context Protocol)
- Composio
- Gmail

## Project Flow

User  
↓  
LangChain Agent  
↓  
Google Gemini  
↓  
MCP  
↓  
Gmail Tools  
↓  
Fetch Emails / Summarize / Draft Replies

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/email-inbox-summarizer-agent-mcp.git
cd email-inbox-summarizer-agent-mcp
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project directory:

```env
GOOGLE_API_KEY=your_google_api_key
COMPOSIO_API_KEY=your_composio_api_key
```

Never share or commit your API keys.

## Run the Project

```bash
python app.py
```

## Example

The agent can process a request such as:

```text
Check my inbox, summarize all unread emails, and draft replies for any that look important or need a response.
```

The agent then uses MCP tools to access the required Gmail functionality and generates a structured inbox summary.

## .gitignore

Make sure your `.gitignore` contains:

```gitignore
.env
__pycache__/
*.pyc
```

## Future Improvements

- Add email priority detection
- Add automatic labeling
- Support multiple email accounts
- Improve reply generation
- Add a web interface
- Add scheduled inbox summaries

## Author

Siva
