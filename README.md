

# **SneakPixel** - *Hack the Pixels, Hide Your Secrets*

**“Information wants to be free. And so do your secrets.”**

Welcome to **SneakPixel**, where **digital espionage** meets **steganography**. Hide your messages inside images, just like the best hackers of the 90s. Encrypt your world, decode the unknown.

---

## **🚨 Features:**
- **Encode Messages**: Insert your secret into an image. No one will know unless they have the key.
- **Decode Messages**: Upload an image, and if it contains a hidden message, **SneakPixel** will reveal it.
- **Session Security**: Use a system-generated session key or bring your own custom cryptographic key.
- **Private and Secure**: Encrypt messages and images with the key only you control.

---

## **💾 Setup - Your Digital Safehouse**

1. **Clone the Repo**:
    ```bash
    git clone https://github.com/yourusername/sneakpixel.git
    cd sneakpixel
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare Upload Folder**:
    ```bash
    mkdir -p static/uploaded_images
    ```

4. **Start the App**:
    ```bash
    python app.py
    ```

5. Go to `http://127.0.0.1:5000/`—your secret base.

---

## **🖥️ How It Works**

1. **Encoding**: Upload an image and a secret message. The system hides the message inside the image using cryptography. You can use a session-generated key or your own custom key.
   
2. **Decoding**: Upload an image with a hidden message. If you’ve got the key, **SneakPixel** will reveal the secret.

---

## **⚡️ Security**

- **Session Key**: No key? No problem. A unique session key keeps your messages secure.
- **Custom Key**: Use your own key for complete control over your encrypted messages.

---

## **💡 Contributing**

Ready to break the system? Fork, code, and submit your changes. Let’s keep the revolution alive.

---

## **🎬 Inspired by the Hackers’ Universe**

Inspired by *Hackers* (1995), where the code is the weapon, and the digital world is a playground for the brave. **SneakPixel** is your gateway to hiding and revealing secrets.  

*“Hack the planet. Hide your secrets.”*

---

Let me know if you want further edits! 😎
