import os
import subprocess

video_folder = "videos"
output_file = "output.mp4"

videos = sorted([
    f for f in os.listdir(video_folder)
    if f.lower().endswith((".mp4", ".mov"))
])

with open("list.txt", "w", encoding="utf-8") as f:
    for video in videos:
        path = os.path.join(video_folder, video).replace("\\", "/")
        f.write(f"file '{path}'\n")

subprocess.run([
    "ffmpeg",
    "-f", "concat",
    "-safe", "0",
    "-i", "list.txt",
    "-c", "copy",
    output_file
])

print("✅ Ghép video xong!")