# vigenère from text


def vigenere_letter_change(sign, key):
    # upper case
    if ord(sign) in range(65, 91):
        step = ord(key.upper()) - 65
        if ord(sign) < 91 - step:
            return chr(ord(sign) + step), True
        return chr(64 + ord(sign) - 90 + step), True
    # lower case
    if ord(sign) in range(97, 123):
        step = ord(key.lower()) - 97
        if ord(sign) < 123 - step:
            return chr(ord(sign) + step), True
        return chr(96 + ord(sign) - 122 + step), True
    return sign, False


def vigenere(text, keyword):
    new_text = ""
    while len(keyword) < len(text):
        keyword += keyword
    keyword = keyword[:len(text)]
    index = 0
    for i in range(len(text)):
        sign, changed = vigenere_letter_change(text[i], keyword[index])
        new_text += sign
        if changed:
            index += 1
    return new_text


user_keyword = input("Keyword: ")
with open("from.txt", "r") as f:
    file_text = f.read()
with open("to.txt", "w") as f:
    f.write(vigenere(file_text, user_keyword))
