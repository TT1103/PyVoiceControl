import subprocess,os


def HOCR(img,filename):

    subprocess.call(["tesseract", filename, "out" ,"hocr"])
    
    
    try: 
        os.remove(filename)
    except:
        return "fail2"
    
    ret ="fail"
    try:
        f=open("out.hocr","r")
        ret = f.readlines()
        f.close()
    except:
        return "fail3"
    
    try:
        os.remove("out.hocr")
    except:
        return "fail4"
     
    return ret
        
    