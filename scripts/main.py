import ocrhandler
import mousehandler


def main():
    t = "print"
    filename = ".screenshot.png"
    img = ocrhandler.GetScreenShot(filename)
    s = ocrhandler.LocateText(img, t, filename)

    if not s:
        print "failed"
        return
    for x in s:
        print x

    mousehandler.Move(s[0][0], s[0][1])


if __name__ == "__main__":
    main()
