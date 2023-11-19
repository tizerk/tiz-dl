import yt_dlp


def audio(url, ydl, ydl_opts):
    ydl_opts = {
        "quiet": True,
        "format": "bestaudio/best",
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)

    ydl.download(url)
