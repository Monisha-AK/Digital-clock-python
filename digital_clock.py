from tkinter import *
from time import strftime
root=Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.config(bg="black")
def time():
    s=strftime('%H:%M:%S %p')
    label.config(text=s)
    label.after(1000,time)
label=Label(root,font=('calibri',40,'bold'),background='black',foreground='#FFB6C1')
label.pack(anchor='center')
time()
root.mainloop()
