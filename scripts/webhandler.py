import webbrowser


def OpenURL(url):
    webbrowser.open(url)


def GoogleSearch(query):
    webbrowser.open("https://google.ca/#q=" + "+".join(query.strip().split()))


def OpenSite(query):
    webbrowser.open("https://" + str(query) + ".com")


def ImageSearch(query):
    webbrowser.open("https://images.google.ca/#q=" +
                    "+".join(query.strip().split()))
