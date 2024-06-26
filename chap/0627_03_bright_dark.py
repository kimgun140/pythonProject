import cv2

image = cv2.imread("images/j2.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise  Exception("영상 파일 오류")


##opencv 함수 이용 (saturation방식)
dst1 = cv2.add(image, 100)
dst2 = cv2.subtract(image,100)


##numpy.ndarray이용 (modulo 방식)
dst3 = image +100
dst4 = image -100


cv2.imshow("original image", image)
cv2.imshow("dst1- bright:opencv", dst1)
cv2.imshow("dst2- dark:opencv", dst2)
cv2.imshow("dst3- bright:numpy", dst3)
cv2.imshow("dst4- dark:numpy", dst4)
cv2.waitKey(0)