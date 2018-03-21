from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import queue
from time import sleep

app = Flask(__name__)
messages = queue.Queue()
CORS(app)

whiteApproximation = 180

isPrinting = False

xMotor = LargeMotor('out2')
yMotor = LargeMotor('out3')
zMotor = LargeMotor('out1')

colorSensor = ColorSensor('outB')
colorSensor.mode = 'RGB-RAW'


def print_messages():
    threading.Timer(1, print_messages).start()
    if colorSensor.value(0)>whiteApproximation and colorSensor.value(1)>whiteApproximation and colorSensor.value(2)>whiteApproximation:
        while not messages.empty():
            if(not isPrinting):
                isPrinting = True
                printA()
                parseText(messages.get())

def parseText(text):
    for letter in text:
        if(letter == 'a' or letter == 'A'):
            printA()
        if (letter == 'b' or letter == 'B'):
            printB()
        if (letter == 'c' or letter == 'C'):
            printC()
        if (letter == 'd' or letter == 'D'):
            printD()
        if (letter == 'e' or letter == 'E'):
            printE()
        if (letter == 'f' or letter == 'F'):
            printF()
        if (letter == 'g' or letter == 'G'):
            printG()
        if (letter == 'h' or letter == 'H'):
            printH()
        if (letter == 'i' or letter == 'I'):
            printI()
        if (letter == 'j' or letter == 'J'):
            printJ()
        if (letter == 'k' or letter == 'K'):
            printK()
        if (letter == 'l' or letter == 'L'):
            printL()
        if (letter == 'm' or letter == 'M'):
            printM()
        if (letter == 'n' or letter == 'N'):
            printN()
        if (letter == 'o' or letter == 'O'):
            printO()
        if (letter == 'p' or letter == 'P'):
            printP()
        if (letter == 'q' or letter == 'Q'):
            printQ()
        if (letter == 'r' or letter == 'R'):
            printR()
        if (letter == 's' or letter == 'S'):
            printS()
        if (letter == 't' or letter == 'T'):
            printT()
        if (letter == 'u' or letter == 'U'):
            printU()
        if (letter == 'v' or letter == 'V'):
            printV()
        if (letter == 'w' or letter == 'W'):
            printW()
        if (letter == 'x' or letter == 'X'):
            printX()
        if (letter == 'y' or letter == 'Y'):
            printY()
        if (letter == 'z' or letter == 'Z'):
            printZ()
        print(letter)
    isPrinting = True

def printA():
    xMotor.run_timed(time_sp=300, speed_sp=50)
    sleep(1)
    print ("A")

def printB():
    print ("B")

def printC():
    print ("C")

def printD():
    print ("D")

def printE():
    print ("D")

def printF():
    print ("D")

def printG():
    print ("D")

def printH():
    print ("D")

def printI():
    print ("D")

def printJ():
    print ("D")

def printK():
    print("D")

def printL():
    print("D")

def printM():
    print("D")

def printN():
    print("D")

def printO():
    print("D")

def printP():
    print("D")

def printQ():
    print("D")

def printR():
    print("D")

def printS():
    print("D")

def printT():
    print("D")

def printU():
    print("D")

def printV():
    print("D")

def printW():
    print("D")

def printX():
    print("D")

def printY():
    print("D")

def printZ():
    print("D")

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    if data and 'message' in data and len(data['message']) > 0:
        messages.put(data['message'])
        return jsonify({'success': True, 'message': 'Message received.'})
    else:
        return jsonify({'success': False, 'message': 'Invalid request.'})


@app.route('/')
def hello():
    return 'Hello!'


if __name__ == "__main__":
    print_messages()
    app.run(host='0.0.0.0', port=4000, threaded=True)
