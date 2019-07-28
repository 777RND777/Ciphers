# vigenère from text


def letter_change(sign):
    # upper case
    if ord(sign) in range(65, 91):
        step = ord(sign) - 65
        if ord(sign) < 91 - step:
            return chr(ord(sign) + step)
        return chr(64 + ord(sign) - 90 + step)
    # lower case
    if ord(sign) in range(97, 123):
        step = ord(sign) - 97
        if ord(sign) < 123 - step:
            return chr(ord(sign) + step)
        return chr(96 + ord(sign) - 122 + step)
    return sign


def caesar(text):
    new_text = ""
    for sign in text:
        new_text += letter_change(sign)
    return new_text


with open("from.txt", "r") as f:
    file_text = f.read()
with open("to.txt", "w") as f:
    f.write(caesar(file_text))
