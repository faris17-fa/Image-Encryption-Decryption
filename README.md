# image-encryption-decryption
This project implements a basic Image Encryption and Decryption tool using Python. The application provides a graphical user interface (GUI) built with Tkinter that allows users to encrypt and decrypt images using a simple XOR-based algorithm.

#Features
Encrypt Images: Select a JPG image from your file system and encrypt it with a key.
Decrypt Images: Decrypt an encrypted image using the same key.
Graphical Interface: User-friendly interface for easy interaction with the encryption and decryption processes.
#How It Works
Encryption: The image is read as a byte array, and each byte is XORed with the provided key, resulting in an encrypted image file.
Decryption: The encrypted image can be decrypted by applying the same key used during encryption. The decryption process reverses the XOR operation to restore the original image.
#Requirements
Python 3.x
Tkinter
PIL (Pillow)
#Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/image-encryption-decryption.git
cd image-encryption-decryption
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Alternatively, you can manually install the required packages:

bash
Copy code
pip install Pillow
Usage
Run the application:

bash
Copy code
python image_encryption_decryption.py
Use the GUI to:

Click Choose to select an image file.
Enter an integer key in the Enter Key field.
Click Encrypt to encrypt the selected image.
Click Decrypt to decrypt the encrypted image.
The encrypted and decrypted images can be saved to your desired location.

Project Structure
image_encryption_decryption.py: Main Python script containing the implementation of the encryption and decryption tool.
requirements.txt: List of dependencies required for the project.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize the README as needed!






