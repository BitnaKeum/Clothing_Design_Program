import cv2
import sys
import os 

UPLOAD_DIR = os.path.abspath("C:\\Users\\123\\Desktop\\Clothes_Design\\public\\uploads")
file_name = os.path.join(UPLOAD_DIR, sys.argv[1])

imageNDArray = cv2.imread(file_name)
imageH, imageW = imageNDArray.shape[:2]

resizeImageNDArray = cv2.resize(imageNDArray, (256, 256), interpolation=cv2.INTER_LINEAR)
output_file_name = os.path.join(UPLOAD_DIR, 're'+sys.argv[1])
cv2.imwrite(output_file_name, resizeImageNDArray)
