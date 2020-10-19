# atbash from text


def atbash_cipher(sign):
    # upper case
    if ord(sign) in range(65, 91):
        return chr((65 + 26) - ord(sign) + 64)
    # lower case
    if ord(sign) in range(97, 123):
        return chr((97 + 26) - ord(sign) + 96)
    return sign


def atbash_main(text):
    new_text = ""
    for sign in text:
        new_text += atbash_cipher(sign)
    return new_text


# independent terminal part
# if __name__ == "__main__":
#     with open("from.txt", "r") as f:
#         file_text = f.read()
#     with open("to.txt", "w") as f:
#         f.write(atbash_main(file_text))
