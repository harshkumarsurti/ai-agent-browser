from flask import Flask, request, jsonify
from agent import run_agent

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return """
    <h2>AI Agent Browser Backend</h2>
    <p>Server is running.</p>
    <p>Use <code>/ask</code> endpoint with POST.</p>
    """

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"error": "Query is empty"}), 400

    answer = run_agent(query)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
