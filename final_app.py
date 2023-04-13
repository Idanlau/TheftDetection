import tkinter as tk
from camera import count # import count function from camera python file

root = tk.Tk # initialize tkinter
root.geometry("800x800) # set app width
root.title("Cash Safe") 

# color info
light_blue = (97, 137, 183)
color_string = "#%02x%02x%02x" % light_blue

# Root background info
canvas = tk.Canvas(root, bg=color_string, width=800, height=800)
canvas.pack(expand=True)

# Text
text_frame = tk.Frame(root, width=221, height=70)
text_frame.place(x=155, y=110)

text_label = tk.Label(text_frame, text="SMRT BOX", font=("Bold", 75), bg=color_string, fg="white")
text_label.pack(fill=tk.BOTH, expand=True)

# Image
image_frame = tk.Frame(root, width=200, height=154.76)
image_frame.place(x=400, y=530, anchor="center")
image_label = tk.Label(image_frame, bg=color_string)
image_label.pack(fill=tk.BOTH, expand=True)

image = tk.PhotoImage(file="Image.png")
image_label.config(image=image)
image_label.image = image

# Apply filter to the image
image_label.config(highlightthickness=0, bd=0)
image_label.bind("<Configure>", lambda e: image_label.config(width=e.width, height=e.height))

text_var = tk.StringVar()
text_var.set("count()")

def update_text():
    text_var.set("Dollars: " + str(count()))
    # Schedule the function to be called again after 1 second
    root.after(100, update_text)
    
label2_frame = tk.Frame(root, width=200, height=154.76)
label2_frame.place(x=400, y=320, anchor="center")
label2 = tk.Label(label2_frame, textvariable=text_var, font=("Helvetica", 70), bg=color_string, fg="black")
label2.pack(fill=tk.BOTH, expand=True)

update_text()
root.mainloop()


