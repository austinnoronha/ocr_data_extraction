import time
start = time.time()

from PIL import Image 
from pytesseract import pytesseract 
import os
import numpy as np
import cv2 

  
# Defining paths to tesseract.exe 
# and the image we would be using 
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
path_to_media = r"./media"

# Import required packages
import cv2
import pytesseract
 
# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

 

for (dir, _, files) in os.walk(path_to_media):
    for file in files:
        path = os.path.join(dir, file)    
        
        image_path = path
        print(f"Image: {image_path}\n")
            
        # Read image from which text needs to be extracted
        img = cv2.imread(image_path)
        
        # Preprocessing the image starts
        
        # Convert the image to gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Performing OTSU threshold
        ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        
        # Specify structure shape and kernel size. 
        # Kernel size increases or decreases the area 
        # of the rectangle to be detected.
        # A smaller value like (10, 10) will detect 
        # each word instead of a sentence.
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
        
        # Applying dilation on the threshold image
        dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
        
        # Finding contours
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
                                                        cv2.CHAIN_APPROX_NONE)
        
        # Creating a copy of image
        im2 = img.copy()
    
        
        # Looping through the identified contours
        # Then rectangular part is cropped and passed on
        # to pytesseract for extracting text from it
        # Extracted text is then written into the text file
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            
            # Drawing a rectangle on copied image
            rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Cropping the text block for giving input to OCR
            cropped = im2[y:y + h, x:x + w]
            
            # Apply OCR on the cropped image
            text = pytesseract.image_to_string(cropped)
            print(text)         

        print('*********************************************')
            
            
# python 2
print ('It took', time.time()-start, 'seconds.')