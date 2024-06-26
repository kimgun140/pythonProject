import cv2

rate  = 15
win_title = 'rect'
image = cv2.imread("images/j2.jpg")
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
# eye_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")


# eyes = eye_cascade.detectMultiScale(image,scaleFactor=1.3,minNeighbors=4,minSize=(10,10))
faces = face_cascade.detectMultiScale(image, scaleFactor=1.3,minNeighbors=4, minSize=(20,20))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
while  True:
    if len(faces):
        for x, y, w, h in faces:
            roi_gray = gray[y: y+h, x+w] # 모자이크 부분
            roi_color = image[y: y+h, x+w]
            roi = cv2.resize(roi_color, (w // rate,h//rate))
            roi = cv2.resize(roi,(w,h),interpolation=cv2.INTER_AREA)
            image[y:y+h, x:x+w] = roi
    cv2.imshow(win_title,image)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('mosaic2.jpg', image)
cv2.destroyAllWindows()