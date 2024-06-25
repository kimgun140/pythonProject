import cv2
import numpy as np


def onChange(value): # 트랙바 값과 영상 화소값 차분
    global image ,title

    add_value = value - int(image[0][0])
    image[:] = image + add_value
    cv2.imshow(title, image)


def onMouse(event,x,y,flags,param): #마우스 콜백함수
    global image, bar_name

    if event == cv2.EVENT_RBUTTONDOWN:
        print(image[0][0])
        if(image[0][0] < 246): image[:] = image + 10
        cv2.setTrackbarPos(bar_name, title, image[0][0]) # 트랙바 위치변경
        cv2.imshow(title, image)

    elif event == cv2.EVENT_LBUTTONDOWN:
        print(image[0][0])
        if(image[0][0] >= 10): image[:] = image -10
        cv2.setTrackbarPos(bar_name, title, image[0][0]) # 트랙바 위치변경
        cv2.imshow(title, image)

image = np.zeros((300,500), np.uint8)


title = "Trackbar & Mouse Event" #윈도우 이름
bar_name = "Brightness" #트랙바 이름
cv2.imshow(title, image)

cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
