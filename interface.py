from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("Cash Safe")



# Root background info
light_blue = (84, 140, 230)
color_string = "#%02x%02x%02x" % light_blue
canvas = tk.Canvas(root, bg=color_string, width=320, height=240)
canvas.pack(expand=True)

#Coin info
coin1 = canvas.create_oval(50, 50, 100, 100, fill="gold", outline="yellow")
coin2 = canvas.create_oval(20, 20, 100, 100, fill="gold")
coin3 = canvas.create_oval(50, 50, 100, 100, fill="gold")
#coin1.place(padx=50, pady=20)

root.mainloop()
