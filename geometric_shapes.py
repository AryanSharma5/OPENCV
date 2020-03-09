import cv2
import numpy as np

'''
Image reading can be performed in 3 ways:
1. from the disk
2. from real time video frames
3. from stored video clips

Image reading from disk:    cv2.imread(image_path)

can pass one argument in imread function of opencv which 
signifies the color channels(RGB(1 default) or GRAYSCALE(0))
'''

def main():
	canvas = np.zeros((512,512,3), np.uint8)
	cv2.line(canvas , (0, 0), (512, 512), (0, 0, 255), 2)
	cv2.rectangle(canvas, (250, 50), (500, 200), (0, 0 , 255), 1)
	cv2.circle(canvas, (150, 350), 100, (0, 0, 255), 1)
	cv2.imshow('CANVAS', canvas)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()