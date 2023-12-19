import yt_dlp
from yt_dlp.extractor import list_extractors
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

def url_check(url):
    ies = list_extractors()
    extractor = next(
        (ie.ie_key() for ie in ies if ie.suitable(url) and ie.ie_key() != "Generic"), None
    )
    if extractor:
        return True
    else:
        return False

def get_video_data(url, title, creator, upload_date):
    if url_check(url):
        with ydl:
            result = ydl.extract_info(url, download=False)
            if "title" in result:
                title.set(f'Title: {result["title"]}')     
            if "uploader" in result:
                creator.set(f'Creator: {result["uploader"]}')
            if "upload_date" in result:
                date = datetime.strptime(result["upload_date"], "%Y%m%d")
                upload_date.set(f"Upload Date: {date.strftime("%b")} {date.strftime("%d")}, {date.strftime("%Y")}")
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
            return(list(selected_formats.values()))
    else:
        title.set(f'Title: Not a Valid URL!!  Try Again.')
        creator.set(f'Creator: Not a Valid URL!!  Try Again.')
        upload_date.set(f'Upload Date: Not a Valid URL!!  Try Again.')
