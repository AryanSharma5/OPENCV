import cv2
import numpy as np

def main():
	
	cap = cv2.VideoCapture(0)

	if cap.isOpened():
		isconnected, frame = cap.read()
	else:
		isconnected = False

	# low and high range for blue color
	#low = np.array([100,50,50])
	#high = np.array([140,255,255])


    # Red color
	low = np.array([0,50,100])
	high = np.array([100,255,255])	

	while isconnected:

		isconnected, frame = cap.read()
		# hsv format is used to detect color 
		# Default BGR format is not suitable for color tracking
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
		# Image mask is created
		# It is a binary array of 0(Black) and 255(White) as value.
		image_mask = cv2.inRange(hsv, low, high)

		# MAsked Video stream
		# output will contain masked video stream which will show only blue color objects.
		output = cv2.bitwise_and(frame, frame, mask = image_mask)

		cv2.imshow('OUTPUT MASKED VIDEO STREAM', output)
		cv2.imshow('MASKED IMAGE', image_mask)
		cv2.imshow('ORIGINAL VIDEO STREAM', frame)

		if cv2.waitKey(1) == 27:
			break
	cv2.destroyAllWindows()
	cap.release()


if __name__ == '__main__':
	main()