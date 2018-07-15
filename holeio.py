import cv2
import pyautogui
import time
import datetime
import numpy as np

waited = False
print("Capturing was started")
while(True):
    image = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    saveimg = img
    cv2.imwrite('temp_screen.png', img)
    img = cv2.imread('temp_screen.png',0)
    img2 = img.copy()
    template = cv2.imread('Screenshot_39.png',0)
    w, h = template.shape[::-1]
    img = img2.copy()
    method = eval('cv2.TM_SQDIFF_NORMED')
    
    res = cv2.matchTemplate(img,template,method)    
    #print(cv2.minMaxLoc(res))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if (min_val > 0.12): # the coef to detect the image
        #print("NOT FOUND")
        waited = True
        time.sleep(1)

    else:
        if(not waited):
            time.sleep(1)
        else:
            print("'Continue' has been found")
            
            top_left = min_loc
            bottom_right = ((top_left[0] + w, top_left[1] + h))            
            
            image_name = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + '.png'        
            print(image_name)
            cv2.imwrite(image_name, saveimg)
            print("Screenshot has been saved")
            waited = False
            time.sleep(1)        
