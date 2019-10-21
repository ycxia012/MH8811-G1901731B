from random import randint, choice

characters={
    "LowerLetter":"abcdefghijklmnopqrstuvwxyz",
    "UpperLetter":"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Numbers":"1234567890",
    "Symbols":"`-=[]\;',./~!@#$%^&*()_+{}|:\"<>?"}

def genPassword(n):
    """
    Function that used to generats a strong password of length n(n>=4).
    """
    chars = ""
    catagory = list(characters.keys())
    # list with elements that each character is chose from.
    catagory_list = []
    for _ in range(n-4):
        catagory_list.append(choice(catagory))
    catagory_list += catagory
    # choose char from each desired catagory
    for cata in catagory_list:
        chars += choice(characters[cata])

    return chars


if __name__=="__main__":
    print(genPassword(12))