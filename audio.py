import yt_dlp
import ffmpeg
import os

def download_audio(url, format):
    ydl_opts = {
        "quiet": True,
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s"
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    result = ydl.extract_info(url, download=False)

    ydl.download(url)
    input_file = f"{result["title"]}.{result["ext"]}"

    output_file = f"{result["title"]}.{format}"
    if (format != "WEBM (OPUS)"):
        ffmpeg.input(input_file).output(output_file).run()
        os.remove(input_file)
    print("Download Complete!")
