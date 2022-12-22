from tkinter import *
from getCharInfo import *
from charDao import read

class home:
    def __init__(self):
        window = Tk()
        window.title("MyFavChar")
        window.geometry("300x300")
        window.columnconfigure(0, weight=1)

        title = Label(window, text="MyFavChar", font="Helvetica, 14")
        title.grid(column=0, row=0, pady=10)

        listChar = Listbox(window, font="Helvetic, 10", width=30)
        listChar.grid(column=0, row=1)

        read(listChar)

        charName = Entry(window)
        charName.grid(column=0, row=2, pady=5)
        charGrade = Entry(window)
        charGrade.grid(column=0, row=3)
        charDesc = Entry(window)
        charDesc.grid(column=0, row=4, pady=5)
        addChar = Button(window, text="Add", font="Helvetica, 10", command=lambda: addchar(listChar, charName, charGrade, charDesc))
        addChar.grid(column=0, row=5, pady=5)

        charId = Entry(window)
        charId.grid(column=0, row=6)

        updateChar = Button(window, text="Update", font="Helvetica, 10", command=lambda: updatechar(listChar, charId, charName, charGrade, charDesc))
        updateChar.grid(column=0, row=7, pady=10)

        deleteChar = Button(window, text="Delete", font="Helvetica, 10", command=lambda: deletechar(listChar, charId))
        deleteChar.grid(column=0, row=8)

        window.mainloop()

home()
