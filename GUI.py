import Tkinter as tk
import time

rotating = True
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=108, borderwidth=0,
                   highlightthickness=0, bg="#A6D785")
# TODO change to black
canvas.grid()

frame = tk.Frame(root)
frame.grid(row=0,column=0, sticky="n")

v=tk.StringVar()
label1=tk.Label(frame, textvariable=v,bg="#A6D785").grid(row=0,column=0, sticky="nw")
v.set("hello")

ws = root.winfo_screenwidth()
#hs = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (500, 108, ws - 500, 0))


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)
tk.Canvas.create_circle = _create_circle


def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x - r, y - r, x + r, y + r, **kwargs)
tk.Canvas.create_circle_arc = _create_circle_arc

root.wm_title("PyVoiceControl")

i = 0

while True:
    if(rotating):
        i += 5
    canvas.delete("all")
    canvas.create_circle(446, 54, 50, fill="blue", outline="#DDD", width=4)
    canvas.create_circle_arc(446, 54, 45, style="arc",
                             outline="#7cdbd5", width=15, start=i - 25, end=+ i + 25)
    canvas.create_circle_arc(446, 54, 45, style="arc",
                             outline="#7cdbd5", width=15, start=180 + i - 25, end=180 + i + 25)

    # TODO add in input text -------------------------------------------------

    canvas.after(20)
    canvas.update()
    
root.mainloop()


