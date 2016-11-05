from webhandler import*

# parses the input test and determines a valid command


def GetCommand(text):

    if(text[0: 6] == "Google"):
        # run google script
        GoogleSearch(text[7:])
    pass
