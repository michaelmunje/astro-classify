import cv2
import numpy as np
import os

image_path = os.getcwd() + '/252342.jpg'
new_image_path = os.getcwd() + '/bbox/new_image.jpg'

# img = cv2.imread(image_path)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# _,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

# contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# cnt = contours[0]
# x,y,w,h = cv2.boundingRect(cnt)

# crop = img[y:y+h,x:x+w]
# cv2.imwrite(new_image_path,crop)

img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
cnts, hierarchy= cv2.findContours(gray.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for contour in cnts:
    print(cv2.boundingRect(contour))
cv2.drawContours(img,cnts,-1,(125,125,0),3 )
cv2.imwrite(new_image_path, img)
# cv2.imshow('contours',img)
# cv2.waitKey(0)  
# cv2.destroyAllWindows()
