def audio(link):
    print(f"Downloading {link.title} in audio format...")
    link.streams.get_audio_only().download()
    print("Download Complete!")
