# caesar from text


def caesar_letter_change(sign, shift):
    # upper case
    if ord(sign) in range(65, 91):
        if ord(sign) < 91 - shift:
            return chr(ord(sign) + shift)
        return chr(64 + ord(sign) - 90 + shift)
    # lower case
    if ord(sign) in range(97, 123):
        if ord(sign) < 123 - shift:
            return chr(ord(sign) + shift)
        return chr(96 + ord(sign) - 122 + shift)
    return sign


def caesar(text, shift):
    try:
        shift = int(shift)
        if shift not in range(23):
            return "Wrong value for Key: 1-22"
    except ValueError:
        return "Wrong parameter: Key"
    new_text = ""
    for sign in text:
        new_text += caesar_letter_change(sign, shift)
    return new_text


user_key = input("Key: ")
with open("from.txt", "r") as f:
    file_text = f.read()
with open("to.txt", "w") as f:
    f.write(caesar(file_text, user_key))
