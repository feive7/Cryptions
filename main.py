import numpy as np

#message = input("Input message: ")
message = "SLYHQEYOSQJDBOR"
#key = input("Input Key: ")
key = "bluey"
def LtoN(letter):
    return ord(letter) - 97
def NtoL(number):
    return chr(number + 97)
def caesar(string,key):
    encrypt = ""
    for i,char in enumerate(message):
        charHashed = char.lower()
        Case = (charHashed == char)
        if charHashed in "abcdefghijklmnopqrstuvwxyz":
            dec = LtoN(charHashed)
            shift = (dec + key) % 26
            charHashed = NtoL(shift)
            if not Case:
                charHashed = charHashed.upper()
        encrypt += charHashed
    return string, "caesar cipher", key, encrypt
def vignere(string,key):
    encrypt = ""
    keyHashed = []
    for i in key:
        keyHashed.append(LtoN(i))
    for i,char in enumerate(message):
        charHashed = char.lower()
        Case = (charHashed == char)
        if charHashed in "abcdefghijklmnopqrstuvwxyz":
            dec = LtoN(charHashed)
            shift = (dec + keyHashed[i % len(keyHashed)]) % 26
            charHashed = NtoL(shift)
            if not Case:
                charHashed = charHashed.upper()
        encrypt += charHashed
    return string, "vignere cipher", key, encrypt
def rail_fence(string,key):
    grid = [["-" for x in range(len(string))] for y in range(key)]
    y_pos = 0
    direction = 1
    for i,char in enumerate(string):
        grid[y_pos][i] = char
        y_pos += direction
        if y_pos == 1 or y_pos == key - 1:
            direction = - direction
    return grid
def print_result(params):
    print("Input: " + str(params[0]))
    print("Method: " + str(params[1]))
    print("Key: " + str(params[2]))
    print("Output: " + str(params[3]))
print_result(vignere(message,key))
#print(rail_fence(message,2))

RAEDSDNUOSISHKT
