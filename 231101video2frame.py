import cv2
# import pafy
import yt_dlp
import os

cap = cv2.VideoCapture('./data/아이로드 T10 블랙박스 FHD 30프레임 주행 영상 [ipyzW38sHg0].mp4')

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('frame_size =', frame_size)
print('frame_count =', frame_count)

frameNum = 0

dataPath = './dataset/'
os.makedirs(dataPath, exist_ok=True)

while True:   
    retval, frame = cap.read() # 프레임 캡처
    if not retval:
        break

    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
    if frameNum % 30 == 0:
        filename = os.path.join(dataPath, 'dataset' + str(frameNum) + '.jpg')
        # print(filename)
        cv2.imwrite(filename, frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
    frameNum += 1


if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()