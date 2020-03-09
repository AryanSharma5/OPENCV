def main():
    
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    img_path1 = 'C:\\Users\\aryan\\Desktop\\IMAGE DATASET\\standard_test_images\\4.2.01.tiff'
    img_path2 = 'C:\\Users\\aryan\\Desktop\\IMAGE DATASET\\standard_test_images\\4.2.03.tiff'
    
    
    # LOGICAL OPERATIONS : 
    
    def logical_operations(img_path1, img_path2):

        print('-------------- LOGICAL OPERATIONS ON THE IMAGE ----------------')
        
        img1 = cv2.imread(img_path1, 1)
        img2 = cv2.imread(img_path2, 1)
        	
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        
        operations = [img1, img2, cv2.bitwise_and(img1, img2), cv2.bitwise_not(img1), 
        		      cv2.bitwise_or(img1, img2),cv2.bitwise_xor(img1, img2)]
        labels = ['ORIGINAL IMG1', 'ORIGINAL IMG2', 'BITWISE AND', 'BITWISE NOT', 'BITWISE OR',\
        		  'BITWISE XOR']
        
        for i in range(1, 7):
            plt.subplot(2, 3, i)
            plt.imshow(operations[i-1])
            plt.title(labels[i-1])
            plt.xticks = [[]] 
            plt.yticks = [[]]
            plt.tight_layout()
        
        plt.show()
    
    def negative_image(img_path):
    
        # NEGATIVE OF AN IMAGE :
        
        print('--------------- NEGATIVE OPERATION ON THE IMAGE ---------------')
        
        img = cv2.imread(img_path, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        neg_img = 255 - img
        
        IMAGES = [img, neg_img]
        LABELS = ['ORIGINAL IMAGE', 'NEGATIVE OF THE IMAGE']
        for i in range(1,3):
            plt.subplot(1, 2, i)
            plt.imshow(IMAGES[i-1])
            plt.title(LABELS[i-1])
            plt.tight_layout()
            
        plt.show()
    
    def shifting(img_path):
    
        # SHIFTING AN IMAGE (TRANSLATING) :
        # SHIFTING OPERATION COMES UNDER GEOMETRIC TRANSFORMATIONS
        # AND GEOMETRIC TRANSFORMATIONS ARE TYPE OF AFFINE TRANSFOMRTAIONS.
        #               
        #           AFFINE TRANSFORMATIONS
        #                   |
        #           GEOMETRIC TRANSFORMATIONS
        #                   |
        #           SHIFTING OR TRANSLATING
    
        print('--------------- SHIFTING IMAGE -------------------')
        
        img = cv2.imread(img_path, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        rows, cols, channels = img.shape
        
        Transformation_mat = np.float32([[1, 0, 50], [0, 1, -50]])
        
        output = cv2.warpAffine(img, Transformation_mat, (rows, cols))
        
        IMAGES = [img, output]
        LABELS = ['ORIGINAL IMAGE', 'SHIFTED IMAGE']
        
        for i in range(1, 3):
            plt.subplot(1, 2, i)
            plt.imshow(IMAGES[i-1])
            plt.title(LABELS[i-1])
            plt.tight_layout()
            
        plt.show()
        
    logical_operations(img_path1, img_path2)
    negative_image(img_path1)
    shifting(img_path1)
        
if __name__ == '__main__':
    main()