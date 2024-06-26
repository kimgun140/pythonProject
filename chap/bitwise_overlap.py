import numpy as np, cv2

image = cv2.imread("images/read_color.jpg", cv2.IMREAD_COLOR)
logo = cv2.imread("images/OpenCV_Logo.png", cv2.IMREAD_COLOR)
if image is None or logo is None: raise Exception("영상파일 읽기 오류")
logo = cv2.resize(logo, dsize=(200,150), interpolation=cv2.INTER_LINEAR)
masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2],fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

(H,W),(h,w) = image.shape[:2], logo.shape[:2]
x, y = (W-w)//2, (H-h)//2
roi = image[y:y+h, x:x+w]

# 행렬 논리곱과 마스킹을 이용한 관심 영역 복사
foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)
background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)

dst = cv2.add(background, foreground)
image[y:y+h, x:x+w] = dst

# #flip 시작
# x_axis = cv2.flip(image,0)
# y_axis  = cv2.flip(image,1)
# xy_axis = cv2.flip(image,-1)
# rep_image = cv2.repeat(image,1,2)
# trans_image = cv2.transpose(image)
#
#
# ## 각행렬을 영상으로 표시
# titles = ["image","x_axis","y_axis","xy_axis", "rep_image", "trans_image"]
# for title in titles:
#     cv2.imshow(title,eval(title)) #문자열을 명령어로 만듦 - 행렬 변수로 적용
# cv2.waitKey(0)
# #flip 끝

# 원그리기 시작
orange, blue, cyan   = (0,165,255),(255,0,0),(255,255,0)
white, black = (255,255,255),(0,0,0)
# image = np.full((300,500,3), white, np.uint8) #컬러 영상 생성 및 초기화
center = (image.shape[1]//2, image.shape[0]//2)     #영상 중심 좌표 - 역순 구성
pt1, pt2 = (300, 50),(100,220)
cv2.circle(image, center, 100, blue)        #원그리기
cv2.circle(image, pt1, 50, orange, 2)
cv2.circle(image,pt2,70,cyan, -1)
# 원그리기 끝


bgr = cv2.split(image)
#
print("bgr 자료형:", type(bgr),type(bgr[0]), type(bgr[0][0][0]))
print("bgr 원소 개수:" ,len(bgr))

##

cv2.imshow("image", image)

cv2.imshow("Blue channel", bgr[0])
cv2.imshow("Green channel", bgr[1])
cv2.imshow("Red channel", bgr[2])

cv2.imshow("background", background); cv2.imshow("foreground", foreground)
cv2.imshow("dst", dst); cv2.imshow("image",image)
cv2.waitKey()