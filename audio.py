import yt_dlp
import ffmpeg
import os

def audio(url, ydl, ydl_opts):
    ydl_opts = {
        "quiet": True,
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s"
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    result = ydl.extract_info(url, download=False)

    format = format_choice()

    ydl.download(url)
    input_file = f"{result["title"]}.{result["ext"]}"

    output_file = f"{result["title"]}{format}"
    if (format != ".WEBM"):
        ffmpeg.input(input_file).output(output_file).run()
        os.remove(input_file)
    print("Download Complete!")


def format_choice():
    print("Available Format Options:")
    count = 0
    formats = [".MP3", ".FLAC", ".WAV", ".AAC", ".WEBM", ".MOV", ".OGG", ".OPUS", ".AIFF", ".M4A"]
    for i in formats:
        count += 1
        print(f"{count}: {i}")
    try:
        choice = int(input("Select Desired Format: "))
    except ValueError:
        print(
            "Incorrect Input: Enter the Integer Value Next to the Desired Resolution\n"
        )
        format_choice(formats)
    if 0 >= choice or choice > count:
        print(
            "Incorrect Input: Enter the Integer Value Next to the Desired Resolution\n"
        )
        format_choice(formats)
    return formats[choice - 1]
