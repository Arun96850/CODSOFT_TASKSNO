from flask import Flask, request, redirect, url_for, session, render_template_string, send_file
from cryptography.fernet import Fernet
import os

app = Flask(__name__)
app.secret_key = "secure-file-sharing-secret"

UPLOAD_FOLDER = "uploads"
KEY_FILE = "secret.key"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as f:
        f.write(Fernet.generate_key())

with open(KEY_FILE, "rb") as f:
    encryption_key = f.read()

cipher = Fernet(encryption_key)

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Secure File Sharing</title>
    <style>
        body {
            font-family: Arial;
            background: #eef2f7;
            margin: 0;
            padding: 30px;
        }

        .container {
            max-width: 700px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 12px;
        }

        h1 {
            color: #17365d;
            text-align: center;
        }

        input, button {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            box-sizing: border-box;
        }

        button {
            background: #17365d;
            color: white;
            border: none;
            border-radius: 6px;
        }

        .file {
            padding: 12px;
            background: #f1f5f9;
            margin: 8px 0;
            border-radius: 6px;
        }

        .success {
            color: green;
        }

        .error {
            color: red;
        }
    </style>
</head>

<body>
<div class="container">

{% if not session.get("username") %}

<h1>🔐 Secure File Sharing</h1>

<form method="POST" action="/login">
    <input type="text" name="username" placeholder="Username" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Login</button>
</form>

{% if error %}
<p class="error">{{ error }}</p>
{% endif %}

{% else %}

<h1>📁 Secure File Sharing</h1>

<p>
Welcome, <b>{{ session["username"] }}</b>
({{ session["role"] }})
</p>
{% if session["role"] == "admin" %}
<form method="POST" action="/upload" enctype="multipart/form-data">
    <input type="file" name="file" required>
    <button type="submit">🔒 Encrypt & Upload</button>
</form>
{% endif %}
{% if message %}
<p class="success">{{ message }}</p>
{% endif %}

<h2>Available Files</h2>

{% for file in files %}
<div class="file">
    {{ file }}
    <br><br>
    <a href="/download/{{ file }}">
        <button>⬇️ Download</button>
    </a>
</div>
{% endfor %}

<a href="/logout">
    <button>Logout</button>
</a>

{% endif %}

</div>
</body>
</html>
"""

@app.route("/")
def home():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML, files=files)


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username in users and users[username]["password"] == password:

        session["username"] = username
        session["role"] = users[username]["role"]

        return redirect(url_for("home"))

    return render_template_string(
        HTML,
        error="❌ Invalid username or password.",
        files=[]
    )


@app.route("/upload", methods=["POST"])
def upload():

    if "username" not in session:
        return redirect(url_for("home"))
    if session.get("role") != "admin":
        return "Access denied: Admin only", 403
    file = request.files["file"]

    if file.filename == "":
        return redirect(url_for("home"))

    data = file.read()

    encrypted_data = cipher.encrypt(data)

    filename = file.filename + ".enc"

    with open(os.path.join(UPLOAD_FOLDER, filename), "wb") as f:
        f.write(encrypted_data)

    return render_template_string(
        HTML,
        files=os.listdir(UPLOAD_FOLDER),
        message="✅ File encrypted and uploaded successfully!"
    )


@app.route("/download/<filename>")
def download(filename):

    if "username" not in session:
        return redirect(url_for("home"))

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(filepath):
        return "File not found", 404

    with open(filepath, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    temp_file = "temp_download"

    with open(temp_file, "wb") as f:
        f.write(decrypted_data)

    original_name = filename.replace(".enc", "")

    return send_file(
        temp_file,
        as_attachment=True,
        download_name=original_name
    )



@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)		

