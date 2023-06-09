from pytube import YouTube
from sys import argv

# Take the first argument(the link) when calling the script 
link = argv[1]
# the script should be called by Ytdownload.py "link" vid/audio

yt = YouTube(link)

print("Title is " + yt.title)
# check if i want audio only
if (argv[2] == "audio"):
    audio = yt.streams.get_audio_only()
    audio.download("C:/Users/MAlas/Music/Yt")
else:
    vid = yt.streams.get_highest_resolution()
    vid.download("C:/Users/MAlas/Videos/Youtube")