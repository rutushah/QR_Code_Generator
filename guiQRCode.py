import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import qrGenerate

#this is the code for generating GUI for python application using tkinter

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")

headline = tk.Label(root,text="Enter Text and Click Generate Button", font=("Arial, 12"))
headline.pack(pady=12)

entry = tk.Entry(root, width=40, font=("Arial,12"))
entry.pack(pady=12)

frame = tk.Frame(root)
frame.pack(pady=12)

generated_data = {'img':None}

def generate_and_store_qr():
    img = qrGenerate.generate_qr(entry,headline,display_qr)
    generated_data['img'] = img

generate_button = tk.Button(frame,text="Generate QR Code ",font=("Arial,12"),command=generate_and_store_qr)
generate_button.pack(side=tk.LEFT, padx=10)

display_qr = tk.Label(root)
display_qr.pack(padx=10)

imgtk = None
root.mainloop()