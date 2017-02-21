import os
from flask import Flask, request

FB_VERIFY_TOKEN = os.environ.get('FB_VERIFY_TOKEN')

app = Flask(__name__)


@app.route('/messenger', methods=['GET', 'POST'])
def messenger_webhook():
    if request.method == 'GET':
        verify_token = request.args.get('hub.verify_token')
        print(verify_token)
        if verify_token == FB_VERIFY_TOKEN:
            challenge = request.args.get('hub.challenge')
            return challenge
        else:
            return 'Invalid Request or Verification Token'
    elif request.method == 'POST':
        data = request.json
        print(data)
        return ''


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)