# vigenère from text


def vigenere_cipher(sign, key):
    # upper case
    if ord(sign) in range(65, 91):
        step = ord(key.upper()) - 65
        if ord(sign) + step < 91:
            return chr(ord(sign) + step), True
        return chr(64 + ord(sign) - 90 + step), True
    # lower case
    if ord(sign) in range(97, 123):
        step = ord(key.lower()) - 97
        if ord(sign) + step < 123:
            return chr(ord(sign) + step), True
        return chr(96 + ord(sign) - 122 + step), True
    return sign, False


def vigenere_decipher(sign, key):
    # upper case
    if ord(sign) in range(65, 91):
        step = ord(key.upper()) - 65
        if ord(sign) - step >= 65:
            return chr(ord(sign) - step), True
        return chr(ord(sign) + 26 - step), True
    # lower case
    if ord(sign) in range(97, 123):
        step = ord(key.lower()) - 97
        if ord(sign) - step >= 97:
            return chr(ord(sign) - step), True
        return chr(ord(sign) + 26 - step), True
    return sign, False


def vigenere_get_error(keyword):
    if not keyword.isalpha():
        return "Wrong parameter: Keyword"
    return ""


def vigenere_main(text, keyword):
    new_text = ""
    while len(keyword) < len(text):
        keyword += keyword
    keyword = keyword[:len(text)]
    index = 0
    for i in range(len(text)):
        sign, changed = vigenere_cipher(text[i], keyword[index])
        new_text += sign
        if changed:
            index += 1
    return new_text


user_keyword = input("Keyword: ")
with open("from.txt", "r") as f:
    file_text = f.read()
with open("to.txt", "w") as f:
    error = vigenere_get_error(user_keyword)
    if len(error) == 0:
        f.write(vigenere_main(file_text, user_keyword))
    else:
        print(error)
