from flask import Flask, request, jsonify
from flask_cors import CORS
import queue
import letters

app = Flask(__name__, static_folder='react_build', static_url_path='')
messages = queue.Queue()
CORS(app)
lettersPrinted = 1
lettersPerLine = 4

atBeginning = False

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'j', 'з': 'z',
            'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
            'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
            'ш': 'sh', 'щ': 'sht', 'ъ': 'u', 'ь': 'i', 'ю': 'iu', 'я': 'ya'}
BG = 'bg-BG'
EN = 'en-US'


def translate_msg(msg, lang):
    if lang == BG:
        translated = ""
        for char in msg:
            translated += alphabet[char].lower()
        return translated
    else:
        return msg


def print_message(msg):
    global atBeginning

    print(msg)

    # go at the beginning of the page
    letters.beginningOfThePage()
    print('print_message')

    parse_text(msg)


def parse_text(text):
    global lettersPrinted

    for letter in text:
        if lettersPrinted % lettersPerLine == 0:
            letters.newLine()
        else:
            if letter == 'a' or letter == 'A':
                letters.printA()
            if letter == 'b' or letter == 'B':
                letters.printB()
            if letter == 'c' or letter == 'C':
                letters.printC()
            if letter == 'd' or letter == 'D':
                letters.printD()
            if letter == 'e' or letter == 'E':
                letters.printE()
            if letter == 'f' or letter == 'F':
                letters.printF()
            if letter == 'g' or letter == 'G':
                letters.printG()
            if letter == 'h' or letter == 'H':
                letters.printH()
            if letter == 'i' or letter == 'I':
                letters.printI()
            if letter == 'j' or letter == 'J':
                letters.printJ()
            if letter == 'k' or letter == 'K':
                letters.printK()
            if letter == 'l' or letter == 'L':
                letters.printL()
            if letter == 'm' or letter == 'M':
                letters.printM()
            if letter == 'n' or letter == 'N':
                letters.printN()
            if letter == 'o' or letter == 'O':
                letters.printO()
            if letter == 'p' or letter == 'P':
                letters.printP()
            if letter == 'q' or letter == 'Q':
                letters.printQ()
            if letter == 'r' or letter == 'R':
                letters.printR()
            if letter == 's' or letter == 'S':
                letters.printS()
            if letter == 't' or letter == 'T':
                letters.printT()
            if letter == 'u' or letter == 'U':
                letters.printU()
            if letter == 'v' or letter == 'V':
                letters.printV()
            if letter == 'w' or letter == 'W':
                letters.printW()
            if letter == 'x' or letter == 'X':
                letters.printX()
            if letter == 'y' or letter == 'Y':
                letters.printY()
            if letter == 'z' or letter == 'Z':
                letters.printZ()
        lettersPrinted += 1
        print(letter)


@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    if data and 'message' in data and 'language' in data:
        if len(data['message']) > 0 and data['language'] == EN or data['language'] == BG:
            translated = translate_msg(data['message'], data['language'])
            print_message(translated)
            return jsonify({'success': True, 'message': 'Message received.'})

    return jsonify({'success': False, 'message': 'Invalid request.'})


@app.route('/')
def hello():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', ssl_context='adhoc', port=4000, threaded=False)
