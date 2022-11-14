import cv2

imgs = []
imgs.append( cv2.imread('go1.jpg') )
imgs.append( cv2.imread('tyoki1.jpg') )
imgs.append( cv2.imread('pa1.jpg') )

while True:
    for i in range(0,3):
        cv2.imshow("win",imgs[i])
        key = cv2.waitKey(50)
        if key==ord(' '):
            cv2.waitKey(0)
            cv2.destroyAllWindows()

