# Author:       Adam Wright
# Date:         2-4-2020
# Description:  Python re-implementation of testme.c file


import string
import random


def inputChar():
    # Generate and return a random character from a-z A-Z [{( )}]
    test_char = string.ascii_letters
    test_char = test_char + "[{( )}]"
    return random.choice(test_char)


def inputString():
    # Generate and return a 5 character string from a subset of a-z
    char_set = "restabcdfghijklm"
    test_str = ''.join(random.choice(char_set) for i in range(5))
    return test_str


def testme():
    # Test character and test string
    s = ""
    c = ''
    tcCount = 0
    state = 0

    while True:
        tcCount+=1
        c = inputChar()
        s = inputString()
        print("Iteration " + str(tcCount) + " c = " + str(c) + ", " + "s = " + str(s) + ", " + "state = " + str(state))

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
        if s[0] == 'r' and s[1] == 'e' and s[2] == 's' and s[3] == 'e' and s[4] == 't' and state == 9:
            print("error ")
            exit(200)


def main():
    random.seed(None)
    testme()


if __name__ == '__main__':
    main()
