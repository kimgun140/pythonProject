import numpy as np, cv2
#
# def preprocessing(coin_no):
#     fname = "images/coin/{0:02d}.png".foramt(coin_no)
#     image = cv2.imread(fname, cv2.IMREAD_COLOR)
#     if image is None: return  None, None
#
#
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     gray = cv2.GaussianBlur(gray, (7,7), 2,2)
#     flag = cv2.THRESH_BINARY + cv2.THRESH_OTSU
#
#     _, th_img = cv2.threshold(gray, 130, 255, flag)
#
#     mask = np.ones((3,3), np.uint8)
#     th_ing = cv2.morphologyEx(th_img, cv2.MORPH_OPEN, mask)
#     return image, th_img
#
#
# def find_coins(image):
#     results = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     contours = results[0] if int(cv2.__version__[0]) >= 4 else results[1]
#
#     # #반복문 방식
#     # circles = []
#     # for contour in contours:
#     #     center , radius = cv2.minEnclosingCircle(contour)
#     #     circle = (tuple(map(int, center)), int(radius))
#     #     if radius>35: circles.append(circle)
#     circles = [cv2.minEnclosingCircle(c) for c in contours] # 외각을 둘러 싸는 원 검출
#     circles = [(tuple(map(int,center)), int (radius))
#                for center, radius in circles if radius>25]
#     return  circles

from header.coin_preprocess import *


image, th_img = preprocessing(70)
if image is None: raise Exception("영상 파일 읽기 에러")

circles = find_coins(th_img)
for center, radius in circles:
    cv2.circle(image, center, radius, (0,255,0), 2)

cv2.imshow("preprocessed image", th_img)
cv2.imshow("coin image", image)
cv2.waitKey(0)