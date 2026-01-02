from agent import run_agent
from voice import listen, speak

print("🎧 Voice Agent Started (Say 'stop' to exit)")

while True:
    query = listen()

    if query == "":
        continue

    if "stop" in query.lower():
        speak("Goodbye")
        break

    response = run_agent(query)
    print("Agent:", response)

    if response.startswith("ACTION"):
        speak("Executing action")
    else:
        speak(response)
