import qrcode
from tkinter import messagebox
from PIL import Image,ImageTk

def generate_qr(entry, headline, display_qr):
    webUrl = entry.get()

    if not webUrl:
        messagebox.showerror("Error", "Please enter valid URL to generate the QR Code")
        return None
    
    myqr = qrcode.QRCode(version=2)
    myqr.add_data(webUrl)
    myqr.make(fit=True)

    global img,imgtk
    img = myqr.make_image()

    imgtk =  ImageTk.PhotoImage(img)
    display_qr.config(image=imgtk)
    display_qr.image = imgtk
    headline.config(text="Image Generated Successfully!!")

    return img