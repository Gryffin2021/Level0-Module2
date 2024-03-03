import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    ran1 = random.randint(0, 9)
    ran2 = random.randint(0, 9)
    ran3 = random.randint(0, 9)
    ran4 = random.randint(0, 9)
    ran5 = random.randint(0, 9)
    ran6 = random.randint(0, 9)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title="Lottery Ticket", message=str(ran1)+str(ran2)+str(ran3)+str(ran4)+str(ran5)+str(ran6))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
