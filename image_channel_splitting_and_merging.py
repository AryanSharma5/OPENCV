import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

img_path = '\\'.join(os.getcwd().split('\\')[:-2])+'\\IMAGE DATASET\\standard_test_images\\4.2.01.tiff'
#print(img_path)

namedWindow = 'IMAGE_READER'
cv2.namedWindow(namedWindow)

img = cv2.imread(img_path, 1)
r, g, b = cv2.split(img)

#print(img)

while True:

	cv2.imshow(namedWindow, img)
	cv2.imshow('red', r)
	cv2.imshow('green', g)
	cv2.imshow('blue', b)
	cv2.imshow('merged image', cv2.merge((r, g, b)))
	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()