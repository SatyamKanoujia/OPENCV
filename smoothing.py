import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat',img)

average=cv.blur(img,(3,3))
cv.imshow('Average blur',average)

gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gauss)

median=cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

bilateral=cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)