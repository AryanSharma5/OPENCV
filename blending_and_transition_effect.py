import os
import numpy as np
import cv2
import time


#Following code blends two images and gives a smooth transition effect.

'''

def main():
	path = 'C:\\Users\\aryan\\Desktop\\IMAGE DATASET\\standard_test_images\\'

	img1 = cv2.imread(path + 'woman_blonde.tif', 1)
	img2 = cv2.imread(path + 'lena_color_512.tif', 1)
	
	for i in np.linspace(0, 1, 50):
		alpha = i
		beta = 1 - alpha
		gamma = 0
		blend = cv2.addWeighted(img1, alpha, img2, beta, gamma)
		cv2.imshow('BLENDED_IMAGE_TRANSITION', blend)
		time.sleep(0.1)
		if cv2.waitKey(1) == 27:
			break
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()'''

#Following code blends and make transition effect using interactive trackbars of opencv.

'''
def empty_func():
	pass

def main():
	path = 'C:\\Users\\aryan\\Desktop\\IMAGE DATASET\\standard_test_images\\'

	img1 = cv2.imread(path + 'woman_blonde.tif', 1)
	img2 = cv2.imread(path + 'lena_color_512.tif', 1)

	alpha = 0.5
	beta = 0.5
	gamma = 0

	blend = cv2.addWeighted(img1, alpha, img2, beta, gamma)

	window_name = 'BLENDED_IMAGE_TRANSITION'
	cv2.namedWindow(window_name)

	cv2.createTrackbar('ALPHA', window_name, 0, 100, empty_func)

	while True:
		cv2.imshow(window_name, blend)
		if cv2.waitKey(1) == 27:
			break
		alpha = cv2.getTrackbarPos('ALPHA', window_name) / 100
		beta = 1 - alpha
		gamma = 0
		blend = cv2.addWeighted(img1, alpha, img2, beta, gamma)

	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()
'''