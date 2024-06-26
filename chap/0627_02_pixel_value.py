import cv2

image = cv2.imread("images/j2.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise  Exception("영상파일 읽기 오류")


(x,y), (w,h) = (180,37), (15,10) # 좌표 는 x,y
roi_img = image[y:y+h, x:x+w] #행렬 접근은 y,x


print("[roi_img] =")
for row in roi_img: # 원소 순회 방식 출력
    for p in row:
        print("%4d" %p, end="") # 순회 요소 하나씪 출력
print()


cv2.rectangle(image, (x,y,w,h), 255, 1) # 관심영역에 사각형 표시
cv2.imshow("image", image)
cv2.waitKey(0)