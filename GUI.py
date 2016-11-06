import Tkinter as tk
import time
import threading


class GUI(object):
    i = 0
    v = None
    rotatingFast = False

    def __init__(self):
        self.v = tk.StringVar()

        self.rotatingFast = False
        self.root = tk.Tk()
        self.canvas = tk.Canvas(root, width=500, height=108, borderwidth=0,
                                highlightthickness=0, bg="#A6D785")

        self.canvas.grid()

        frame = tk.Frame(root)
        frame.grid(row=0, column=0, sticky="n")

        label1 = tk.Label(frame, textvariable=v, bg="#A6D785").grid(
            row=0, column=0, sticky="nw")
        self.v.set("Hello!")

        ws = root.winfo_screenwidth()
        #hs = root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (500, 108, ws - 500, 0))
        tk.Canvas.create_circle = _create_circle
        tk.Canvas.create_circle_arc = _create_circle_arc

        self.root.wm_title("PyVoiceControl")
        thread = threading.Thread(target=runAnimationThread)
        thread.start()

    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)

    def _create_circle_arc(self, x, y, r, **kwargs):
        if "start" in kwargs and "end" in kwargs:
            kwargs["extent"] = kwargs["end"] - kwargs["start"]
            del kwargs["end"]
        return self.create_arc(x - r, y - r, x + r, y + r, **kwargs)

    #--------------------------------------------------------------------------

    def updateGuiSpeed(rotation):
        self.rotatingFast = rotation

    def updateGui(textIn):
        self.v.set(textIn)
#------------------------------------------------------------------

    def runAnimationThread():
        while True:
            if(rotatingFast):
                self.i += 3
            self.i += 3
            self.canvas.delete("all")
            self.canvas.create_circle(446, 54, 50, fill="blue",
                                      outline="#DDD", width=4)
            self.canvas.create_circle_arc(446, 54, 45, style="arc",
                                          outline="#7cdbd5", width=15, start=i - 25, end=+ i + 25)
            self.canvas.create_circle_arc(446, 54, 45, style="arc",
                                          outline="#7cdbd5", width=15, start=180 + i - 25, end=180 + i + 25)

            # TODO add in input text ------------------------------------------
            self.root.call('wm', 'attributes', '.', '-topmost', '1')
            self.canvas.after(20)
            self.canvas.update()
        self.root.mainloop()
