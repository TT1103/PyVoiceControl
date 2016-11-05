import subprocess
import VoiceOutput

def OpenApp(s):
    try:
        subprocess.call(["open","-a",s])
    except:
        print "application open failed"
        VoiceOutput.Say("Unable to open "+str(s))
        return
    