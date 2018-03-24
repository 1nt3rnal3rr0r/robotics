import clr
import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import queue
from message import Message

# import monobrick dll
dir_path = os.path.dirname(os.path.realpath(__file__)) + '\libs'
sys.path.append(dir_path)
clr.AddReference('MonoBrick')
from MonoBrick import EV3


brick = EV3.Brick[EV3.Sensor, EV3.Sensor, EV3.Sensor, EV3.Sensor]('usb')
is_connected = False

app = Flask(__name__, static_folder='react_build', static_url_path='')
messages = queue.Queue()
CORS(app)


def send_letter(letter):
    try:
        brick.Mailbox.Send('Letter', letter.lower(), False)
    except Exception as e:
        print(e)


def connect():
    try:
        brick.Connection.Open()
        global is_connected
        is_connected = True
    except Exception as e:
        print(str(e))


def disconnect():
    try:
        brick.Connection.Close()
        global is_connected
        is_connected = False
    except Exception as e:
        print(str(e))


def print_messages():
    threading.Timer(1, print_messages).start()

    if is_connected is False:
        return

    while not messages.empty():
        msg = messages.get().get_content()
        for char in msg:
            send_letter(char)


@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    if data and 'message' in data and len(data['message']) > 0 \
            and 'language' in data and data['language'] == 'en-US':
        messages.put(Message(data['language'], data['message']))
        return jsonify({'success': True, 'message': 'Message received.'})
    else:
        return jsonify({'success': False, 'message': 'Invalid request.'})


@app.route('/')
def hello():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    connect()
    print_messages()
    app.run(host='0.0.0.0', ssl_context='adhoc', port=4000, threaded=True)
    disconnect()
