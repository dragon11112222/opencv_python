import cv2
# import pafy
import yt_dlp
# 참조 : https://www.codeit.kr/community/questions/UXVlc3Rpb246NjQ5MjQ4ZTc3ZWQwNzAzMGIxNDVjNjNh
# import os

url = 'https://www.youtube.com/watch?v=ipyzW38sHg0'
# video = pafy.new(url)
# best = video.getbest(preftype='mp4')
with yt_dlp.YoutubeDL() as ydl:
    ydl.download([url])