import numpy as np, cv2


from common.utils import filter


image  = cv2.imread("images/filter_blur.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

## 샤프닝 마스크 원소지정
data1 = [0,-1,0,
         -1,5,-1,
         0,-1,0]
data2 = [[-1,-1,-1,
          -1,5,-1,
          -1,-1,-1]]

mask1 = np.array(data1, np.float32).reshape((3,3))
mask2 = np.array(data2, np.float32)

sharpen1 = filter(image,mask1)
sharpen2 = filter(image,mask2)
sharpen1 = cv2.convertScaleAbs(sharpen1)
sharpen2 = cv2.convertScaleAbs(sharpen2)
cv2.imshow("image",image)
cv2.imshow("sharpen1",sharpen1)
cv2.imshow("sharpen2",sharpen2)
cv2.waitKey(0)