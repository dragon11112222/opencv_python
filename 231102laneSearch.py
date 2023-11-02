import cv2
import numpy as np

# 비디오 영상 가져오기
filePath = 'data/아이로드 T10 블랙박스 FHD 30프레임 주행 영상 [ipyzW38sHg0].mp4'
cap = cv2.VideoCapture(filePath)

# 비디오 영상 크기 확인하기
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('frame_size =', frame_size)
print('frame_count =', frame_count)

def on_mouse(event, x, y, flags, param):
    print('x = {}, y = {}'.format(x, y))
# 207, 675 / 521, 476 / 803, 476 / 1120, 675

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

ROI_vertices = [
    (300, 678),
    (590, 413),
    (770, 413),
    (1170, 678)
]

# main
cv2.namedWindow('mask_window')
cv2.setMouseCallback('mask_window', on_mouse)

# 마스크를 생성


# while문으로 반복하면서 영상 한 프레임씩 가져오기


# 마스크를 적용해서 마스크 부분만 영상 가져오기(cv2.copyTo(, mask, ))


# 영상 출력
while True:   
    retval, frame = cap.read() # 프레임 캡처
    if not retval:
        break

    masked_img = region_of_interest(frame, np.array([ROI_vertices], np.int32))
    img_hsv = cv2.cvtColor(masked_img, cv2.COLOR_BGR2HSV)
    yLine_img = cv2.inRange(img_hsv, (18, 140, 0), (24, 255, 255))
    wLine_img = cv2.inRange(img_hsv, (0, 0, 135), (179, 24, 255))
    cv2.imshow('mask_window', frame)
    cv2.imshow('result', masked_img)
    cv2.imshow('yLine', yLine_img)
    cv2.imshow('wLine', wLine_img)
    
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break

