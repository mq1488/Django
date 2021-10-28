from tkinter import Label, Entry, Button, W, E

import secondWindow
import thirdWindow
from presenter import *


def onStart(root):
    root.title("Window 1")
    clear(root)


    BfromBD2toBD3= Button(root, text="From BD2 to BD3", command=lambda: export_to_db3(output))
    BfromBD2toBD3.grid(columnspan=2, row=11, sticky=W,)
    BfromBD1toBD2 = Button(root, text="From BD1 to BD2", command=lambda: export_to_db2(output))
    BfromBD1toBD2.grid(columnspan=2, row=12, sticky=W)
    bWindow2 = Button(root, text="CRUD", command=lambda: secondWindow.onStart(root))
    bWindow2.grid(columnspan=2, row=13, sticky=W)
    Label(root, text="Бригада№22 Коноплін, Шибецький").grid(columnspan=3, row=0, sticky=W)
    output = Label(root)
    output.grid(column=4, row=12, sticky=W)



