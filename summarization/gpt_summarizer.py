import os
from dotenv import load_dotenv
from openai import OpenAI

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(f"OPENAI_API_KEY not found. Checked path: {env_path}")

client = OpenAI(api_key=api_key)

system_prompt = """
You are a smart AI assistant. Given a transcript of a meeting, summarize it and extract any action items.
Format:

### Summary:
[Summary]

### Action Items:
- [Item 1]
- [Item 2]
"""

def generate_summary_and_actions(transcript):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcript},
        ],
        temperature=0.4
    )
    return response.choices[0].message.content
