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

sys.exit()

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


addX("committee")
addX("book")

