from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import queue
from time import sleep
from ev3dev.ev3 import *

app = Flask(__name__)
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
    penToPaper()

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

    #pen out of power
    penOutOfPaper()
    print ("A")

def printB():
    # pen on paper
    penToPaper()

    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)
    xMotor.run_timed(time_sp=timeT/2, speed_sp=speed)
    sleep(timeT/2000)
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT/1000)
    xMotor.run_timed(time_sp=timeT/2, speed_sp=speedBackwards)
    sleep(timeT/2000)

    # spacing

    # pen out of power
    penOutOfPaper()
    print ("B")

def printC():
    # pen on paper
    penToPaper()

    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)
    xMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT/1000)
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # spacing

    # pen out of power
    penOutOfPaper()
    print ("C")

def printD():
    # pen on paper
    penToPaper()

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

    # pen out of power
    penOutOfPaper()
    print ("D")

def printE():
    # pen on paper
    penToPaper()

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

    # spacing

    # pen out of power
    penOutOfPaper()
    print ("E")

def printF():
    # pen on paper
    penToPaper()

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

    # spacing

    # pen out of power
    penOutOfPaper()
    print ("F")

def printG():
    # pen on paper
    penToPaper()

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

    # spacing

    # pen out of power
    penOutOfPaper()
    print ("G")

def printH():
    # pen on paper
    penToPaper()

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

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print ("H")

def printI():
    # pen on paper
    penToPaper()

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print ("I")

def printJ():
    # pen on paper
    penToPaper()

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print ("J")

def printK():
    # pen on paper
    penToPaper()

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

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print("K")

def printL():
    # pen on paper
    penToPaper()

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # spacing
    spacing()

    print("L")

def printM():
    # pen on paper
    penToPaper()

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

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print("M")

def printN():
    # pen on paper
    penToPaper()

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

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print("N")

def printO():
    # pen on paper
    penToPaper()

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

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print("O")

def printP():
    # pen on paper
    penToPaper()

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
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
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
    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print("Q")

def printR():
    # pen on paper
    penToPaper()

    printP()

    yMotor.run_timed(time_sp=timeT/2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print("R")

def printS():
    # pen on paper
    penToPaper()

    #-
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    #-
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    #|
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()

    print("S")

def printT():
    # pen on paper
    penToPaper()

    # -
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT/2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print("T")

def printU():
    # pen on paper
    penToPaper()

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print("U")

def printV():
    # pen on paper
    penToPaper()

    # \
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    #/
    xMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print("V")

def printW():
    # pen on paper
    penToPaper()

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # /
    xMotor.run_timed(time_sp=timeT/2, speed_sp=speedBackwards)
    yMotor.run_timed(time_sp=timeT/2, speed_sp=speed)
    sleep(timeT / 2000)

    # \
    xMotor.run_timed(time_sp=timeT/2, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT/2, speed_sp=speed)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()

    print("W")

def printX():
    # pen on paper
    penToPaper()

    # \
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # \
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # /
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # /
    xMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 2000)

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()
    print("X")

def printY():
    # pen on paper
    penToPaper()

    # \
    printBackSlash()

    # /
    printFrontSlash()

    #/
    xMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()

    print("Y")

def printZ():
    penToPaper()

    # -
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # /
    xMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # spacing
    spacing()

    # pen out of power
    penOutOfPaper()

    print("Z")

def spacing():
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

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

def penToPaper():
    zMotor.ramp_down_sp(0)

def penOutOfPaper():
    zMotor.ramp_down_sp(30)

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
