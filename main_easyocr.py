import easyocr
import os
import time
start = time.time()

reader = easyocr.Reader(['en'], gpu=False)

path_to_media = r"./media"
for (dir, _, files) in os.walk(path_to_media):
    for file in files:
        path = os.path.join(dir, file)    
        image_path = path
        print(f"Image: {image_path}\n")
        result = reader.readtext(image_path, detail = 0)
        print(result)
        print('*********************************************')


print ('It took', time.time()-start, 'seconds.')