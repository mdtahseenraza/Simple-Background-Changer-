import os
import tkinter as tk
from tkinter import filedialog
import ctypes
from PIL import Image, ImageTk
import time

selected_image = None
image_on_canvas = None


def set_wallpaper(feedback_label):
    try:
        global selected_image
        selected_image.save("selected_image.jpg")

        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("selected_image.jpg"), 3)

        feedback_label.config(text="Image wallpaper has been set successfully", fg="green")
        time.sleep(1)
    except Exception as e:
        feedback_label.config(text="Error: Please select an image before setting wallpaper", fg="red")

def browse_wallpaper(feedback_label, canvas):
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if file_path:
        global selected_image, image_on_canvas
        selected_image = Image.open(file_path)

        image_width, image_height = selected_image.size

       
        canvas.config(width=image_width, height=image_height)
        canvas.create_rectangle(0, 0, image_width, image_height, outline="white", width=0)


        img = ImageTk.PhotoImage(selected_image)
        if image_on_canvas:
            canvas.delete(image_on_canvas) 
        image_on_canvas = canvas.create_image(0, 0, anchor=tk.NW, image=img)
        canvas.image = img

        feedback_label.config(text="Click 'Set Wallpaper' to set the selected image as wallpaper", fg="black")

root = tk.Tk()
root.title("Image Wallpaper Setter")

credits_label = tk.Label(root, text="Made by (Md Tahseen Raza) Connect to Github", font=("Helvetica", 12), fg="blue", cursor="hand2")
credits_label.pack(side=tk.TOP)
credits_label.bind("<Button-1>", lambda e: os.system("start https://github.com/mdtahseenraza"))


set_button = tk.Button(root, text="Set Wallpaper", command=lambda: set_wallpaper(feedback_label), font=("Helvetica", 14))
set_button.pack(pady=10, side=tk.TOP)


browse_button = tk.Button(root, text="Browse for Wallpaper", command=lambda: browse_wallpaper(feedback_label, canvas), font=("Helvetica", 14))
browse_button.pack(pady=10, side=tk.TOP)


canvas = tk.Canvas(root, bg="white")
canvas.pack()

feedback_label = tk.Label(root, text="Select an image and click 'Set Wallpaper' to set it as wallpaper", font=("Helvetica", 12), fg="black")
feedback_label.pack()

root.mainloop()
