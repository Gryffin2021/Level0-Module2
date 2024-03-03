import random
import sys
from tkinter import messagebox, Tk


def crack_the_safe():
    for i in range(999999):
        code = i
        try_code(code)
    # TODO: Your mission: Use the try_code method to crack the safe
    #  by trying all possible combinations


# ======================= DO NOT EDIT THE CODE BELOW =========================

wekncrzpasfdkjhcfjse = random.randint(0, 999999)


def try_code(guess):
    print("trying " + str(guess))

    secret_code = 999999 - wekncrzpasfdkjhcfjse

    if guess == secret_code:
        messagebox.showinfo(None, "Congratulations! You cracked the safe with " + str(guess))
        sys.exit(0)
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    crack_the_safe()
