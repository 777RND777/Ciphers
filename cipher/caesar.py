# caesar from text


def caesar_cipher(sign, shift):
    # upper case
    if ord(sign) in range(65, 91):
        if ord(sign) + shift < 91:
            return chr(ord(sign) + shift)
        return chr(64 + ord(sign) - 90 + shift)
    # lower case
    if ord(sign) in range(97, 123):
        if ord(sign) + shift < 123:
            return chr(ord(sign) + shift)
        return chr(96 + ord(sign) - 122 + shift)
    return sign


def caesar_decipher(sign, shift):
    # upper case
    if ord(sign) in range(65, 91):
        if ord(sign) - shift >= 65:
            return chr(ord(sign) - shift)
        return chr(ord(sign) + 26 - shift)
    # lower case
    if ord(sign) in range(97, 123):
        if ord(sign) - shift >= 97:
            return chr(ord(sign) - shift)
        return chr(ord(sign) + 26 - shift)
    return sign


def caesar_get_error(shift):
    try:
        shift = int(shift)
        if shift not in range(1, 26):
            return "Wrong value for Key: 1-25 (positive & negative)", shift
    except ValueError:
        return "Wrong parameter: Key", shift
    return "", shift


def caesar_main(text, shift, mode):
    new_text = ""
    if mode == "Cipher":
        for sign in text:
            new_text += caesar_cipher(sign, shift)
    else:
        for sign in text:
            new_text += caesar_decipher(sign, shift)
    return new_text


# independent terminal part
# if __name__ == "__main__":
#     mode = input("Mode (Cipher/Decipher): ")
#     user_key = input("Key: ")
#     with open("from.txt", "r") as f:
#         file_text = f.read()
#     with open("to.txt", "w") as f:
#         error, user_key = caesar_get_error(user_key)
#         if len(error) == 0:
#             f.write(caesar_main(file_text, user_key, mode))
#         else:
#             print(error)
