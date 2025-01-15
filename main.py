from flask import Flask, request, render_template, redirect, url_for, send_file, session, flash
import os
from cryptosteganography import CryptoSteganography
import secrets

app = Flask(__name__)

# Randomly generate a secure secret key for Flask
app.secret_key = secrets.token_hex(32)  # 64-character hex string for a strong secret key

app.config['UPLOAD_FOLDER'] = 'static/uploaded_images'

@app.route("/", methods=["GET", "POST"])
def index():
    crypto_key = None

    if request.method == "POST":
        # Get the entered secret key or generate a session key if none is provided
        user_key = request.form.get("user_key")
        if user_key:
            crypto_key = user_key
        else:
            if "session_key" not in session:
                session["session_key"] = secrets.token_hex(16)  # Generate session key
            crypto_key = session["session_key"]

        crypto_steganography = CryptoSteganography(crypto_key)

        # Handle message encoding
        if "encode" in request.form:
            message = request.form["message"]
            image = request.files["image"]

            if message and image:
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(image_path)

                # Encode the message in the image
                output_path = os.path.join(app.config['UPLOAD_FOLDER'], "encoded_image.png")
                crypto_steganography.hide(image_path, output_path, message)
                return send_file(output_path, as_attachment=True)

        # Handle message decoding
        elif "decode" in request.form:
            image = request.files["encoded_image"]

            if image:
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(image_path)

                # Decode the message from the image
                message = crypto_steganography.retrieve(image_path)
                return f"Decoded message: {message}"

    return render_template("index.html", session_key=session.get("session_key"))

if __name__ == "__main__":
    app.run(debug=True)
