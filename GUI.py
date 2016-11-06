import Tkinter as tk
import time
import threading


class GUI(object):
    i = 0
    v = None
    rotatingFast = False
    canvas=None
    frame =None
    label1=None
    root=None
    def __init__(self):
        
        GUI.root = tk.Tk()

        GUI.v = tk.StringVar()

        GUI.rotatingFast = False
        GUI.canvas = tk.Canvas(GUI.root, width=500, height=108, borderwidth=0,
                                highlightthickness=0, bg="#A6D785")

        GUI.canvas.grid()

        GUI.frame = tk.Frame(GUI.root)
        GUI.frame.grid(row=0, column=0, sticky="n")

        GUI.label1 = tk.Label(GUI.frame, textvariable=GUI.v, bg="#A6D785").grid(
            row=0, column=0, sticky="nw")
        GUI.v.set("Hello!")

        ws = GUI.root.winfo_screenwidth()
        #hs = root.winfo_screenheight()
        GUI.root.geometry('%dx%d+%d+%d' % (500, 108, ws - 500, 0))
        tk.Canvas.create_circle =self._create_circle
        tk.Canvas.create_circle_arc = self._create_circle_arc

        GUI.root.wm_title("PyVoiceControl")
        #thread = threading.Thread(target=self.runAnimationThread)
        #thread.start()
        
        

    def setup(self):
        self.runAnimationThread()
        GUI.root.mainloop()
        
    def _create_circle(self, x, y, r, **kwargs):
        return GUI.canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)

    def _create_circle_arc(self, x, y, r, **kwargs):
        if "start" in kwargs and "end" in kwargs:
            kwargs["extent"] = kwargs["end"] - kwargs["start"]
            del kwargs["end"]
        return GUI.canvas.create_arc(x - r, y - r, x + r, y + r, **kwargs)

    #--------------------------------------------------------------------------
    @staticmethod
    def UpdateGuiSpeed(rotation):
        GUI.rotatingFast = rotation

    @staticmethod
    def UpdateGui(textIn):
        GUI.v.set(textIn)
#------------------------------------------------------------------

    def runAnimationThread(self):

        if(GUI.rotatingFast):
            GUI.i += 3
        GUI.i += 3
        GUI.canvas.delete("all")
        GUI.canvas.create_circle(446, 54, 50, fill="blue",
                                  outline="#DDD", width=4)
        GUI.canvas.create_circle_arc(446, 54, 45, style="arc",
                                      outline="#7cdbd5", width=15, start=GUI.i - 25, end=+ GUI.i + 25)
        GUI.canvas.create_circle_arc(446, 54, 45, style="arc",
                                      outline="#7cdbd5", width=15, start=180 + GUI.i - 25, end=180 + GUI.i + 25)

        # TODO add in input text ------------------------------------------
        GUI.root.call('wm', 'attributes', '.', '-topmost', '1')
        GUI.canvas.after(20,self.runAnimationThread)
        GUI.canvas.update()
