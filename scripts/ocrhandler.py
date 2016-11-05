import pyautogui,PIL, tesseracthandler,math

def GetScreenShot(filename):
    
    img =pyautogui.screenshot(filename)
    xSize,ySize = img.size
    return img.resize((xSize/4, ySize/4));
    



#returns x y cord of location,(-1,-1 if not found)
def LocateText(img,text,filename):
    data = tesseracthandler.HOCR(img,filename)
    return data
    
    

#a b are [x y] 
def ContainsText(img,text,a,b):
    tmp=img.crop((a[0], a[1], b[0], b[1]))
    #return text in pytesseract.image_to_string(tmp).lower
    
    
    
    