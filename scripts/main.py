import ocrhandler
import mousehandler
import VoiceInput
import textparser
import thread
import webhandler
import applicationhandler

audioQueue = []
textQueue = []

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


if __name__ == "__main__":
    main()
