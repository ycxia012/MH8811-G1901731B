from H1_module import genPassword

while True:
    n = input("Password length:")

    try:
        n = int(n)
        if n >= 4:
            password = genPassword(n)
            print("Password:",password)
            break
        else:
            print("The number you entered should be larger than or equal to 4.")
    except Exception:
        pass