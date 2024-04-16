import tkinter as ui
import time 
import math     
def update():
    hour = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))
    
    sec_x = sec_len * math.sin(math.radians(seconds * 6)) + x
    sec_y = -1 * sec_len * math.cos(math.radians(seconds * 6)) + y
    canvas.coords(sec_hand, x, y, sec_x, sec_y)
    
    min_x = min_len * math.sin(math.radians(minutes * 6)) + x
    min_y = -1 * sec_len * math.cos(math.radians(minutes * 6)) + y
    canvas.coords(min_hand, x, y, min_x, min_y)
    
    hour_x = hour_len * math.sin(math.radians(hour * 6)) + x
    hour_y = -1 * sec_len * math.cos(math.radians(hour * 6)) + y
    canvas.coords(hour_hand, x, y, hour_x,hour_y)
    
    window.after(1000,update)
    
window = ui.Tk()
window.geometry("464x600")

canvas= ui.Canvas(window, width=464,height=600,bg="white")
canvas.pack(expand=True, fill='both')
bg= ui.PhotoImage(file='clock1.png')
canvas.create_image(232, 300, image=bg)

x= 232
y=300
sec_len=140
min_len=127
hour_len=93

sec_hand=canvas.create_line(232, 300,232 + sec_len, 300 + sec_len, width=1.5, fill='cyan')
min_hand=canvas.create_line(232, 300,232 + min_len, 300 + min_len, width=2, fill='red')
hour_hand=canvas.create_line(232, 300,232 + hour_len, 300 + hour_len, width=4, fill='green')

update()
window.mainloop()