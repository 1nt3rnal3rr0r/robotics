from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import queue
import letters
from message import Message

app = Flask(__name__)
messages = queue.Queue()
CORS(app)
lettersPrinted = 1
lettersPerLine = 4

atBeginning = False

def print_messages():
    global atBeginning

   #go at the beginning of the page
    letters.beginningOfThePage()

    print("print_message")

    parseText("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def parseText(text):
    global lettersPrinted


    for letter in text:
        if (lettersPrinted % lettersPerLine == 0):
            letter.newLine()
        else:
            if(letter == 'a' or letter == 'A'):
                letters.printA()
            if (letter == 'b' or letter == 'B'):
                letters.printB()
            if (letter == 'c' or letter == 'C'):
                letters.printC()
            if (letter == 'd' or letter == 'D'):
                letters.printD()
            if (letter == 'e' or letter == 'E'):
                letters.printE()
            if (letter == 'f' or letter == 'F'):
                letters.printF()
            if (letter == 'g' or letter == 'G'):
                letters.printG()
            if (letter == 'h' or letter == 'H'):
                letters.printH()
            if (letter == 'i' or letter == 'I'):
                letters.printI()
            if (letter == 'j' or letter == 'J'):
                letters.printJ()
            if (letter == 'k' or letter == 'K'):
                letters.printK()
            if (letter == 'l' or letter == 'L'):
                letters.printL()
            if (letter == 'm' or letter == 'M'):
                letters.printM()
            if (letter == 'n' or letter == 'N'):
                letters.printN()
            if (letter == 'o' or letter == 'O'):
                letters.printO()
            if (letter == 'p' or letter == 'P'):
                letters.printP()
            if (letter == 'q' or letter == 'Q'):
                letters.printQ()
            if (letter == 'r' or letter == 'R'):
                letters.printR()
            if (letter == 's' or letter == 'S'):
                letters.printS()
            if (letter == 't' or letter == 'T'):
                letters.printT()
            if (letter == 'u' or letter == 'U'):
                letters.printU()
            if (letter == 'v' or letter == 'V'):
                letters.printV()
            if (letter == 'w' or letter == 'W'):
                letters.printW()
            if (letter == 'x' or letter == 'X'):
                letters.printX()
            if (letter == 'y' or letter == 'Y'):
                letters.printY()
            if (letter == 'z' or letter == 'Z'):
                letters.printZ()
        lettersPrinted += 1
        print(letter)



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
    # app.run(host='0.0.0.0', ssl_context='adhoc', port=4000, threaded=True)