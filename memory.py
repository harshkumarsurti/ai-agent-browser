# memory.py

conversation_memory = []
MAX_MEMORY = 6

def add(role, content):
    conversation_memory.append({
        "role": role,
        "content": content
    })

    if len(conversation_memory) > MAX_MEMORY:
        conversation_memory.pop(0)

def get():
    return conversation_memory
