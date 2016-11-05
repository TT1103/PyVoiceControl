import ocrhandler

def main():
    t="shell"
    filename = ".screenshot.png"
    img = ocrhandler.GetScreenShot(filename)
    s= ocrhandler.LocateText(img,t,filename)
        
    print len(s)
        
        
    
    
    
if __name__ == "__main__":
    main()
        