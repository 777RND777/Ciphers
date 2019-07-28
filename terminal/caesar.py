# caesar from text


def letter_change(sign, step):
    # upper case
    if ord(sign) in range(65, 91):
        if ord(sign) < 91 - step:
            return chr(ord(sign) + step)
        return chr(64 + ord(sign) - 90 + step)
    # lower case
    if ord(sign) in range(97, 123):
        if ord(sign) < 123 - step:
            return chr(ord(sign) + step)
        return chr(96 + ord(sign) - 122 + step)
    return sign


def caesar(text, step):
    try:
        step = int(step)
        if step not in range(23):
            return "Wrong value for Step: 1-22"
    except ValueError:
        return "Wrong parameter: Step"
    new_text = ""
    for sign in text:
        new_text += letter_change(sign, step)
    return new_text


user_step = input("Step: ")
with open("from.txt", "r") as f:
    file_text = f.read()
with open("to.txt", "w") as f:
    f.write(caesar(file_text, user_step))
