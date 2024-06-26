import cv2
import numpy as np
import pytesseract

img = cv2.imread("images/recipt.jpg")

x,y,w,h =cv2.selectROI('img',img ,False)
if w and h:
    roi = img[y:y+h, x:x+w]
cv2.imshow('cropped', roi)
cv2.imwrite('cropped.jpg', roi)

#테서렉트를 이용해서 ocr을 진행하도록한다.
ocr = pytesseract.image_to_string('cropped.jpg', lang='kor')

print(ocr)

cv2.waitKey(0)
cv2.destroyAllWindows()