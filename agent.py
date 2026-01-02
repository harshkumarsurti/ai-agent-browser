import requests
import memory
from prompt import SYSTEM_PROMPT


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi"

def run_agent(user_input):
    text = user_input.lower()

    # store user message
    memory.add("User", user_input)

    # 🔥 HARD ACTION OVERRIDE
    if "youtube" in text:
        return "ACTION:OPEN_URL:https://www.youtube.com"

    if "google" in text:
        return "ACTION:OPEN_URL:https://www.google.com"

    if "github" in text:
        return "ACTION:OPEN_URL:https://github.com"

    # build conversation context
    context = ""
    for msg in memory.get():
        context += f'{msg["role"]}: {msg["content"]}\n'

    payload = {
        "model": MODEL_NAME,
        "prompt": f"{SYSTEM_PROMPT}\n{context}Agent:",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload).json()
    reply = response["response"]

    # store agent reply
    memory.add("Agent", reply)

    return reply
