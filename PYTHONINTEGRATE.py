from flask import Flask, render_template, request, redirect
import os

app = Flask(PYTHONINTEGRATE)
os.makedirs('uploads', exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST" and request.form["pass"] == "1234":
        return redirect("/upload")
    return render_template("login.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        if file.filename.endswith((".docx", ".pptx", ".xlsx")):
            file.save("uploads/" + file.filename)
            return "Uploaded: " + file.filename
        return "Invalid file!"
    return render_template("upload.html")

app.run(debug=true)