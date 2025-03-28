import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Display the version message set via environment variable
    version = os.environ.get('APP_VERSION', 'unknown')
    return f"Hello from version: {version}!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)

