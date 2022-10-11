from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("350x150")
app_window.minsize(290,130)

text_font = ("Bold", 68, 'bold')
background = 'yellow'
foreground = 'black'
border_width = 40

label = Label(app_window, font=text_font, bg=background, fg=foreground,
            bd=border_width)   
label.grid(row=0, column=1)

def digital__clock():
    time_live = time.strftime("%I:%M:%S")
    label.config(text=time_live)
    label.after(200, digital__clock)

digital__clock()
app_window.mainloop()