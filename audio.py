import yt_dlp
import ffmpeg

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

    match format:
        case ".MP3":
            output_file = f"{result["title"]}.mp3"
            ffmpeg.input(input_file).output(output_file).run()
        case ".AAC":
            output_file = f"{result["title"]}.aac"
            ffmpeg.input(input_file).output(output_file).run()
        case ".FLAC":
            output_file = f"{result["title"]}.flac"
            ffmpeg.input(input_file).output(output_file).run()
        case ".WAV":
            output_file = f"{result["title"]}.wav"
            ffmpeg.input(input_file).output(output_file).run()
        case ".MOV":
            output_file = f"{result["title"]}.mov"
            ffmpeg.input(input_file).output(output_file).run()
        case ".OGG":
            output_file = f"{result["title"]}.ogg"
            ffmpeg.input(input_file).output(output_file).run()
        case ".OPUS":
            output_file = f"{result["title"]}.opus"
            ffmpeg.output(ffmpeg.input(input_file), output_file, acodec='copy').run()
        case ".AIFF":
            output_file = f"{result["title"]}.aiff"
            ffmpeg.input(input_file).output(output_file).run()
        case ".M4A":
            output_file = f"{result["title"]}.m4a"
            ffmpeg.input(input_file).output(output_file).run()
    print("Download Complete!")


def format_choice():
    print("Available Format Options:")
    count = 0
    formats = [".MP3", ".AAC", ".FLAC", ".WAV", ".WEBM", ".MOV", ".OGG", ".OPUS", ".AIFF", ".M4A"]
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
