# 동영상 파일 읽기

import cv2
# from common.utils import put_string
def put_string(frame, text, pt, value=None, color=(120, 200, 90)) :
    text = str(text) + str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2) # 그림자 효과
    cv2.putText(frame, text, pt   , font, 0.7, color, 2) # 작성 문자




capture = cv2.VideoCapture(0)
if not capture.isOpened(): raise Exception("동영상파일 개방 안됨")

frame_rate = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000 / frame_rate)
frame_cnt = 0

while True:
    ret, frame = capture.read()
    if not ret or cv2.waitKey(delay) >=0 :break

    blue, green , red = cv2.split(frame)
    frame_cnt +=1

    if 100 <= frame_cnt < 200: cv2.add(blue,100,blue)
    elif 200<= frame_cnt < 300: cv2.add(green, 100, green)
    elif 300 <= frame_cnt < 400: cv2.add(red, 100 ,red)

    frame = cv2.merge([blue, green, red])
    put_string(frame, 'frame_cnt', (20,30), frame_cnt)
    cv2.imshow("Read Video File", frame)

capture.release()