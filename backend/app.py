# backend/app.py
import os
import string
import random
from flask import Flask, request, redirect, render_template, jsonify
import redis

REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)
BASE_URL = os.environ.get("BASE_URL", "http://localhost:5000/")

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

app = Flask(__name__)

ALPHABET = string.ascii_letters + string.digits
SHORT_LEN = 6

def generate_short():
    return ''.join(random.choices(ALPHABET, k=SHORT_LEN))

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/shorten", methods=["POST"])
def shorten():
    long_url = request.form.get("url") or request.json.get("url")
    if not long_url:
        return jsonify({"error": "No URL provided"}), 400

    # try to avoid collisions
    for _ in range(5):
        short = generate_short()
        if not r.exists(f"url:{short}"):
            r.set(f"url:{short}", long_url)
            r.set(f"count:{short}", 0)
            return jsonify({"short_url": BASE_URL + short})
    return jsonify({"error": "Could not generate short URL"}), 500

@app.route("/<short>")
def redirect_short(short):
    long_url = r.get(f"url:{short}")
    if not long_url:
        return jsonify({"error": "Not found"}), 404
    r.incr(f"count:{short}")
    return redirect(long_url, code=302)

@app.route("/analytics/<short>")
def analytics(short):
    long_url = r.get(f"url:{short}")
    if not long_url:
        return jsonify({"error": "Not found"}), 404
    count = r.get(f"count:{short}") or "0"
    return jsonify({"short": short, "long_url": long_url, "clicks": int(count)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
