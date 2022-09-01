import cv2
import numpy as np
#Turn on the camera
vid = cv2.VideoCapture(0) 

while(True):
    #capture and grayscale filter for image
    ret, img = vid.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img,(5,5),0)

    #applying the cat face classifier
    catFaceCascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
    faces = catFaceCascade.detectMultiScale(blur, scaleFactor=1.1, minNeighbors=7, minSize=(65, 65))

    #drawing a rectangle in cat face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0),3)
    
    if len(faces) == 0:
        print("No faces found")

    #take a picture of the cat for test
    else:
        print("Number of faces detected: " + str(faces.shape[0]))
        #cv2.imwrite('img1.png',img)

    #show the camera image
    cv2.imshow('frame', img)

    #function to stop the algorithm
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #cv2.imwrite('img1.png',img)
        break

vid.release()
cv2.destroyAllWindows()
