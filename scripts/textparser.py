from webhandler import*

# parses the input test and determines a valid command


app=["open","app","application"]
search=["google","bing","search","look up"]
url=["goto","go to","url", "website","web"]
mouseMove=["move","cursor","mouse"]
mouseScroll=["scroll","up","down"]
mouseClick=["click","press"]
mouseDoubleClick=["doubleclick","double click","double press","doublepress"]
keyboardType=["type", "input"]
keyboardHold=["hold"]
keyboardRelease=["release"]

'''
Types:
app
search
url
mouseMove
mouseScroll
mouseClick
mouseDoubleClick
keyboardType

keyboardHold
keyboardRelease


'''

# returns [command type, parameters]

def GetCommand(text):
    ans =[]
    inputArray = text.split()
    for x in range(len(inputArray)-1):
        v=inputArray[x]
        
        if v in search:
            a=["search", inputArray[x+1]]
            break
        elif v in url:
            a=["url", inputArray[x+1]]
            break
        elif v in app:
            a=["app", inputArray[x+1]]
            break
        elif v in mouseMove:
            a=["mouseMove", inputArray[x+1]]
            break
        elif v in mouseClick:
            a=["mouseClick", inputArray[x+1]]
            break
        elif v in mouseMove:
            a=["mouseDoubleClick", inputArray[x+1]]
            break
        elif v in keyboardType:
            a=["keyboardType", inputArray[x+1]]
            break
        elif v in keyboardHold:
            a=["keyboardHold", inputArray[x+1]]
            break
        elif v in keyboardRelease:
            a=["keyboardRelease", inputArray[x+1]]
            break
    return ans
            
            
        