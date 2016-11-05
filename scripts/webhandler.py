import webbrowser


def OpenURL(url):
    webbrowser.open(url);
    
def GoogleSearch(query):
    webbrowser.open("https://google.ca/#q=" + "+".join(query.strip().split()))
    
    

    