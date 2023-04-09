from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
import tkinter as tk
import asyncio
from camera import count

root = tk.Tk()
root.geometry("320x240")
root.title("Cash Safe")

#color info
light_blue = (84, 140, 230)
color_string = "#%02x%02x%02x" % light_blue


#
text_var = StringVar()
text_var.set("str(count())")

def update_text():
    text_var.set("Dollars: " + str(count()))
    # Schedule the function to be called again after 1 second
    root.after(100, update_text)

text_var = StringVar()
total_display = tk.Label(bg="white", textvariable=text_var, font=("Arial", 12))
total_display.pack(padx=5, pady=5)

# Call the update_text function to start the label updating
update_text()



# Root background info
canvas = tk.Canvas(root, bg=color_string, width=800, height=800)
canvas.pack(expand=True)


#Coin info
coin1 = canvas.create_oval(50, 50, 100, 100, fill="gold", outline="yellow")
coin2 = canvas.create_oval(20, 20, 100, 100, fill="gold")
coin3 = canvas.create_oval(50, 50, 100, 100, fill="gold")
#coin1.place(padx=50, pady=20)


root.mainloop()
