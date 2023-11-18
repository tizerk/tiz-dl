from pytube import YouTube


def main():
    video = YouTube(input("Enter YouTube Video URL: "))
    choice = input("Video or Audio? (v/a)")
    if choice == "v":
        print(f"Downloading {video.title} in video format...")
        video.streams.get_highest_resolution().download()
        print("Download Complete!")
    elif choice == "a":
        print(f"Downloading {video.title} in audio format...")
        video.streams.get_audio_only().download()
        print("Download Complete!")


main()
