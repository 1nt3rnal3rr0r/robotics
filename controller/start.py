from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import queue
from time import sleep
from ev3dev.ev3 import *

app = Flask(__name__, static_folder='react_build', static_url_path='')
messages = queue.Queue()
CORS(app)

whiteApproximation = 180
timeT = 300
speed = 100
speedBackwards = -100


xMotor = LargeMotor('outA')
yMotor = LargeMotor('outB')
zMotor = MediumMotor('outC')

touchSensor = TouchSensor('inA')



def print_messages():
    threading.Timer(1, print_messages).start()
    isPrinting = False

    print("print_message")
    if (not isPrinting):
        printA()
        isPrinting = True

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
    #pen on paper

    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT/1000)
    xMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT/1000)
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)
    yMotor.run_timed(time_sp=timeT/6, speed_sp=speed)
    sleep(timeT / 6000)
    yMotor.run_timed(time_sp=timeT / 3 + timeT, speed_sp=speedBackwards)
    sleep(timeT / 3000 + timeT)

    #spacing
    print ("A")

def printB():
    #pen on paper

    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)
    xMotor.run_timed(time_sp=timeT/2, speed_sp=speed)
    sleep(timeT/2000)
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT/1000)
    xMotor.run_timed(time_sp=timeT/2, speed_sp=speedBackwards)
    sleep(timeT/2000)

    #spacing

    #pen away from the paper
    print ("B")

def printC():
    #pen on paper

    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)
    xMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT/1000)
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # spacing

    # pen away from the paper
    print ("C")

def printD():
    #pen on paper
    yMotor.run_timed(time_sp=timeT/2, speed_sp=speed)
    sleep(timeT / 2000)
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # spacing

    # pen away from the paper

    print ("D")

def printE():

    #-
    xMotor.run_timed(time_sp=timeT / 3, speed_sp=speed)
    sleep(timeT / 3000)
    xMotor.run_timed(time_sp=timeT / 3, speed_sp=speedBackwards)
    sleep(timeT / 3000)

    #|
    yMotor.run_timed(time_sp=timeT / 3, speed_sp=speed)
    sleep(timeT / 3000)

    #-
    xMotor.run_timed(time_sp=timeT / 3, speed_sp=speed)
    sleep(timeT / 3000)
    xMotor.run_timed(time_sp=timeT / 3, speed_sp=speedBackwards)
    sleep(timeT / 3000)

    # |
    yMotor.run_timed(time_sp=timeT / 3, speed_sp=speed)
    sleep(timeT / 3000)

    #-
    xMotor.run_timed(time_sp=timeT / 3, speed_sp=speed)
    sleep(timeT / 3000)
    xMotor.run_timed(time_sp=timeT / 3, speed_sp=speedBackwards)
    sleep(timeT / 3000)
    print ("E")

def printF():
    # -
    xMotor.run_timed(time_sp=timeT / 3, speed_sp=speed)
    sleep(timeT / 3000)
    xMotor.run_timed(time_sp=timeT / 3, speed_sp=speedBackwards)
    sleep(timeT / 3000)

    # |
    yMotor.run_timed(time_sp=timeT / 3, speed_sp=speed)
    sleep(timeT / 3000)

    # -
    xMotor.run_timed(time_sp=timeT / 3, speed_sp=speed)
    sleep(timeT / 3000)
    xMotor.run_timed(time_sp=timeT / 3, speed_sp=speedBackwards)
    sleep(timeT / 3000)

    # |
    yMotor.run_timed(time_sp=timeT / 3, speed_sp=speed)
    sleep(timeT / 3000)

    print ("F")

def printG():
    #|
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    #-
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    #|
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    #-
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    #|
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    #-
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)
    print ("G")

def printH():
    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)
    # |
    yMotor.run_timed(time_sp=timeT/2, speed_sp=speedBackwards)
    sleep(timeT / 2000)
    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)
    # |
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)
    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)
    print ("H")

def printI():
    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)
    print ("I")

def printJ():
    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    print ("J")

def printK():
    # |
    yMotor.run_timed(time_sp=timeT/2, speed_sp=speed)
    sleep(timeT / 2000)

    # /
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    # /
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 1000)

    # |
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # \
    printBackSlash()

    print("K")

def printL():
    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    print("L")

def printM():
    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    # \
    printBackSlash()

    # /
    printFrontSlash()

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    print("M")

def printN():
    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    # \
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)
    print("N")

def printO():
    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)
    print("O")

def printP():
    # |
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)
    print("P")

def printQ():
    printO()
    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # \
    yMotor.run_timed(time_sp=timeT / 3, speed_sp=speed)
    xMotor.run_timed(time_sp=timeT / 3, speed_sp=speed)
    sleep(timeT / 3000)
    print("Q")

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

def printBackSlash():
    # \
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 1000)

#/
def printFrontSlash():
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 1000)


# en-US
# bg-BG
@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    if data and 'message' in data and len(data['message']) > 0 \
            and 'language' in data and data['language'] == 'en-US' or data['language'] == 'bg-BG':
        print(data['language'])
        messages.put(data['message'])
        return jsonify({'success': True, 'message': 'Message received.'})
    else:
        return jsonify({'success': False, 'message': 'Invalid request.'})


@app.route('/')
def hello():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    # print_messages()
    app.run(host='0.0.0.0', ssl_context='adhoc', port=4000, threaded=True)
