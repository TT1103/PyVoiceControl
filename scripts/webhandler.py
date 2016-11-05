import webbrowser


def OpenURL(url):
    webbrowser.open("https://" + url + ".com")


def GoogleSearch(query):
    webbrowser.open("https://google.ca/#q=" + "+".join(query.strip().split()))
