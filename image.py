import cv2

#Creat a CascadeClassifier Object
faceDetect = cv2.CascadeClassifier('/home/oswalgaurav/PycharmProjects/numpy/haarcascade_frontalface_default.xml')

#Reading the image
img = cv2.imread("/home/oswalgaurav/Downloads/messi.jpg",1)

#reading the image as grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#search the coordinates of the face in the image
faces = faceDetect.detectMultiScale(gray_img, 1.05, 5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
   img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 50)

resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))


cv2.imshow("Gray",resized)

cv2.waitKey(0)

cv2.destroyAllWindows()