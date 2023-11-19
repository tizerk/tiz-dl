import math
from pytube import YouTube
from video import *
from audio import *


def main():
    link = YouTube(input("Enter YouTube Video URL: "))
    print(f"Title: {link.title}")
    print(
        f"Uploaded by {link.author} on {link.publish_date.strftime("%b")} {link.publish_date.day}, {link.publish_date.year}"
    )
    print(f"Duration: {math.floor(link.length / 60)}min {link.length % 60}sec")
    choice = input("\n\nVideo or Audio? (v/a)")
    if choice == "v":
        video(link)
    elif choice == "a":
        audio(link)


main()
