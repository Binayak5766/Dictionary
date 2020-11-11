import json
import tkinter as tk
from difflib import get_close_matches

data = json.load(open("data.json"))


def search_word():
    word = e1.get()
    word = word.lower()
    list1.delete(0,tk.END)

    if word in data:                           #This line searches the word directly and prints if it is there in the file.
        if type(data[word]) == list:
            for item in data[word]:
                list1.insert(tk.END,item)

    elif word.upper() in data:
        if type(data[word.upper()]) == list:
            for item in data[word.upper()]:
                list1.insert(tk.END,item)

    elif word.title() in data:
        if type(data[word.title()]) == list:
            for item in data[word.title()]:
                list1.insert(tk.END,item)
    
    elif len(get_close_matches(word, data.keys())) > 0:       #This line gets the close matches of the word and shows the most appropriate to us
        list1.delete(0,tk.END)
        list1.insert(tk.END,"Did you mean these instead?")      #This line asks if this is the word we are looking
        for each in get_close_matches(word,data.keys()):
            list1.insert(tk.END,each)

    else:
        list1.delete(0,tk.END)
        list1.insert(tk.END,"The word does not exist in the dictionary. Please double check it!!!!")

top = tk.Tk()
top.title("Dictionary")

e1 = tk.Entry(top, text = "", width = 60, borderwidth = 5, font = 'Calibri 11')
e1.grid(row = 0,column = 0, padx = '10', pady = '10', columnspan = 4)

list1 = tk.Listbox(top, height = 10, width = 55)
list1.grid(row = 1, column = 0, rowspan = 6, columnspan = 2, padx = '10', pady = '10')

sb1 = tk.Scrollbar(top, orient=tk.HORIZONTAL, width=25)
sb1.grid(row=7, column=0, columnspan=2)

list1.configure(xscrollcommand=sb1.set)
sb1.configure(command=list1.xview)

butn1 = tk.Button(top, text = "Search", width = 12, command = search_word)
butn1.grid(row = 1, column = 3)

butn2 = tk.Button(top, text = "Close", width = 12, command = top.destroy)
butn2.grid(row = 2, column = 3)

top.mainloop()
