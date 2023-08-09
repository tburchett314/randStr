import string
import random
alphaChars = list(string.ascii_letters)

def randStr(length):
    randomStr = ""
    if(length <= 0):
        print("ERROR: random string length input needs to be a whole number")
    if(type(length)!=int):
        print("ERROR: random string length input needs to an integer")

    for i in range(0, length):
        randomStr+=alphaChars[random.randint(0,len(alphaChars))]
    return randomStr

def probStr(length):
    randomStr = ""
    if (length <= 0):
        print("ERROR: probablistic string length input needs to be a whole number")
    if (type(length) != int):
        print("ERROR: probablistic string length input needs to an integer")
    letter_probabilities = {
        'A': 0.084966,
        'a': 0.084966,
        'B': 0.020720,
        'b': 0.020720,
        'C': 0.045388,
        'c': 0.045388,
        'D': 0.033844,
        'd': 0.033844,
        'E': 0.111607,
        'e': 0.111607,
        'F': 0.018121,
        'f': 0.018121,
        'G': 0.024705,
        'g': 0.024705,
        'H': 0.030034,
        'h': 0.030034,
        'I': 0.075448,
        'i': 0.075448,
        'J': 0.001965,
        'j': 0.001965,
        'K': 0.011016,
        'k': 0.011016,
        'L': 0.054893,
        'l': 0.054893,
        'M': 0.030129,
        'm': 0.030129,
        'N': 0.066544,
        'n': 0.066544,
        'O': 0.071635,
        'o': 0.071635,
        'P': 0.031671,
        'p': 0.031671,
        'Q': 0.001962,
        'q': 0.001962,
        'R': 0.075809,
        'r': 0.075809,
        'S': 0.057351,
        's': 0.057351,
        'T': 0.069509,
        't': 0.069509,
        'U': 0.036308,
        'u': 0.036308,
        'V': 0.010074,
        'v': 0.010074,
        'W': 0.012899,
        'w': 0.012899,
        'X': 0.002902,
        'x': 0.002902,
        'Y': 0.017779,
        'y': 0.017779,
        'Z': 0.002722,
        'z': 0.002722
    }

    for i in range(0, length):
        letters = list(letter_probabilities.keys())
        weights = [letter_probabilities[letter] for letter in letters]
        chosen_letter = random.choices(letters, weights=weights)[0]
        randomStr+=chosen_letter
    return randomStr

