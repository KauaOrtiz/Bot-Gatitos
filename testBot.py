import cv2

vid = cv2.VideoCapture(0)

while(True):
    ret, img = vid.read()
    cv2.imshow('frame', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('img1.png',img)
        break

vid.release()
cv2.destroyAllWindows()
