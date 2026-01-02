import requests
import memory
from prompt import SYSTEM_PROMPT

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi"

# 🗺️ Intent → URL map (agent brain)
SITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com"
}

def run_agent(user_input):
    text = user_input.lower().strip()

    # store user message
    memory.add("User", user_input)

    # 🔥 INTENT-BASED ACTION HANDLER (NO LINKS TO USER)
    if text.startswith("open "):
        site_name = text.replace("open ", "").strip()

        if site_name in SITES:
            return f"ACTION:OPEN_URL:{SITES[site_name]}"
        else:
            return f"I don't know how to open {site_name}"

    # 🧠 Build conversation context from memory
    context = ""
    for msg in memory.get():
        context += f'{msg["role"]}: {msg["content"]}\n'

    payload = {
        "model": MODEL_NAME,
        "prompt": f"{SYSTEM_PROMPT}\n{context}Agent:",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload).json()
    reply = response.get("response", "").strip()

    # store agent reply
    memory.add("Agent", reply)

    return reply
