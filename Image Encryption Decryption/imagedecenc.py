from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Initialize Tkinter window
window = Tk()
window.geometry("1000x700")
window.title("Image Encryption Decryption")

# Defined variables
f = None #store the file object of slected image
image_label = None #store label widget
encrypted_file_name = None  # To store the name of the encrypted file

# Function to open the selected image
def open_img():
    global f, image_label
    f = filedialog.askopenfile(mode='r', filetypes=[('JPG files', '*.jpg')])
    if f:
        img_path = f.name
        img = Image.open(img_path)
        img = img.resize((500, 500), Image.LANCZOS)  # Resize the image to fit in the window
        img_tk = ImageTk.PhotoImage(img) #convert img to format suitable for tkinter

        if image_label is None:
            image_label = Label(window, image=img_tk)
            image_label.image = img_tk  # Keep a reference to avoid garbage collection
            image_label.place(x=250, y=50)
        else:
            image_label.config(image=img_tk)
            image_label.image = img_tk

# Function to encrypt the image
def encrypt_img():
    global f, image_label, encrypted_file_name
    file1 = f
    if file1 is not None:
        file_name = file1.name
        key = key_entry.get(1.0, END).strip() #retrive key entered by user
        try:
            key = int(key) #convert key to key integer
        except ValueError:
            messagebox.showerror("Error", "Enter a valid Key \nKey must be an integer.")
            return

        with open(file_name, 'rb') as fi: #reads img in binary mode
            image = fi.read()
        image = bytearray(image) #convert img to mutable byte array (0-256 BYTES)
        for index, values in enumerate(image):
            image[index] = values ^ key

        encrypted_file_name = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if encrypted_file_name:
            with open(encrypted_file_name, 'wb') as fil:
                fil.write(image)
            messagebox.showinfo("Encrypt Status", "Image Encrypted successfully.")
        
        # Hide the image from the window
        if image_label is not None:
            image_label.place_forget() #hides img from window

# Function to decrypt the image
def decrypt_img():
    global encrypted_file_name, image_label
    if encrypted_file_name is None:
        messagebox.showerror("Error", "No image has been encrypted yet.")
        return

    key = key_entry.get(1.0, END).strip()
    try:
        key = int(key)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid key \nKey must be an integer.")
        return

    with open(encrypted_file_name, 'rb') as fi:
        image = fi.read()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key

    decrypted_file_name = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
    if decrypted_file_name:
        with open(decrypted_file_name, 'wb') as fil:
            fil.write(image)
        messagebox.showinfo("Decrypt Status", "Image Decrypted successfully.")

        # Display the decrypted image
        img = Image.open(decrypted_file_name)
        img = img.resize((500, 500), Image.LANCZOS)  # Resize the image to fit in the window
        img_tk = ImageTk.PhotoImage(img)

        if image_label is None:
            image_label = Label(window, image=img_tk)
            image_label.image = img_tk  # Keep a reference to avoid garbage collection
            image_label.place(x=250, y=50)
        else:
            image_label.config(image=img_tk)
            image_label.image = img_tk
            
# exit button created 
def exit_win():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# UI components
encrypt_btn = Button(window, text="Encrypt", command=encrypt_img, font=("Arial", 20), bg="light green", fg="blue", borderwidth=3, relief="raised")
encrypt_btn.place(x=100, y=620)

decrypt_btn = Button(window, text="Decrypt", command=decrypt_img, font=("Arial", 20), bg="orange", fg="blue", borderwidth=3, relief="raised")
decrypt_btn.place(x=800, y=620)

key_label = Label(window, text="Enter Key:", font=("Arial", 13))
key_label.place(x=450, y=600)

key_entry = Text(window, height=1, width=10)
key_entry.place(x=450, y=630)

chooseb = Button(window, text="Choose", command=open_img, font=("Arial", 20), bg="orange", fg="blue", borderwidth=3, relief="raised") 
chooseb.place(x=30, y=20)

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="groove")
exitb.place(x =880 , y =20 )

window.mainloop()