from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import queue

app = Flask(__name__)
messages = queue.Queue()
CORS(app)


def print_messages():
    threading.Timer(1, print_messages).start()
    while not messages.empty():
        print(messages.get())


@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    if data and 'message' in data and len(data['message']) > 0 \
            and 'language' in data and len(data['language']) > 0:
        print(data['language'])
        messages.put(data['message'])
        return jsonify({'success': True, 'message': 'Message received.'})
    else:
        return jsonify({'success': False, 'message': 'Invalid request.'})


@app.route('/')
def hello():
    return 'Hello!'


if __name__ == "__main__":
    print_messages()
    app.run(host='0.0.0.0', ssl_context='adhoc', port=4000, threaded=True)
