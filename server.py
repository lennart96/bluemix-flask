import os
from flask import Flask

PORT = int(os.getenv('VCAP_APP_PORT', 8000))

app = Flask(__name__)

@app.route('/')
def main():
    return 'hello world'

if __name__ == '__main__':
    app.run(port=PORT, host='', debug=False)
