import yt_dlp


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
    ydl = yt_dlp.YoutubeDL({**ydl_opts, "format": resolution_choice(list_formats)})
    with ydl:
        ydl.download(url)


def resolution_choice(formats):
    print("Available Resolution Options:")
    count = 0
    for i in formats:
        count += 1
        print(f"{count}: {i["format_note"]}")
    choice = int(input("Select Desired Resolution: "))
    if 0 >= choice or choice > count:
        print("Incorrect Input: Enter the Integer Value Next to the Desired Resolution\n")
        resolution_choice(formats)
    else:
        return formats[choice]['format_id']
