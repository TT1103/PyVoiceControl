import pyautogui,PIL, tesseracthandler,math, re

def GetScreenShot(filename):
    
    img =pyautogui.screenshot(filename)
    #xSize,ySize = img.size
    #return img.resize((xSize/4, ySize/4));
    return img



#returnsarray of  x y cord of location,(empty array if not found)
def LocateText(img,text,filename):
    data = tesseracthandler.HOCR(img,filename)
    text=text.lower()
    coords=[]
    #parse the data:
    
    textSplit = text.strip().split()
    
    data= "".join(data).lower()

    for i in xrange(len(data)):
        s=""
        c=[]
        if data[i:i+9] == "ocrx_word":
            i+=8
            tmp=""
            while data[i:i+4] !="bbox":
                i+=1
            i+=4
            while data[i] !=";":
                tmp+=data[i]
                i+=1
            c=tmp.strip().split()
            
            
            while data[i] !=">":
                i+=1
            i+=1
            while data[i] !="<":
                s+=data[i] 
                i+=1
            
        if text in s or s in textSplit and len(c)==4:
             coords.append([math.fabs((int(c[0]) + int(c[2]))/4), math.fabs((int(c[1])+ int(c[3]))/4)])
        
        
    
            
        
    return coords
    
    

        
    