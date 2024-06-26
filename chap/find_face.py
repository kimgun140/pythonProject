import cv2

win_title = 'rect'
image = cv2.imread("images/20231002_Jang_Won-young.jpg")
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")


eyes = eye_cascade.detectMultiScale(image,scaleFactor=1.3,minNeighbors=4,minSize=(10,10))
faces = face_cascade.detectMultiScale(image, scaleFactor=1.3,minNeighbors=4, minSize=(20,20))

while  True:
    if len(faces):
        for x, y, w, h in faces:
            cv2.rectangle(image, (x,y),(x+w,y+h), (255,255,255), 2, cv2.LINE_4)
    if len(eyes):
        for x,y,w,h in eyes:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2,cv2.LINE_4)
    cv2.imshow(win_title,image)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.imwrite('rectangle.jpg',image)
cv2.destroyAllWindows()