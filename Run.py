from tkinter import *

window = Tk()
window.title("Name Hash Magic")


def hash(key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions


def modHash(number):
    while number >= 255:
        number -= 255
    #print(number)
    return number


def hexNum(number):
    hexedNum = hex(number)
    while len(hexedNum) < 4:
        hexedNum = hexedNum + "0"
    return hexedNum[2:]


def colorFromName(nameOne, nameTwo="", nameThree=""):

    #Hash Names
    firstName = hash(nameOne)
    secondName = hash(nameTwo)
    thirdName = hash(nameThree)

    #Bring value between 0-255
    firstName = modHash(firstName)
    secondName = modHash(secondName)
    thirdName = modHash(thirdName)

    #Return two character hex code
    firstName = hexNum(firstName)
    secondName = hexNum(secondName)
    thirdName = hexNum(thirdName)

    lst = [firstName, secondName, thirdName]
    hexCode = "#" + "".join(lst)
    return hexCode


def click():
    global bannerImage

    firstName = firstNameEntry.get()
    secondName = secondNameEntry.get()
    thirdName = thirdNameEntry.get()
    hexCode = colorFromName(firstName, secondName, thirdName)
    bannerImage.config(bg = hexCode)
    print('DEBUG:\nHexcode = ' + hexCode)

#hexCode = colorFromName("M", "W", "Bauer")

#Images/General GUI
banner = PhotoImage(file="banner.png")
bannerImage = Label(window, image=banner, bg='black')
bannerImage.grid(row=0, column=0, sticky=W)
bannerImage.config(bg='white')

firstName = Label(window, text='First Name:', bg="black", fg="white", font="none 12 bold")
firstName.place(x = 40, y = 250, height = 25, width = 90, anchor = W)

secondName = Label(window, text='Second Name:', bg="black", fg="white", font="none 12 bold")
secondName.place(x = 240, y = 250, height = 25, width = 120, anchor = W)

thirdName = Label(window, text='Third Name:', bg="black", fg="white", font="none 12 bold")
thirdName.place(x = 450, y = 250, height = 25, width = 100, anchor = W)

#TextEntryBoxes
firstNameEntry = Entry(window, width=20, bg='white')
firstNameEntry.place(x = 50, y = 300, height = 25, width = 70, anchor = W)

secondNameEntry = Entry(window, width=20, bg='white')
secondNameEntry.place(x = 260, y = 300, height = 25, width = 70, anchor = W)

thirdNameEntry = Entry(window, width=20, bg='white')
thirdNameEntry.place(x = 460, y = 300, height = 25, width = 70, anchor = W)

#SubmitButton
Submit = Button(window, text="Go!", width=6, command=click)
Submit.place(x = 260, y = 450, height = 25, width = 70, anchor = W)

#MainLoop
window.mainloop()