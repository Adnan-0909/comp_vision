import cv2

img1 = cv2.imread('ASCII-art.png')
cv2.imshow('Original Image',img1)
cv2.waitKey(0)
cv2.imwrite('ASCII-art_original.jpg', img1)