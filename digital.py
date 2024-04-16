from tkinter import *
from time import *
def update():
    time_string = strftime ("%I : %M : %S %p")
    label.config(text=time_string)
    label.after(1000,update)
window = Tk()

label= Label(window,font=("Arial",50),fg="#40E0D0",bg="black")
label.pack()

update()
window.mainloop()

