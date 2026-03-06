from flask import Flask, render_template
import sys
import os

app = Flask(__name__)

@app.get("/")
def home():
    # Read secret from environment variable
    secret_value = os.getenv("MY_SECRET", "No Secret Found")

    return render_template(
        "index.html",
        python_version=sys.version,
        secret_value=secret_value
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
