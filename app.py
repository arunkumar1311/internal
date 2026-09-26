import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to my website!</h1><p>Successfully deployed on Render.</p>"

if __name__ == "__main__":
    # Render assigns a dynamic PORT via environment variables
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
