import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class MainDialog(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.wm_title(title)
        self.protocol("WM_DELETE_WINDOW", self.allQuit)
        
    def allQuit(self):
        self.destroy()
        self.quit()
        
    def show(self):
        self.mainloop()

class SubDialog(tk.Toplevel):
    def __init(self, title):
        super().__init()
        self.wm_title(title)
        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.withdraw)
        
    def show(self):
        self.deiconify()

class Button(tk.Button):
    def __init__(self, parent, label, action = None):
        frame = tk.Frame(master = parent)
        frame.pack(side = tk.TOP, fill = tk.BOTH)
        super().__init__(text = label, command = action)
        self.pack()

class __Entry(tk.Entry):
    def __init__(self, parent, label, init, datatype):

        frame = tk.Frame(master = parent)
        frame.pack(side = tk.TOP, fill = tk.BOTH)
        
        tk.Label(frame, text=label).pack(side = tk.LEFT)
        self.value = tk.StringVar()
        super().__init__(frame, textvariable = self.value, width = 15)
        self.pack(side = tk.RIGHT, fill = tk.X)
        self.value.set(str(init))
        self.datatype = datatype

    def get(self):
        return {'S': str, 'I': int, 'F': float}[self.datatype](self.value.get())

    def upd(self, s):
        self.value.set(str(s))

class IntEntry(__Entry):
    def __init__(self, parent, label, init):
        super().__init__(parent, label, init, 'I')
        
class FloatEntry(__Entry):
    def __init__(self, parent, label, init):
        super().__init__(parent, label, init, 'F')
        
class TextEntry(__Entry):
    def __init__(self, parent, label, init):
        super().__init__(parent, label, init, 'S')

class RadioButtons():
    def __init__(self,
                 parent, label, buttonLabels, init, vertical):

        self.value = tk.IntVar()
        self.value.set(init)
        frame = tk.Frame(master = parent)
        frame.pack(side = tk.TOP)
        if vertical:
            ps = tk.TOP
        else:
            ps = tk.LEFT
        tk.Label(frame, text = label).pack(side=ps)
        for i in range(len(buttonLabels)):
            tk.Radiobutton(frame, text = buttonLabels[i], value = i,
                               variable = self.value).pack(side=ps)

    def get(self):
        return self.value.get()

    def upd(self, i):
        self.value.set(i)

class CheckBox(tk.Checkbutton):
    def __init__(self, parent, label, init, callback):
        self.value = tk.IntVar()
        self.value.set(init)
        frame = tk.Frame(master = parent)
        frame.pack(side = tk.TOP, fill = tk.BOTH)
        super().__init__(frame,
                       text = label,
                       command = callback,
                       variable = self.value)
        self.pack(side = tk.LEFT)

    def get(self):
        return self.value.get()

    def upd(self, i):
        self.value.set(i)

class Graph():
    def __init__(self, parent, r, c):
        self.fig = matplotlib.figure.Figure()
        self.axes = [self.fig.add_subplot(s) 
                     for s in matplotlib.gridspec.GridSpec(r, c)]
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side = tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(self.canvas, parent)
        toolbar.update()
        toolbar.pack(side = tk.TOP)