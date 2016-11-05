import ocrhandler
import mousehandler
import VoiceInput
import textparser
import thread
import webhandler
import applicationhandler
import threading
import keyboardhandler

audioQueue = []
textQueue = []
commandQueue=[]
'''
def GetContinuousAudio():
    audioQueue.append(VoiceInput.GetVoice())
'''


def GetContinuousText(audio):
    textQueue.append(VoiceInput.GetText(audio).lower())


def RunCommand(com):
    c = com[0]
    v = com[1]

    if c == "search":
        webhandler.GoogleSearch(v)
    elif c == "url":
        webhandler.OpenURL(v)
    elif c == "app":
        applicationhandler.OpenApp(v)
    elif c == "mouseMove":
        pass
    elif c == "mouseClick":
        mousehandler.Click()
    elif c == "mouseDoubleClick":
        mousehandler.DoubleClick()
    elif c == "mouseScroll":
        t = 1
        if v == "up":
            t = -1
        mousehandler.Scroll(t)
    elif c == "keyboardType":
        keyboardhandler.TypeText(v)
    elif c == "keyboardHold":
        keyboardhandler.HoldKey(v)
    elif c == "keyboardRelease":
        keyboardhandler.ReleaseKey(v)


        
def GetAudioThread():
    while True:
        audioQueue.append(VoiceInput.GetVoice())

def GetTextThread():
    while True:
        if audioQueue:
            textQueue.append(VoiceInput.GetText(audioQueue.pop(0)).lower())

def GetCommandThread():
    while True:
        if textQueue:
            com = textparser.GetCommand(textQueue.pop(0))
            if len(com)>0:
                commandQueue.append(com)
                
def RunCommandThread():
    while True:
        if commandQueue:
            RunCommand(commandQueue.pop(0))
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
    
    '''
    while (True):
        #thread.start_new_thread(GetContinuousAudio, ())
        audioQueue.append(VoiceInput.GetVoice())
        if audioQueue:
            #text = VoiceInput.GetText(audioQueue.pop(0)).lower()
            thread.start_new_thread(GetContinuousText, (audioQueue.pop(0),))
        if textQueue:

            com = textparser.GetCommand(textQueue.pop(0))
            if len(com) > 0:
                RunCommand(com)
'''
    
    
    #thread.start_new_thread(GetAudioThread(),())
    #thread.start_new_thread(GetTextThread(),())
    #thread.start_new_thread(GetCommandThread(),())
    #thread.start_new_thread(RunCommandThread(),())
    
    a = threading.Thread(target=GetAudioThread)
    b = threading.Thread(target=GetTextThread)
    c = threading.Thread(target=GetCommandThread)
    d = threading.Thread(target=RunCommandThread)
    
    a.start()
    b.start()
    c.start()
    d.start()



if __name__ == "__main__":
    main()
