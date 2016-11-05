import ocrhandler,mousehandler, VoiceInput, textparser,threading,webhandler,applicationhandler

audioQueue=[]

def GetContinuousAudio():
    audioQueue.append(VoiceInput.GetVoice())

    
def RunCommand(com):
    c = com[0]
    v=com[1]
    
    if c=="search":
        webhandler.GoogleSearch(v)
    elif c=="url":
        webhandler.OpenURL(v)
    elif c== "app":
        applicationhandler.OpenApp(v)
    elif c =="mouseMove":
        pass
    elif c=="mouseClick":
        mousehandler.Click()
    elif c=="mouseDoubleClick":
        mousehandler.DoubleClick()
    elif c=="mouseScroll":
        t =1
        if v=="up":
            t=-1
        mousehandler.Scroll(t)
    elif c== "keyboardType":
        keyboardhandler.TypeText(v)
    elif c=="keyboardHold":
        keyboardhandler.HoldKey(v)
    elif c=="keyboardRelease":
        keyboardhandler.ReleaseKey(v)
        
def main():
    '''
    t="View"
    filename = ".screenshot.png"
    img = ocrhandler.GetScreenShot(filename)
    s= ocrhandler.LocateText(img,t,filename)
        
    for x in s:
        print x
    
   
    mousehandler.Move(s[0][0], s[0][1])
        '''
    
    thread.start_new_thread(GetContinuousAudio,())
    
    
    if audioQueue:
        text = VoiceInput.GetText(audioQueue.pop(0)).lower()
        com = textparser.GetCommand(text)
        
        if len(com)>0:
            RunCommand(com)
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
        