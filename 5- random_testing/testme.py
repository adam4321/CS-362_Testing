# Author:       Adam Wright
# Date:         2-4-2020
# Description:  Python re-implementation of testme.c file


import random


def inputChar():
    return ' '


def inputString():
    return ""


def testme():
    tcCount = 0
    s = ""
    c = ''
    state = 0

    while True:
        tcCount+=1
        test_char = inputChar()
        test_string = inputString()
        print("Iteration " + tcCount + "c = " + test_char + ", " + "s = " + test_string + ", " + "state = " + state)

        if c == '[' and state == 0:
            state = 1
        if c == '(' and state == 1:
            state = 2
        if c == '{' and state == 2:
            state = 3
        if c == ' ' and state == 3:
            state = 4
        if c == 'a' and state == 4:
            state = 5
        if c == 'x' and state == 5:
            state = 6
        if c == '}' and state == 6:
            state = 7
        if c == ')' and state == 7:
            state = 8
        if c == ']' and state == 8:
            state = 9
        if s.index(0) == 'r' and s.index(1) == 'e' and s.index(2) == 's' and s.index(3) == 'e' and s.index(4) == 't' and state == 9:
            print("error ")
            exit(200)


def main():
    random.seed(None)
    testme()
