import cv2
import numpy as np

def emptyfunc():
	pass

def main():
	#It will create black canvas window
	img = np.zeros((512, 512, 3), np.uint8)
	
	#Creating a named window 'color palette'
	namedWindow = 'COLOR PALETTE'
	cv2.namedWindow(namedWindow)

	#Creating Trackbars using OpenCV

	cv2.createTrackbar('B', namedWindow, 0, 255, emptyfunc)
	cv2.createTrackbar('G', namedWindow, 0, 255, emptyfunc)
	cv2.createTrackbar('R', namedWindow, 0, 255, emptyfunc)

	#This loop will show the window continously till the ESC(27 as its key code) key is not pressed.
	while True:
		cv2.imshow(namedWindow, img)
		if cv2.waitKey(1) == 27:
			break

		Blue = cv2.getTrackbarPos('B', namedWindow)
		Green = cv2.getTrackbarPos('G', namedWindow)
		Red = cv2.getTrackbarPos('R', namedWindow)

		img[:] = [Blue, Green, Red]

	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()