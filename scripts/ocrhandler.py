import pyautogui,PIL, tesseracthandler,math, re

def GetScreenShot(filename):
    
    img =pyautogui.screenshot(filename)
    xSize,ySize = img.size
    #return img.resize((xSize/4, ySize/4));
    return img



#returnsarray of  x y cord of location,(empty array if not found)
def LocateText(img,text,filename):
    data = tesseracthandler.HOCR(img,filename)
    
    coords=[]
    #parse the data:
    data = " ".join(data).strip()
    data=re.findall(r"[\w']+", data)
    
    for i in range(len(data)):
        print data[i]
        if data[i] == "'ocrx_word'":
            w=data[i+15]
            if w== "strong":
                w=data[i+15]
            if w.lower() == text.lower():
                coords.append([math.fabs((int(data[i+5]) + int(data[i+7]))/4),math.fabs((int(data[i+6])+int(data[i+8])/4))  ])
        
            
        
    return coords
    
    

        
    