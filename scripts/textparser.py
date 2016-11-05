from webhandler import*

# parses the input test and determines a valid command


def GetCommand(text):

    inputArray = text.split()

    if(inputArray[0] == "Google"):
        # run google script
        GoogleSearch(text[len(inputArray[0]):])

    elif(inputArray[0] == "Open"):

    pass
