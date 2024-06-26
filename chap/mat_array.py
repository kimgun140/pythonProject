import cv2

image = cv2.imread("images/matplot.jpg", cv2.IMREAD_COLOR)

if image is None: raise  Exception("영상파일 읽기 오류 발생")

x_axis = cv2.flip(image,0)
y_axis  = cv2.flip(image,1)
xy_axis = cv2.flip(image,-1)
rep_image = cv2.repeat(image,1,2)
trans_image = cv2.transpose(image)


## 각행렬을 영상으로 표시
titles = ["image","x_axis","y_axis","xy_axis", "rep_image", "trans_image"]
for title in titles:
    cv2.imshow(title,eval(title)) #문자열을 명령어로 만듦 - 행렬 변수로 적용
cv2.waitKey(0)