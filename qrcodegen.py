from tkinter.constants import ANCHOR, W
import qrcode
import tkinter as tk
from tkinter import Label, Scale, StringVar, filedialog
from PIL import Image, ImageTk

""" Quick and dirty local QR code generator """


# Save function, taking qr.pil object
def savefile(qr_img):
    filename = tk.filedialog.asksaveasfilename(defaultextension=".png")
    if not filename:
        return
    else:
        qr_img.save(filename)


#start tkinter 
root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
canvas = tk.Canvas(root)
canvas.grid(columnspan=6, rowspan=7)

#outer layers
top_layer= tk.Label(root)
top_layer.grid(columnspan=6, column=0, row=0)
btm_layer = tk.Label(root)
btm_layer.grid(columnspan=6, column=0, row=7)
left_layer = tk.Label(root)
left_layer.grid(rowspan=7, column=0, row=0)
right_layer = tk.Label(root)
right_layer.grid(rowspan=7, column=5, row=0)

#logo space
logo = Image.open('logo.jpg')
logo.thumbnail([80,80])
logo = ImageTk.PhotoImage(logo)
logo_label =tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=1)

#Title
title = tk.Label(root, text="QRCode-Gen")
title.grid(columnspan=4, column=1, row=0)

#instructions
instructions = tk.Label(root, text="""QR-Code Generator by Thiemo for personal, local use
quick and dirty...
Paste a URL to create a QR code locally
2021""")
instructions.grid(columnspan=3, column=2, row=1)


#uses py qrcode to generate qrcode image, generates qr.pil object
def make_qr():
    txt = text_line.get()
    qr_img = qrcode.make(txt)

    #if qr pil object has been created, show qr code and add button to save the file
    if qr_img:
        #create label
        qr_show_img = ImageTk.PhotoImage(qr_img)
        qr_show = tk.Label(image = qr_show_img)
        qr_show.image = qr_show_img
        qr_show.grid(columnspan=4, column=1, row=4, pady=5)

        #create save btn
        save_btn = tk.Button(root, text="Speichern", command=lambda:savefile(qr_img), height=2, width=15)
        save_btn.grid(columnspan=2, column=2, row=5, pady=5)



#url entry box
text_line = tk.Entry(root, width=45)
text_line.grid(columnspan=3, column=2, row=2, sticky="w", padx=20, pady=20)
#url entry box instruction
label_text= tk.StringVar()
label_text.set("Url:")
label_info=Label(root, textvariable=label_text)
label_info.grid(column=1, row=2)

#create qr button
create_btn = tk.Button(root, command=lambda:make_qr(), text="Erstellen", height=2, width=15, pady=5)
create_btn.grid(columnspan=2, column=2, row=3)


root.mainloop()