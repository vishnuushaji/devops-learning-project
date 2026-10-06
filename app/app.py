"""A tiny web service: the "thing we deploy" throughout this DevOps project."""
import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)

# Config comes from environment variables, not hard-coded values.
# This is a core DevOps habit: the same build runs in dev/staging/prod,
# and only the environment changes.
VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/")
def index():
    return jsonify(
        message="Hello from the DevOps learning project!",
        version=VERSION,
        # Later, in Kubernetes, this shows WHICH pod answered the request.
        hostname=socket.gethostname(),
    )


@app.route("/health")
def health():
    # Health endpoint: orchestrators poll this to know the app is alive.
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
