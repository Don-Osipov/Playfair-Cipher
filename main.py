# !/usr/bin/python
import sys

print(sys.argv)
if len(sys.argv) < 4:
    print('usage: ARGS="encode/decode plaintext/ciphertext keytext')
    sys.exit()

# whatToDo = open(sys.argv[1], "r")
whatToDo = sys.argv[1]
text = sys.argv[2].upper()
keyText = sys.argv[3].upper()

keyList = [
    list(keyText[i : i + 5]) for i in range(0, len(keyText), 5)
]  # nested array key - used to get letter from row/column
key = {}  # dictionary key
for i, letter in enumerate(keyText):
    key[letter] = [
        i // 5,
        i % 5,
    ]  # letter: [row, column] - used to get row/column of a letter quickly


def preProcessing(plaintext):
    replaceDict = {"J": "I", " ": "", ",": "", ".": "", "!": "", "?": ""}
    for before, after in replaceDict.items():
        plaintext = plaintext.replace(before, after)
    return plaintext


def addX(plaintext):
    processedMessage = ""
    while len(plaintext) > 0:
        double = plaintext[:2]
        if len(double) < 2:  # if last letter in text does not have a double
            processedMessage += double[0] + "X"
            plaintext = plaintext[1:]
        elif double[0] == double[1]:
            processedMessage += double[0] + "X"
            plaintext = plaintext[1:]
        elif double[0] != double[1]:
            processedMessage += double[0] + double[1]
            plaintext = plaintext[2:]
    return processedMessage


def findInKey(char):
    if char in key:
        return key[char]
    return []

    # for row in range(len(key)):
    #     for letter in range(len(key[row])):
    #         if char == key[row][letter]:
    #             return [row, letter]
    # return []  # if char not in key


def verticalEncode(letterPair, direction):
    char1Location = findInKey(letterPair[0])
    char2Location = findInKey(letterPair[1])

    if not char1Location:
        char1Location = findInKey("X")
    if not char2Location:
        char2Location = findInKey("X")

    if direction == "right":  # for ENCODING
        codedChar1Loc = [char1Location[0], (char1Location[1] + 1) % 5]
        codedChar2Loc = [char2Location[0], (char2Location[1] + 1) % 5]
    elif direction == "left":  # for DECODING
        codedChar1Loc = [char1Location[0], (char1Location[1] - 1) % 5]
        codedChar2Loc = [char2Location[0], (char2Location[1] - 1) % 5]

    return (
        keyList[codedChar1Loc[0]][codedChar1Loc[1]]
        + keyList[codedChar2Loc[0]][codedChar2Loc[1]]
    )


# print(verticalEncode("af"))


def horizontalEncode(letterPair, direction):
    char1Location = findInKey(letterPair[0])
    char2Location = findInKey(letterPair[1])

    if not char1Location:
        char1Location = findInKey("X")
    if not char2Location:
        char2Location = findInKey("X")

    if direction == "down":  # for ENCODING
        codedChar1Loc = [(char1Location[0] + 1) % 5, char1Location[1]]
        codedChar2Loc = [(char2Location[0] + 1) % 5, char2Location[1]]
    elif direction == "up":  # for DECODING
        codedChar1Loc = [(char1Location[0] - 1) % 5, char1Location[1]]
        codedChar2Loc = [(char2Location[0] - 1) % 5, char2Location[1]]

    return (
        keyList[codedChar1Loc[0]][codedChar1Loc[1]]
        + keyList[codedChar2Loc[0]][codedChar2Loc[1]]
    )


# print(horizontalEncode("ac"))


def regularEncode(letterPair):
    char1Location = findInKey(letterPair[0])
    char2Location = findInKey(letterPair[1])

    if not char1Location:
        char1Location = findInKey("X")
    if not char2Location:
        char2Location = findInKey("X")

    codedChar1Loc = [char1Location[0], char2Location[1]]
    codedChar2Loc = [char2Location[0], char1Location[1]]

    return (
        keyList[codedChar1Loc[0]][codedChar1Loc[1]]
        + keyList[codedChar2Loc[0]][codedChar2Loc[1]]
    )


# print(regularEncode("az"))

# addX("committee")
# addX("book")


def encode(letterPair, encodeOrDecode="encode"):
    char1Location = findInKey(letterPair[0])
    char2Location = findInKey(letterPair[1])

    verticalDirection = "right" if encodeOrDecode == "encode" else "left"
    horizontalDirection = "down" if encodeOrDecode == "encode" else "up"

    if char1Location and char2Location:

        if (
            char1Location[0] != char2Location[0]
            and char1Location[1] == char2Location[1]
        ):
            return verticalEncode(letterPair, verticalDirection)

        if (
            char1Location[0] == char2Location[0]
            and char1Location[1] != char2Location[1]
        ):
            return horizontalEncode(letterPair, horizontalDirection)

        if (
            char1Location[0] != char2Location[0]
            and char1Location[1] != char2Location[1]
        ):
            return regularEncode(letterPair)


def encodeMessage(plaintext):
    encodedMessage = ""
    plaintext = preProcessing(plaintext)
    plaintext = addX(plaintext)

    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i + 1]

        encodedMessage += encode(char1 + char2)

    return encodedMessage


def decodeMessage(encodedMessage):
    decodedMessage = ""

    for i in range(0, len(encodedMessage), 2):
        char1 = encodedMessage[i]
        char2 = encodedMessage[i + 1]

        decodedMessage += encode(char1 + char2, "decode")

    return decodedMessage


if whatToDo == "encode":
    print(encodeMessage(text))
elif whatToDo == "decode":
    print(decodeMessage(text))
else:
    print(encodeMessage(text))
