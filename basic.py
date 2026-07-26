import cv2 as cv 

img = cv.imread('photos/park.jpg')
cv.imshow('park',img)

# Converting to Grayscale
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('Gray',gray)

# blur
blur = cv.GaussianBlur(img, (7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge cascade
canny = cv.Canny(blur, 125,175)
cv.imshow('Canny',canny)

# Dialating the image
dilated = cv.dilate(canny, (3,3),iterations = 3)
cv.imshow('Dilated',dilated)

#Erodng 
eroded = cv.erode(dilated , (3,3),iterations=3)
cv.imshow('Eroded',eroded)

# Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)