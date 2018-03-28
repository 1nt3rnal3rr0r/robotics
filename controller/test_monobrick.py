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

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'j', 'з': 'z',
            'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
            'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
            'ш': 'sh', 'щ': 'sht', 'ъ': 'u', 'ь': 'i', 'ю': 'iu', 'я': 'ya'}
BG = 'bg-BG'
EN = 'en-US'


def send_letter(letter):
    try:
        # letter can consist of multiple symbols
        for char in letter:
            brick.Mailbox.Send('Letter', char, False)
    except Exception as e:
        print(e)


def translate_letter(letter, lang):
    let = letter.lower()
    if lang == BG:
        return alphabet[let].lower()
    else:
        return let


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
        msg = messages.get()
        content = msg.get_content()
        language = msg.get_language()
        for char in content:
            translated = translate_letter(char, language)
            send_letter(translated)


@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    if data and 'message' in data and len(data['message']) > 0 \
            and 'language' in data and (data['language'] == EN or data['language'] == BG):
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
