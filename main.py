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

