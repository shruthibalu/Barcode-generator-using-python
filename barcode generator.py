import barcode
import tkinter as tk
from PIL import ImageTk, Image

# function to generate barcode and display in GUI window
def generate_barcode():
    format = format_entry.get()
    data = data_entry.get()
    code = barcode.get(format, data)
    filename = code.save("barcode")
    image = Image.open(filename)
    image = image.resize((300, 200))
    photo = ImageTk.PhotoImage(image)
    barcode_label.config(image=photo)
    barcode_label.image = photo

# create GUI window
window = tk.Tk()
window.title("Barcode Generator")

# create entry fields for barcode format and data
format_label = tk.Label(window, text="Barcode format (EAN-13, UPC-A, etc.):")
format_label.pack()
format_entry = tk.Entry(window)
format_entry.pack()

data_label = tk.Label(window, text="Data to encode:")
data_label.pack()
data_entry = tk.Entry(window)
data_entry.pack()

# create button to generate barcode
generate_button = tk.Button(window, text="Generate Barcode", command=generate_barcode)
generate_button.pack()

# create label to display generated barcode image
barcode_label = tk.Label(window)
barcode_label.pack()

# start the main loop
window.mainloop()
