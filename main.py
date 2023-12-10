import yt_dlp
from yt_dlp.utils import DownloadError
from video import *
from audio import *
from datetime import datetime


class loggerOutputs:
    def error(msg):
        print("Captured Error: " + msg)
    def warning(msg):
        print("Captured Warning: " + msg)
    def debug(msg):
        print("Captured Log: " + msg)

ydl_opts = {
    "quiet": True,
    "logger": loggerOutputs,
}
ydl = yt_dlp.YoutubeDL(ydl_opts)


def get_video_data(url, title, creator, upload_date):
    if url != "":
        with ydl:
            try:
                result = ydl.extract_info(url, download=False)
                if "title" in result:
                    title.set(f'Title: {result["title"]}')     
                if "uploader" in result:
                    creator.set(f'Creator: {result["uploader"]}')
                if "upload_date" in result:
                    date = datetime.strptime(result["upload_date"], "%Y%m%d")
                    upload_date.set(f"Upload Date: {date.strftime("%b")} {date.strftime("%d")}, {date.strftime("%Y")}")
            except DownloadError:
                title.set(f'Title: Not a Valid URL!!  Try Again.')
                creator.set(f'Creator: Not a Valid URL!!  Try Again.')
                upload_date.set(f'Upload Date: Not a Valid URL!!  Try Again.')

        

# def main():
#     url = input("Enter YouTube URL: ")
# with ydl:
#     result = ydl.extract_info(url, download=False)

#     if "title" in result:
#         print(f'Title: {result["title"]}')

#     if "uploader" in result:
#         print(f'Creator: {result["uploader"]}')

#     if "upload_date" in result:
#         date = datetime.strptime(result["upload_date"], "%Y%m%d")
#         print(f"Upload Date: {date.strftime("%b")} {date.strftime("%d")}, {date.strftime("%Y")}")

#     choice(url)

# def choice(url):
#     medium = input("Video or Audio? (v/a)").lower()

#     if medium == "v":
#         video(url, ydl, ydl_opts)
#     elif medium == "a":
#         audio(url, ydl, ydl_opts)
#     else:
#         print("Incorrect Input, Try Again\n")
#         choice(url)

# main()
