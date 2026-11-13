import cv2
img = cv2.imread('img1.png')
resizing = cv2.resize(img, (800, 600))
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurring = cv2.GaussianBlur(img, (5, 5), 0)
edges = cv2.Canny(img, 0, 0)

# cv2.imshow('Resizing',resizing)
# cv2.imshow('Grey',grey)
# cv2.imshow('Blurring',blurring)
cv2.imshow('Edges',edges)
cv2.imshow('ASCII-art_edges.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()