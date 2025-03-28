import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Use the GREETING environment variable if set
    greeting = os.environ.get('GREETING', 'Hello, Continuous Delivery!')
    return greeting

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)

