import webbrowser


def OpenURL(url):
    webbrowser.open(url)


def GoogleSearch(query):
    webbrowser.open("https://google.ca/#q=" + str(query))


def ImFeelingLuckySearch(query):
    webbrowser.open("")
