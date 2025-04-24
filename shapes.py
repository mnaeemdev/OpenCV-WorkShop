import cv2 
import numpy as np

img = np.zeros((512,512,3))
# cv2.imshow('Image',img)

# Rectangle
rectangle = cv2.rectangle(img, pt1=(100,100), pt2=(300,300), color=(255,0,0), thickness=-1)
cv2.imshow('Rectangle Image',rectangle)

# Circle
circle = cv2.circle(img, center=(100,300), radius=(70), color=(255,0,0), thickness=-1)
cv2.imshow('Rectangle Image',rectangle)

# Line
line = cv2.line(img, pt1=(0,0), pt2=(512,512), color=(55,45,0), thickness=2)
cv2.imshow('Line',line)

#Text
text= cv2.putText(img, org=(100,100), fontScale=4, color=(255,255,0), thickness=2, lineType=cv2.LINE_AA, text="Hello", fontFace=cv2.FONT_ITALIC)
cv2.imshow('Text',text)

cv2.waitKey(0)