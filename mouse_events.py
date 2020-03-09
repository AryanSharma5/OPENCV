import numpy as np
import cv2
'''
['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON',
 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN',
 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 
 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
'''
windowName = 'Paint'
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(windowName)

def callback_MouseEvent(event, x, y):
	if event == cv2.EVENT_MOUSEWHEEL:
		cv2.circle(img, (x, y), 30, (0, 0, 255), -1)

cv2.setMouseCallback(windowName, callback_MouseEvent)
	
def main():

	while True:
		cv2.imshow(windowName, img)
		if cv2.waitKey() == 27:
			break

	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()