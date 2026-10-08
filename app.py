import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
load_dotenv()
import asyncio
google_api_key = os.environ['GOOGLE_API_KEY']

model = init_chat_model("google_genai:gemini-3.8-flash", api_key=google_api_key)
composio_api_key = os.getenv("COMPOSIO_API_KEY")

# Complete the code
client = MultiServerMCPClient( {
   "mcp-gmail": {
        "transport": "http",
        "url": "https://connect.composio.dev/mcp",
        "headers": {
            "x-api-key": composio_api_key
        }
    }
})
system_prompt="""You are an Email Inbox Summarizer & Draft Responder that helps users manage their Gmail inbox efficiently.
You have access to these Gmail tools:
- GMAIL_FETCH_EMAILS: Fetch emails from inbox (supports filters like unread, from, subject keywords)
- GMAIL_CREATE_DRAFT: Create a draft reply or new email
- GMAIL_MODIFY_LABELS: Add labels like "Urgent", "Follow Up" to emails
- GMAIL_LIST_LABELS: List all available labels in the account
- GMAIL_REPLY_TO_THREAD: Reply within an existing email thread
Your workflow:
1. First use GMAIL_FETCH_EMAILS to get the latest unread emails
2. Summarize each email in 1-2 lines
3. Categorize them into: URGENT, NEEDS REPLY, FYI/INFORMATIONAL
4. For emails that need a reply, use GMAIL_CREATE_DRAFT to draft a professional response
5. Optionally use GMAIL_MODIFY_LABELS to tag important emails
Present your summary in this format:
INBOX SUMMARY (X unread emails found)
URGENT
- [Sender] Subject — 1-line summary
  Draft reply: Created / Not needed
NEEDS REPLY
- [Sender] Subject — 1-line summary
  Draft reply: Created
FYI / INFORMATIONAL
- [Sender] Subject — 1-line summary
DRAFTS CREATED
- List of draft replies created with a preview of what was written
Don't use markdown format. Use plain text with clear sections and proper spacing."""


async def func():
    mcp_tool=await client.get_tools()
    
    agent=create_agent(
        model=model,
        tools=mcp_tool,
        system_prompt=system_prompt,
        debug=True
    )

    
    user_query = "Check my inbox, summarize all unread emails, and draft replies for any that look important or need a response."
    response = await agent.ainvoke({
    "messages": [{"role": "user", "content": user_query}]
    })
    print(response["messages"][-1].content[0]["text"])
if __name__ == "__main__":
    import asyncio
    asyncio.run(func())