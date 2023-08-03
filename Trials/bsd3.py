import youtube_dl
import os
import sys
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

with ydl:
    result = ydl.extract_info(
        'https://www.youtube.com/watch?v=cjVQ36NhbMk',
        download=False # We just want to extract the info
    )


    # Just a video
    video = result

#print(video)
text_file = open("Output.txt", "w")
text_file.write(str(video))
text_file.close()
