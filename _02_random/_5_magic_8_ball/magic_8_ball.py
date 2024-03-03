import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring(title="The 8-ball beckons...", prompt="Do you have a (yes or no) question for the great Magic 8-ball?")
    # Make a variable and initialize it to a random number between 0 and 3
    rsvp = random.randint(0, 3)
    # If the random number is 0
    if rsvp == 0:
        # tell the user "Yes"
        messagebox.showinfo(None, "Yes")
    # If the random number is 1
    if rsvp == 1:
        # tell the user "No"
        messagebox.showinfo(None, "No")
    # If the random number is 2
    if rsvp == 2:
        # tell the user "Maybe you should ask Google?"
        messagebox.showinfo(None, "Maybe you should ask Google?")
    # If the random number is 3
    if rsvp == 3:
        # write your own answer
        messagebox.showinfo(None, "I don't think you want to know...")