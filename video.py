import yt_dlp
import ffmpeg
import os

def video(url, ydl, ydl_opts):
    ydl_opts = {
        "quiet": True,
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
            if (resolution not in selected_formats):
                selected_formats[resolution] = fmt
    list_formats = list(selected_formats.values())
    chosen_resolution = resolution_choice(list_formats)
    if chosen_resolution <= 256:
        ydl = yt_dlp.YoutubeDL({**ydl_opts, "format": "worst"})    
    elif chosen_resolution <= 854:
        ydl = yt_dlp.YoutubeDL({**ydl_opts, "format": f"bestvideo[width<={chosen_resolution}]+worstaudio/best"})
    else:
        ydl = yt_dlp.YoutubeDL({**ydl_opts, "format": f"bestvideo[width<={chosen_resolution}]+bestaudio/best"})
    ydl.download(url)
    print("Download Complete!")

    result = ydl.extract_info(url, download=False)

    chosen_format = format_choice()

    input_file = f"{result["title"]}.{result["ext"]}"

    output_file = f"{result["title"]}{chosen_format}"
    if (chosen_format.lower() != f".{result["ext"]}"):
        ffmpeg.input(input_file).output(output_file).run()
        os.remove(input_file)
        print("Conversion Complete!")
    else:
        print("No Conversion Needed!")

def resolution_choice(formats):
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
    return formats[choice - 1]['width']

def format_choice():
    print("Available Format Options:")
    count = 0
    ext_formats = [".WEBM", ".MP4", ".MOV", ".WMV", ".FLV", ".AVI", ".MKV", ".3GP", ".M4A"]
    for i in ext_formats:
        count += 1
        print(f"{count}: {i}")
    try:
        choice = int(input("Select Desired Format: "))
    except ValueError:
        print(
            "Incorrect Input: Enter the Integer Value Next to the Desired Resolution\n"
        )
        format_choice(ext_formats)
    if 0 >= choice or choice > count:
        print(
            "Incorrect Input: Enter the Integer Value Next to the Desired Resolution\n"
        )
        format_choice(ext_formats)
    return ext_formats[choice - 1]
