import yt_dlp
import ffmpeg
import os

def download_video(url, chosen_resolution, chosen_format):
    ydl_opts = {
        "quiet": True,
        "outtmpl": "%(title)s.%(ext)s",
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    with ydl:
        result = ydl.extract_info(url, download=False)
        if chosen_resolution <= 144:
            ydl = yt_dlp.YoutubeDL({**ydl_opts, "format": "worst"})    
        elif chosen_resolution <= 480:
            ydl = yt_dlp.YoutubeDL({**ydl_opts, "format": f"bestvideo[height<={chosen_resolution}]+worstaudio/best"})
        else:
            print(f"Should be downloading at {chosen_resolution} quality")
            ydl = yt_dlp.YoutubeDL({**ydl_opts, "format": f"bestvideo[height<={chosen_resolution}]+bestaudio/best"})
        ydl.download(url)
        print("Download Complete!")

    input_file = f"{result["title"]}.{result["ext"]}"

    output_file = f"{result["title"]}{chosen_format}"
    if (chosen_format.lower() != f".{result["ext"]}"):
        ffmpeg.input(input_file).output(output_file).run()
        os.remove(input_file)
        print("Conversion Complete!")
    else:
        print("No Conversion Needed!")
