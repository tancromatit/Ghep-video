from flask import Flask, render_template, request, send_file
import os
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FILE = "output.mp4"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    files = request.files.getlist("videos")

    paths = []

    for file in files:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        paths.append(path)

    # gọi file ghép video của bạn
    subprocess.run(["python", "auto_ghep_video.py"])

    return send_file(OUTPUT_FILE, as_attachment=True)


if __name__ == "__main__":
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)