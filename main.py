# !/usr/bin/python
import sys

print(sys.argv)
if len(sys.argv) < 4:
    print('usage: ARGS="encode/decode ciphertext/plaintext keytext')
    sys.exit()

# whatToDo = open(sys.argv[1], "r")
whatToDo = sys.argv[1]
text = sys.argv[2]

keyText = sys.argv[3]
key = [list(keyText[i : i + 5]) for i in range(0, len(keyText), 5)]


# print(key)

# print(whatToDo)
# print(text)
# print(keyText)


def addX(plaintext):
    xLength = 0
    for i in range(0, len(plaintext), 2):
        i += xLength
        if len(plaintext) % 2 + xLength == 1 and i == len(plaintext) - 1:
            plaintext += "x"  # adding 'x' to the end of the string
            break

        char1 = plaintext[i]
        char2 = plaintext[i + 1]
        if char1 == char2:
            plaintext = (
                plaintext[: i + 1] + "x" + plaintext[i + 1 :]
            )  # adding x in between double letters
            xLength += 1

    print(plaintext)


def findInKey(char):
    for row in range(len(key)):
        for letter in range(len(key[row])):
            if char == key[row][letter]:
                return [row, letter]
    # TODO: CHECK IF IT IS EVEN IN KEY


def verticalEncode(letterPair):
    char1Location = findInKey(letterPair[0])
    char2Location = findInKey(letterPair[1])
    codedChar1Loc = [char1Location[0], (char1Location[1] + 1) % 5]
    codedChar2Loc = [char2Location[0], (char2Location[1] + 1) % 5]
    return (
        key[codedChar1Loc[0]][codedChar1Loc[1]]
        + key[codedChar2Loc[0]][codedChar2Loc[1]]
    )


print(verticalEncode("af"))


def horizontalEncode(letterPair):
    char1Location = findInKey(letterPair[0])
    char2Location = findInKey(letterPair[1])
    codedChar1Loc = [(char1Location[0] + 1) % 5, char1Location[1]]
    codedChar2Loc = [(char2Location[0] + 1) % 5, char2Location[1]]
    return (
        key[codedChar1Loc[0]][codedChar1Loc[1]]
        + key[codedChar2Loc[0]][codedChar2Loc[1]]
    )


print(horizontalEncode("ac"))

# def regularEncode(letterPair):


# addX("committee")
# addX("book")

