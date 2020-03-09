'''
CAPTURING LIVE VIDEO : 

import cv2

def main():
	
	windowname = 'LIVE VIDEO'
	cv2.namedWindow(windowname)
	cap = cv2.VideoCapture(0)

	if cap.isOpened():
		isconnected, frame = cap.read()
	else:
		isconnected = False

	while isconnected:

		isconnected, frame = cap.read()
		cv2.imshow(windowname, frame)

		if cv2.waitKey(1) == 27:
			break

	cv2.destroyAllWindows()

	cap.release()


if __name__ == '__main__':
	main()
'''


import cv2

def main():
	cv2.namedWindow('LIVE VIDEO')
	cap = cv2.VideoCapture(0)

	if cap.isOpened():
		isconnected, frame = cap.read()
	else:
		isconnected = False

	while isconnected:

		isconnected, frame = cap.read()

		# processing live video : Converting into GRAY SCALE VIDEO.

		grayVIDEO = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		print(f'WIDTH : {cap.get(3)}')
		print(f'HEIGHT : {cap.get(4)}')

		cv2.imshow('GRAY SCALE VIDEO', grayVIDEO)
		cv2.imshow('LIVE VIDEO', frame)

		if cv2.waitKey(1) == 27:
			break

	cv2.destroyAllWindows()

	cap.release()

if __name__ == '__main__':
	main()

'''
WE CAN GET THE RESOLUTION OF THE WEBCAM USING
CAP.GET(3) AND      ------->   USED TO DISPLAY WIDTH OF THE VIDEO
CAP.GET(4)          ------->   USED TO DISPLAY HEIGHT OF THE VIDEO


WE CAN SET THE RESOLUTION OF THE WEBCAM USING CAMMERA OJBECT (CAP IN THE ABOVE CODE) 
USING 
CAP.SET(3, NEW_WIDTH) AND      ------->  3 USED TO DETECT THE WIDTH PROPERTY OF THE WEBCAM
CAP.SET(4, NEW_HEIGHT)         ------->  4 USED TO DETECT THE HEIGHT PROPERTY OF THE WEBCAM 
'''


