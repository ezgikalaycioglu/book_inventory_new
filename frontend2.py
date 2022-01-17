"""
A program that stores this book information:
Title, Author
Year, rating

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""
#pyinstaller --onefile --windowed  frontend.py

from tkinter import *

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext




import backend
#functions---------------------------------------------------------------------------------------------------------------------------------
def view_command():
    #list1.delete(0,END)
    tv.delete(*tv.get_children())
    for row in backend.view():
        #list1.insert(END,row)
        tv.insert('','end',text='',values=row)


def search_command():
    #list1.delete(0,END)
    tv.delete(*tv.get_children())
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(),rating_text.get(), publishing_text.get(), noreading_text.get(), closet_text.get(), shelf_text.get()):
        #list1.insert(END,row)
        tv.insert('','end',text='',values=row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(),rating_text.get(), publishing_text.get(), noreading_text.get(), closet_text.get(), shelf_text.get())
    #list1.delete(0,END)
    tv.delete(*tv.get_children())
    #list1.insert(END,(title_text.get(), author_text.get(), year_text.get(),rating_text.get(),publishing_text.get(), noreading_text.get(), closet_text.get(), shelf_text.get()))
    tv.insert('','end',text='',values=(title_text.get(), author_text.get(), year_text.get(),rating_text.get(), publishing_text.get(), noreading_text.get(), closet_text.get(), shelf_text.get()))
    view_command()

"""def get_selected_row(event):
    try:
        global selected_tuple
        index=tv.selection()[0]
        selected_tuple=tv.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
        e6.delete(0,END)
        e6.insert(END,selected_tuple[6])
        e7.delete(0,END)
        e7.insert(END,selected_tuple[7])
        e8.delete(0,END)
        e8.insert(END,selected_tuple[8])
    except IndexError:
        pass"""

def get_selected_row(event):
    try:
        global selected_tuple
        curItem = tv.focus()
        selected_tuple=tv.item(curItem)['values']
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
        e6.delete(0,END)
        e6.insert(END,selected_tuple[6])
        e7.delete(0,END)
        e7.insert(END,selected_tuple[7])
        e8.delete(0,END)
        e8.insert(END,selected_tuple[8])
    except IndexError:
        pass

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(),rating_text.get(),publishing_text.get(), noreading_text.get(), closet_text.get(), shelf_text.get())
    view_command()

def clear_command():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)

#GUI-------------------------------------------------------------------------------------------------------------------------------------------------
window=tk.Tk()
window.wm_title("Book Inventory")

#Entry Frame----------------------------------------------------------------------------------------------------------------------------------------
entry_frame = tk.LabelFrame(window, text="Entries")
entry_frame.grid(row=0, column=0)

l1=tk.Label(entry_frame, text="Title")
l1.grid(row=0,column=0)

l2=tk.Label(entry_frame, text="Author")
l2.grid(row=0,column=2)

l3=tk.Label(entry_frame, text="Year")
l3.grid(row=1,column=0)

l4=tk.Label(entry_frame, text="Rating")
l4.grid(row=1,column=2)

l5=tk.Label(entry_frame, text="Publishing House")
l5.grid(row=0, column=5)

l6=tk.Label(entry_frame, text="No of Readings")
l6.grid(row=1, column=5)

l7=tk.Label(entry_frame, text="Closet")
l7.grid(row=0, column=7)

l8=tk.Label(entry_frame, text="Shelf")
l8.grid(row=1, column=7)

title_text=tk.StringVar()
e1=tk.Entry(entry_frame,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=tk.StringVar()
e2=tk.Entry(entry_frame,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=tk.StringVar()
e3=tk.Entry(entry_frame,textvariable=year_text)
e3.grid(row=1,column=1)

rating_text=tk.StringVar()
e4=tk.Entry(entry_frame,textvariable=rating_text)
e4.grid(row=1,column=3)

publishing_text=tk.StringVar()
e5=tk.Entry(entry_frame,textvariable=publishing_text)
e5.grid(row=0,column=6)

noreading_text=tk.StringVar()
e6=tk.Entry(entry_frame,textvariable=noreading_text)
e6.grid(row=1,column=6)

closet_text=tk.StringVar()
e7=tk.Entry(entry_frame,textvariable=closet_text)
e7.grid(row=0,column=8)

shelf_text=tk.StringVar()
e8=tk.Entry(entry_frame,textvariable=shelf_text)
e8.grid(row=1,column=8)

#Buttons Frame----------------------------------------------------------------------
buttons_frame = tk.LabelFrame(window, text="Actions")
buttons_frame.grid(row=1, column=0)

b1=tk.Button(buttons_frame,text="View all", width=12, command=view_command)
b1.grid(row=0, column=1)

b2=tk.Button(buttons_frame,text="Search entry", width=12, command=search_command)
b2.grid(row=0, column=2)

b3=tk.Button(buttons_frame,text="Add entry", width=12, command=add_command)
b3.grid(row=0, column=3)

b7=tk.Button(buttons_frame, text="Clear Entry",width=12, command=clear_command)
b7.grid(row=0,column=4)

b4=tk.Button(buttons_frame,text="Update Selected", width=12, command=update_command)
b4.grid(row=0, column=5)

b5=tk.Button(buttons_frame,text="Delete Selected", width=12, command=delete_command)
b5.grid(row=0, column=6)

b6=tk.Button(buttons_frame,text="Close", width=12, command=window.destroy)
b6.grid(row=0, column=7)



#list frame-------------------------------------------------------------------------------------------
"""
group1 = tk.LabelFrame(window, text="Book List")
group1.grid(row=2, column=0, columnspan=8,sticky=tk.E+tk.W+tk.N+tk.S)

list1=tk.Listbox(group1,height=20,width=50)
list1.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)

sb1=tk.Scrollbar(group1)
sb1.grid(row=0,column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ButtonRelease-1>>', get_selected_row)
"""


#treeview frame----------------------------------------------------------------------------------------------
group2=ttk.LabelFrame(window, text="Tree View")
group2.grid(row=2, column=0, columnspan=8,sticky=tk.E+tk.W+tk.N+tk.S)

tv = ttk.Treeview(group2, columns=(1,2,3,4,5,6,7,8,9), show='headings')
tv.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)

tv.column('#1', stretch=NO, minwidth=0, width=0)
tv.heading(1, text="ID")
tv.heading(2, text="Title")
tv.heading(3, text="Author")
tv.heading(4, text="Year")
tv.heading(5, text="Rating")
tv.heading(6, text="Publishing House")
tv.heading(7, text="No Reading")
tv.heading(8, text="Closet")
tv.heading(9, text="Shelf")

#tv["displaycolumns"]=("Title","Year","Rating","Publishing","No Reading","Closet","Shelf")
tv.bind('<<TreeviewSelect>>', get_selected_row)

window.columnconfigure(0, weight=1)
window.rowconfigure(2, weight=1)

"""
group1.rowconfigure(0, weight=1)
group1.columnconfigure(0, weight=1)
"""

group2.rowconfigure(0, weight=1)
group2.columnconfigure(0, weight=1)

window.mainloop()
