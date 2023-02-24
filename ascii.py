from tkinter import *

root=Tk()
root.title("Codigo Ascii")
root.geometry("500x500")
root.config(background='blue')
enter_word=Entry(root)
label2=Label(root,text="Ingresa una letra o una palabara",bg="light pink",fg="purple")
label2.place(relx=0.35,rely=0.2)
enter_word.place(relx=0.5 ,rely=0.3,anchor=CENTER)
label=Label(root,text="Nombre del codigo ascci",bg="red",fg="black")
def ascci_conventer():
 input_word =enter_word.get() 
 for letter in input_word : 
     label["text"] += str(ord(letter)) + " "



btn=Button(root,text="Dale click",command=ascci_conventer,bg="orange",fg="brown")
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
label.place(relx=0.5,rely=0.17,anchor=CENTER)
root.mainloop()

