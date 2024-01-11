import time
start = time.time()

from PIL import Image 
from pytesseract import pytesseract 
import os
import cv2 
import numpy as np

# Defining paths to tesseract.exe 
# and the image we would be using 
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
path_to_media = r"./media"
pytesseract.tesseract_cmd = path_to_tesseract 

for (dir, _, files) in os.walk(path_to_media):
    for file in files:
        path = os.path.join(dir, file)    
        
        image_path = path
        print(f"Image: {image_path}\n")
                
        img = cv2.imread(image_path)
        
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(img, config=custom_config)
        print(text)         

        print('*********************************************')
        
        

# python 2
print ('It took', time.time()-start, 'seconds.')