import time
start = time.time()

from PIL import Image 
from pytesseract import pytesseract 
import os
  
# Defining paths to tesseract.exe 
# and the image we would be using 
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
path_to_media = r"./media"
for (dir, _, files) in os.walk(path_to_media):
    for file in files:
        path = os.path.join(dir, file)    
        
        image_path = path
        print(f"Image: {image_path}\n")
        # Opening the image & storing it in an image object 
        img = Image.open(image_path) 
        
        # Providing the tesseract executable 
        # location to pytesseract library 
        pytesseract.tesseract_cmd = path_to_tesseract 
        
        # Passing the image object to image_to_string() function 
        # This function will extract the text from the image 
        text = pytesseract.image_to_string(img) 
        
        # Displaying the extracted text 
        print(text[:-1])
        
        print('*********************************************')

# python 2
print ('It took', time.time()-start, 'seconds.')