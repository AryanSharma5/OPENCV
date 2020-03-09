import cv2
import os

storage = os.path.dirname(os.path.abspath(__file__))

folder_name = 'VIDEO_STORAGE/'

def main():
	cv2.namedWindow('LIVE VIDEO CAPTURING')

	target = os.path.join(storage,folder_name)

	if not os.path.isdir(target):
		os.mkdir(target)

	filename = target + 'op.avi'

	'''
	codec :----> coding encoding :---->  THEY ARE FOUR CHARACTER CODES AMONG THEM XVID IS MAINLY USED
	OVER THE INTERNET ALSO
	'''



	codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
	framerate = 30
	resolution = (640,480)

	videofileoutput = cv2.VideoWriter(filename, codec, framerate, resolution)

	cap = cv2.VideoCapture(0)
	if cap.isOpened():
		isconnected, frame = cap.read()
	else:
		isconnected = True

	while isconnected:

		isconnected, frame = cap.read()
		
		videofileoutput.write(frame)

		cv2.imshow('LIVE VIDEO CAPTURING', frame)

		if cv2.waitKey(1) == 27:
			break

	cv2.destroyAllWindows()
	videofileoutput.release()
	cap.release()


if __name__ == '__main__':
	main()
