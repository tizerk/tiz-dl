def video(link):
    print(f"Downloading {link.title} in video format...")
    link.streams.get_highest_resolution().download()
    print("Download Complete!")
