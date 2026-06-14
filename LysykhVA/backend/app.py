from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    text = data["text"]

    with open("/data/task.txt", "w", encoding="utf-8") as f:
        f.write(text)

    while not os.path.exists("/data/result.txt"):
        time.sleep(1)

    with open("/data/result.txt", "r", encoding="utf-8") as f:
        result = f.read()

    os.remove("/data/result.txt")

    return jsonify({
        "result": result
    })

app.run(
    host="0.0.0.0",
    port=5000
)