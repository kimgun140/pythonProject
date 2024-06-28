import cv2
import numpy as np

image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise  Exception("영살파일읽기 ㅇ류")


##영상 합성 방법\
## 사진 크기가 같아야하네

alpha, beta = 0.6 , 0.7
add_img1 = cv2.add(image1,image2)
add_img2 = cv2.add(image1 * alpha, image2 * beta)
add_img = np.clip(add_img2,0,255).astype('uint8')
add_img3 = cv2.addWeighted(image1,alpha,image2, beta,0)

titles = ['image1', 'image2', 'add_img1','add_img2', 'add_img3']
for t in titles: cv2.imshow(t,eval(t))

cv2.waitKey(0)