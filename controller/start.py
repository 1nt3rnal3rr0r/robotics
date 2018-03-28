from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import queue
from time import sleep
from ev3dev.ev3 import *
from message import Message

app = Flask(__name__, static_folder='react_build', static_url_path='')
messages = queue.Queue()
CORS(app)

whiteApproximation = 180
timeT = 1200
speed = 100
speedBackwards = -100

lettersPrinted = 1
lettersPerLine = 6

xMotor = LargeMotor('outC')
yMotor = LargeMotor('outB')
zMotor = MediumMotor('outA')

touchSensor = TouchSensor('inA')

atBeginning = False

def print_messages():
    global atBeginning

   #go at the beginning of the page
    beginningOfThePage()

    print("print_message")

    parseText("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# access text language with text.get_language()
# access text content with text.get_content() because they are objects now
def parseText(text):
    global lettersPrinted


    for letter in text:
        if (lettersPrinted % lettersPerLine == 0):
            newLine()
        else:
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
        lettersPrinted += 1
        print(letter)

def beginningOfThePage():
    xMotor.run_timed(time_sp=timeT*14, speed_sp=speedBackwards)
    sleep((timeT*14)/1000)


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
    yMotor.run_timed(time_sp=timeT/4, speed_sp=speed)
    sleep(timeT / 4000)
    yMotor.run_timed(time_sp=timeT / 4 + timeT + timeT / 4, speed_sp=speedBackwards)
    sleep(timeT / 4000 + timeT/1000 + timeT / 4000)

    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()

    print ("A")

def printB():
    # pen on paper
    penToPaper()

    yMotor.run_timed(time_sp=timeT*2, speed_sp=speed)
    sleep(timeT/500)
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT/1000)
    xMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)
    xMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # pen out of power
    penOutOfPaper()

    # spacing
    spacing()

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


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
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
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
    print ("D")

def printE():
    # pen on paper
    penToPaper()

    #-
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    #|
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    #-
    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
    print ("E")

def printF():
    # pen on paper
    penToPaper()

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
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
    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    #|
    yMotor.run_timed(time_sp=timeT , speed_sp=speedBackwards)
    sleep(timeT / 1000)

    #-
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # pen out of power
    penOutOfPaper()

    # spacing
    spacing()


    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    print ("G")

def printH():
    # pen on paper
    penToPaper()

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)
    # |
    yMotor.run_timed(time_sp=timeT/2, speed_sp=speed)
    sleep(timeT / 2000)
    # -
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)
    # |
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)
    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
    print ("H")

def printI():
    # pen on paper
    penToPaper()

    # -
    print("-")
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # pen out of power
    print("pen out")
    penOutOfPaper()

    # spacing
    print("spacing")
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT/1000)

    # pen in of power
    print("pen out")
    penOutOfPaper()

    print ("I")

def newLine():
    # pen out of power
    print("pen out")
    zMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    xMotor.run_timed(time_sp=timeT*14, speed_sp=speedBackwards)
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000*14)

def printDot():
    # pen on paper
  #  penToPaper()

    # .
    print(".")
    yMotor.run_timed(time_sp=timeT/12, speed_sp=speed)
    sleep(timeT / 12000)

    # pen out of power
    print("pen out")
    penOutOfPaper()

    # spacing
    print("spacing")
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)

    # pen in of power
    print("pen in")
    penToPaper()

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


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
    print ("J")

def printK():
    # pen on paper
    penToPaper()

    # |
    yMotor.run_timed(time_sp=timeT/2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # /
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

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
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # /
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 1000)


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
    print("K")

def printL():
    # pen on paper
    penToPaper()

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)



    #pen out of power
    penOutOfPaper()

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

    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
    print("M")

def printN():
    # pen on paper
    penToPaper()

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # \
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
    print("N")

def printO():
    # pen on paper
    penToPaper()

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
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
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
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

    # |
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

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)



    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)


    #pen out of power
    penOutOfPaper()

    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # spacing
    spacing()
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
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
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


    #pen out of power
    penOutOfPaper()

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # spacing
    spacing()

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
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)


    #pen out of power
    penOutOfPaper()

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # spacing
    spacing()
    print("T")

def printU():
    # pen on paper
    penToPaper()

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
    print("U")

def printV():
    # pen on paper
    penToPaper()

    # \
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    #/
    xMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
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


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
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


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
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


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()

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


    #pen out of power
    penOutOfPaper()

    # spacing
    spacing()
    print("Z")


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
    print()
    zMotor.run_timed(time_sp=4*timeT, speed_sp=speedBackwards)
    sleep(timeT/250)

def penOutOfPaper():
    print()
    zMotor.run_timed(time_sp=4 * timeT, speed_sp=speed)
    sleep(timeT / 250)

def spacing():
    print()
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)

# en-US
# bg-BG
@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    if data and 'message' in data and len(data['message']) > 0 \
            and 'language' in data and data['language'] == 'en-US' or data['language'] == 'bg-BG':
        messages.put(Message(data['language'], data['message']))
        return jsonify({'success': True, 'message': 'Message received.'})
    else:
        return jsonify({'success': False, 'message': 'Invalid request.'})


@app.route('/')
def hello():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    # print_messages()
    app.run(host='0.0.0.0', ssl_context='adhoc', port=4000, threaded=False)
