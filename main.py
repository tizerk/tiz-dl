import yt_dlp
import video
import audio
from datetime import datetime

ydl_opts = {"quiet": True,}
ydl = yt_dlp.YoutubeDL(ydl_opts)

def main():
    url = input("Enter YouTube URL: ")
    with ydl:
        result = ydl.extract_info(url, download=False)

        if "title" in result:
            print(f'Title: {result["title"]}')

        if "uploader" in result:
            print(f'Creator: {result["uploader"]}')

        if "upload_date" in result:
            date = datetime.strptime(result["upload_date"], "%Y%m%d")
            print(f"Upload Date: {date.strftime("%b")} {date.strftime("%d")}, {date.strftime("%Y")}")

        choice(url)

def choice(url):
    medium = input("Video or Audio? (v/a)").lower()

    if medium == "v":
        video(url, ydl, ydl_opts)
    elif medium == "a":
        audio(url, ydl, ydl_opts)
    else:
        print("Incorrect Input, Try Again\n")
        choice(url)

main()
