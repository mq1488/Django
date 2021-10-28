from tkinter import Label, Button, W,E, Entry, Checkbutton, BooleanVar

import firstWindow
from presenter import *
from PIL import Image, ImageTk


def onStart(root):
    root.title("Window 2")
    clear(root)
    name = Label(root, text="Name")
    price = Label(root, text="Price")
    in_stock = Label(root, text="In stock")
    name_enter = Entry(root, width=15)
    price_enter = Entry(root, width=15)
    cb = BooleanVar()
    in_stock_enter = Checkbutton(root, width=15, variable=cb)
    bWindow1 = Button(root, text="Window 1", command=lambda: firstWindow.onStart(root))
    bCreate = Button(root, text="Create", command=lambda: insert_table_mysql(name_enter, price_enter, cb))  # insert
    bRead = Button(root, text="Read", command=lambda: select_table_mysql(output))  # select
    bUpdate = Button(root, text="Update", command=lambda: update_table_mysql(name_enter, price_enter, cb))  # update
    bDelete = Button(root, text="Delete", command=lambda: delete_table_mysql(name_enter))  # delete
    bCreate.grid(row=12, sticky=W)
    bRead.grid(row=13, sticky=W)
    bUpdate.grid(row=14, sticky=W)
    bDelete.grid(row=15, sticky=W)
    bWindow1.grid(row=16, sticky=W)
    name.grid(column=1, row=4,sticky=E )
    price.grid(column=1, row=5, )
    in_stock.grid(column=1, row=6, )
    name_enter.grid(column=2, row=4, )
    price_enter.grid(column=2, row=5, )
    in_stock_enter.grid(column=2, row=6, )
    output = Label(root)
    output.grid(column=0, row=35, )
