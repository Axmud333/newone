import os
from dotenv import load_dotenv
from anthropic import Anthropic, APIError, RateLimitError
import anthropic
import logging
from backend.qdrant_search import qdrant_search

load_dotenv()
logging.basicConfig(filename="logs/chat_logs.txt", level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s" )
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic()

def ask_claude(prompt: str, database: str = None):


    system_message = """
    You are an assistant for university of sulaimani.
    -try to be short and precise.
    -you were made by the computer engineering department
    -answer in the language of the question.
    -answer based on the given database given below.
    """
    if database:
        full_message = f"Database content:\n{database}\n\nQuestion: {prompt}"
    else:
        full_message = f"Question: {prompt}"

    try: 
        message = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=1000,
        temperature=1,
        system= system_message,
        messages=[
            {
                "role": "user","content": full_message
                    
            }
        ]
    )
        return message.content[0].text
    except RateLimitError as e:
        logging.error(f"Claude rate limit: {e}")
        raise Exception("Claude API rate limited ")
    
    except APIError as e:
        logging.error(f"Claude API error: {e}")
        raise Exception("Claude API error")
    
    except Exception as e:
        logging.error(f"Unknown claude error: {e}")
        raise
