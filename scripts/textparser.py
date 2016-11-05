from webhandler import*

# parses the input test and determines a valid command


app = ["app", "application","launch"]
search = ["google", "bing", "search", "look up"]
url = ["open", "goto", "go to", "url", "website", "web"]
mouseMove = ["move", "cursor"]
mouseScroll = ["scroll", "up", "down"]
mouseClick = ["click", "press"]
mouseDoubleClick = ["doublepress",
                    "doubleclick","double"]
keyboardType = ["type", "input"]
keyboardHold = ["hold"]
keyboardRelease = ["release","unhold"]

music = ["play music"]

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
    a = []
    inputArray = text.strip().split()
    for x in range(len(inputArray) - 1):
        v = inputArray[x]

        if v in search:
            a = ["search", " ".join(inputArray[x + 1:])  ]
            break
        elif v in url:
            a = ["url", " ".join(inputArray[x + 1:])]
            break
        elif v in app:
            a = ["app", " ".join(inputArray[x + 1:])]
            break
        elif v in mouseScroll:
            a = ["mouseScroll", inputArray[x + 1]]
            break
        elif v in mouseClick:
            a = ["mouseClick", ""]
            break
        elif v in mouseDoubleClick:
            a = ["mouseDoubleClick", ""]
            break
        elif v in mouseMove:
            a =["mouseMove", " ".join(inputArray[x+1:])]
        elif v in keyboardType:
            a = ["keyboardType", " ".join(inputArray[x + 1:])]
            break
        elif v in keyboardHold:
            a = ["keyboardHold", inputArray[x + 1]]
            break
        elif v in keyboardRelease:
            a = ["keyboardRelease", inputArray[x + 1]]
            break
        elif v +" "+ inputArray[x+1] in music:
            a = ["music", "playpause"]
            break
            

    if len(a) == 0 and len(inputArray) > 0:
        if inputArray[-1] in mouseClick:
            a = ["mouseClick", ""]
        elif inputArray[-1] in mouseDoubleClick:
            a = ["mouseDoubleClick", ""]
    return a
