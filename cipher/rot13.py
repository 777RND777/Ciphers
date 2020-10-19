# rot13 from text


def rot13_cipher(sign):
    # upper case
    if ord(sign) in range(65, 78):
        return chr(ord(sign) + 13)
    if ord(sign) in range(78, 91):
        return chr(ord(sign) - 13)
    # lower case
    if ord(sign) in range(97, 110):
        return chr(ord(sign) + 13)
    if ord(sign) in range(110, 123):
        return chr(ord(sign) - 13)
    return sign


def rot13_main(text):
    new_text = ""
    for sign in text:
        new_text += rot13_cipher(sign)
    return new_text


# independent terminal part
# if __name__ == "__main__":
    # with open("from.txt", "r") as f:
    #     file_text = f.read()
    # with open("to.txt", "w") as f:
    #     f.write(rot13_main(file_text))
