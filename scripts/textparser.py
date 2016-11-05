from webhandler import*

# parses the input test and determines a valid command


def GetCommand(text):

    inputArray = text.split()

    if(inputArray[0] == "Google"):
        # run google script
        GoogleSearch(text[len(inputArray[0]) + 1:])

    elif(inputArray[0] == "open"):
        OpenSite(text[len(inputArray[0]) + 1:])

    elif (inputArray[0] == "show" and inputArray[1] == "me"):
        ImageSearch(text[len(inputArray[0]) + len(inputArray[1]) + 1:])

    pass
