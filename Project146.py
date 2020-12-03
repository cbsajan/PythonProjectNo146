# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:58:38 2020

@author: C.B.Sajan
"""

from tkinter import *

root=Tk()
root.title("ASCII Converter And Encryption")

root.geometry("400x400")
root.configure(background="light pink")

textinput=Entry(root)
textinput.place(relx=0.5,rely=0.4,anchor=CENTER)

label_ascii=Label(root,text="",fg="red",bg="light pink")
label_ascii.configure(state="disabled")
label_encryption=Label(root,text="",fg="red",bg="light pink")
label_encryption.configure(state="disabled")
# this will arrange entry widgets 


def asciiconverter():
    input_from_user=textinput.get()
    print(input_from_user)
    for letter in input_from_user:
        asciivalue=ord(letter)
        print(asciivalue)
        
        encryptionnum=int(asciivalue)-1
        print(encryptionnum)
        encryptionvalue=str(chr(encryptionnum))
        print(encryptionvalue)
        label_ascii["text"]+=str(asciivalue) + " "
        label_encryption["text"]+=encryptionvalue
        
       
btn=Button(root,text="Show The Name In ASCII",command=asciiconverter,fg="red",bg="light blue")
label_ascii.place(relx=0.5,rely=0.5,anchor=CENTER)
label_encryption.place(relx=0.5,rely=0.6,anchor=CENTER)
btn.place(relx=0.5,rely=0.7,anchor=CENTER)



root.mainloop()