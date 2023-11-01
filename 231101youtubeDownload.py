import cv2
# import pafy
import yt_dlp
import os

url = 'https://www.youtube.com/watch?v=ipyzW38sHg0'
# video = pafy.new(url)
# best = video.getbest(preftype='mp4')
with yt_dlp.YoutubeDL() as ydl:
    ydl.download([url])