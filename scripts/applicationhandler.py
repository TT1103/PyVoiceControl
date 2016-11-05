import subprocess

def OpenApp(s):
    try:
        subprocess.call(["open","-a",s])
    except:
        print "application open failed"
        return
    