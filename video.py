import yt_dlp
import ffmpeg
import os

merge_needed = False

def video(url, ydl, ydl_opts):
    ydl_opts = {
        "quiet": True,
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)

    with ydl:
        result = ydl.extract_info(url, download=False)

    selected_formats = {}

    for fmt in result.get("formats", []):
        if (
            fmt.get("video_ext") != "None"
            and fmt.get("format_note") != "storyboard"
            and fmt.get("height") is not None
            and fmt.get("format_note") is not None
        ):
            resolution = f"{fmt['format_note']}"
            if (
                resolution not in selected_formats
                or fmt["tbr"] > selected_formats[resolution]["tbr"]
            ):
                selected_formats[resolution] = fmt

    list_formats = list(selected_formats.values())
    ydl = yt_dlp.YoutubeDL({**ydl_opts, "format": resolution_choice(list_formats), "outtmpl": "%(title)s-Video.%(ext)s",})
    result = ydl.extract_info(url, download=False)
    input_video = f"{result["title"]}-Video.{result["ext"]}"
    output_name = f"{result["title"]}.{result["ext"]}"
    with ydl:
        if merge_needed:
            ydl.download(url)
            ydl = yt_dlp.YoutubeDL({**ydl_opts, "format": "bestaudio/best", "outtmpl": "%(title)s-Audio.%(ext)s",})
            result = ydl.extract_info(url, download=False)
            input_audio = f"{result["title"]}-Audio.{result["ext"]}"
            ydl.download(url)
            ffmpeg.output(ffmpeg.input(input_video).video, ffmpeg.input(input_audio).audio, output_name, vcodec='copy', acodec='copy').run()
            os.remove(input_video)
            os.remove(input_audio)
        else:
            ydl.download(url)


def resolution_choice(formats):
    global merge_needed
    print("Available Resolution Options:")
    count = 0
    for i in formats:
        count += 1
        print(f"{count}: {i["format_note"]}")
    try:
        choice = int(input("Select Desired Resolution: "))
    except ValueError:
        print("Incorrect Input: Enter the Integer Value Next to the Desired Resolution\n")
        resolution_choice(formats)
    if 0 >= choice or choice > count:
        print("Incorrect Input: Enter the Integer Value Next to the Desired Resolution\n")
        resolution_choice(formats)
    elif choice > 5:
        merge_needed = True
    return formats[choice - 1]['format_id']
