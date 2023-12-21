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
            ydl.download(url)
            print("Download Complete!")
        elif chosen_format == "WEBM":
            ydl = yt_dlp.YoutubeDL(
                {
                    **ydl_opts,
                    "format": f"bestvideo[height<={chosen_resolution}]+bestaudio/best",
                }
            )
            ydl.download(url)
            print("Download Complete!")
        elif chosen_format == "MP4 (VP9)":
            ydl = yt_dlp.YoutubeDL(
                {
                    **ydl_opts,
                    "format": f"bestvideo[height<={chosen_resolution}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                }
            )
            ydl.download(url)
            print("Download Complete!")
        elif chosen_format == "MP4 (H.264)" and chosen_resolution <= 1080:
            ydl = yt_dlp.YoutubeDL(
                {
                    **ydl_opts,
                    "format": f"bestvideo[height<={chosen_resolution}][ext=mp4][vcodec^=avc]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                }
            )
            ydl.download(url)
            print("Download Complete!")
        elif chosen_format == "MP4 (H.264)" and chosen_resolution > 1080:
            ydl = yt_dlp.YoutubeDL(
                {
                    **ydl_opts,
                    "format": f"bestvideo[height<={chosen_resolution}]+bestaudio/best",
                }
            )
            ydl.download(url)
            print("Download Complete!")
            conversion(result, "mp4")
        else:
            ydl = yt_dlp.YoutubeDL(
                {
                    **ydl_opts,
                    "format": f"bestvideo[height<={chosen_resolution}]+bestaudio/best",
                }
            )
            ydl.download(url)
            print("Download Complete!")
            conversion(result, chosen_format)


def conversion(info, output_format):
    if output_format == "MKV":
        input_file = f"{info["title"]}.MKV"
    else:
        input_file = f"{info["title"]}.{info["ext"]}"

    output_file = f"{info["title"]}.{output_format}"
    ffmpeg.input(input_file).output(output_file).run()
    os.remove(input_file)
    print("Conversion Complete!")
