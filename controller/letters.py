from time import sleep
from ev3dev.ev3 import *


xMotor = LargeMotor('outC')
yMotor = LargeMotor('outB')
zMotor = MediumMotor('outA')
touchSensor = TouchSensor('in2')



whiteApproximation = 180
timeT = 1200
speed = 100
speedBackwards = -100


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

    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)

    # spacing
    spacing()

    print ("A")

def printB():
    # pen on paper
    penToPaper()

    yMotor.run_timed(time_sp=timeT/2, speed_sp=speedBackwards)
    sleep(timeT/2000)
    xMotor.run_timed(time_sp=timeT/2, speed_sp=speed)
    sleep(timeT/2000)
    yMotor.run_timed(time_sp=timeT/2, speed_sp=speed)
    sleep(timeT/2000)
    xMotor.run_timed(time_sp=timeT/2, speed_sp=speedBackwards)
    sleep(timeT / 2000)
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)
    xMotor.run_timed(time_sp=timeT/2, speed_sp=speed)
    sleep(timeT / 2000)
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
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
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

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

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT / 1000)


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
    yMotor.run_timed(time_sp=timeT*3, speed_sp=speedBackwards)
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

    # |
    yMotor.run_timed(time_sp=timeT, speed_sp=speedBackwards)
    sleep(timeT / 1000)

    # -
    xMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
    sleep(timeT / 2000)

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
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speedBackwards)
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

    # |
    yMotor.run_timed(time_sp=timeT / 2, speed_sp=speed)
    sleep(timeT / 2000)


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
    while(not touchSensor.is_pressed):
        zMotor.run_timed(time_sp=timeT/4, speed_sp=speedBackwards)
        sleep(timeT / 4000)


def penOutOfPaper():
    print()
    zMotor.run_timed(time_sp=3 * timeT, speed_sp=speed)
    sleep(timeT / 333)

def spacing():
    print("spacing")
    xMotor.run_timed(time_sp=timeT, speed_sp=speed)
    sleep(timeT/1000)

def beginningOfThePage():
    xMotor.run_timed(time_sp=timeT*14, speed_sp=speedBackwards)
    sleep((timeT*14)/1000)