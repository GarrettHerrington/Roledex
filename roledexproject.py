#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:07:19 2024

@author: ariciapundt
"""
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Contacts Book')
root.iconbitmap('iCloud Drive: Desktop: CSC 411')
root.geometry("600x400")

# database connection
connection = sqlite3.connect('address_book.db')

# create cursor
cursor = connection.cursor()


# create table


cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (
              first_name text,
              last_name text,
              phone number text,
              birthday text)
               
    """)


# create submit function
def submit():
    # database connection
    connection = sqlite3.connect('address_book.db')

    # create cursor
    cursor = connection.cursor()

    # insert into table
    cursor.execute("INSERT INTO contacts VALUES (:first_name, :last_name, :phone_number, :birth_day)",
                   {
                       'first_name': first_name.get(),
                       'last_name': last_name.get(),
                       'phone_number': phone_number.get(),
                       'birth_day': birth_day.get()
                   })

    connection.commit()
    connection.close()

    # clear text boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    phone_number.delete(0, END)
    birth_day.delete(0, END)

 # create query function


def query():

    connection = sqlite3.connect('address_book.db')

    cursor = connection.cursor()

    cursor.execute("SELECT *, oid FROM contacts")
    records = cursor.fetchall()
    "print(records)"
    cols = ('First Name', 'Last Name', 'Phone Number', 'Birthday')
    tree = ttk.Treeview(root, columns=cols, show='headings', height=100)
    tree.grid(padx=10, pady=10)

    for col in cols:  # Set treeview attributes
        tree.heading(col, text=col)
        tree.column(col, width=140, anchor='center')

    for items in records:  # Insert values inside the treeview
        tree.insert('', 'end', values=items)

    connection.commit()
    connection.close()
    return


# creating text boxes
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20)

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1, padx=20)

phone_number = Entry(root, width=30)
phone_number.grid(row=2, column=1, padx=20)

birth_day = Entry(root, width=30)
birth_day.grid(row=3, column=1, padx=20)

# create text box labels

first_name_label = Label(root, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0)

phone_number_label = Label(root, text="Phone Number")
phone_number_label.grid(row=2, column=0)

birth_day_label = Label(root, text="Birthday")
birth_day_label.grid(row=3, column=0)

# create submit button

submit_button = Button(root, text="Enter Contact", command=submit)
submit_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create query button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


# commit changes
connection.commit()

# close connection
connection.close()
root.mainloop()
