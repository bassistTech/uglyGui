'''
uglyGui
(C) Francis Deck
MIT License
'''

import pandastable
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
import matplotlib
from PIL import ImageTk
matplotlib.use("TkAgg")


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
    def __init__(self, title):
        super().__init__()
        self.wm_title(title)
        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.withdraw)

    def show(self):
        self.deiconify()


class Button(tk.Button):
    def __init__(self, parent, label, action=None):
        frame = tk.Frame(master=parent)
        frame.pack(side=tk.TOP, fill=tk.BOTH)
        super().__init__(text=label, command=action)
        self.pack()


class __Entry(tk.Entry):
    def __init__(self, parent, label, init, datatype):

        frame = tk.Frame(master=parent)
        frame.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Label(frame, text=label).pack(side=tk.LEFT)
        self.value = tk.StringVar()
        super().__init__(frame, textvariable=self.value, width=45)
        self.pack(side=tk.RIGHT, fill=tk.X)
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
                 parent, label, buttonLabels, init, vertical, callback):

        self.value = tk.IntVar()
        self.value.set(init)
        frame = tk.Frame(master=parent)
        frame.pack(side=tk.TOP)
        if vertical:
            ps = tk.TOP
        else:
            ps = tk.LEFT
        tk.Label(frame, text=label).pack(side=ps)
        for i in range(len(buttonLabels)):
            tk.Radiobutton(frame, text=buttonLabels[i], value=i,
                           variable=self.value,
                           command=callback).pack(side=ps)

    def get(self):
        return self.value.get()

    def upd(self, i):
        self.value.set(i)


class CheckBox(tk.Checkbutton):
    def __init__(self, parent, label, init, callback):
        self.value = tk.IntVar()
        self.value.set(init)
        frame = tk.Frame(master=parent)
        frame.pack(side=tk.TOP, fill=tk.BOTH)
        super().__init__(frame,
                         text=label,
                         command=callback,
                         variable=self.value)
        self.pack(side=tk.LEFT)

    def get(self):
        return self.value.get()

    def upd(self, i):
        self.value.set(i)


class ImageLabel(tk.Label):
    def __init__(self, parent, width, height, image):
        self.resized_image = image.resize((width, height))
        self.tk_image = ImageTk.PhotoImage(self.resized_image)
        super().__init__(parent, image = self.tk_image)
        self.image = self.tk_image
        self.pack(side=tk.TOP, fill=tk.BOTH)

    def upd(self, img):
        self.resized_image = img.resize((300, 400))#, Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(self.resized_image)
        self.config(image = self.tk_image)


class Graph():
    def __init__(self, parent, r, c):
        self.fig = matplotlib.figure.Figure()
        self.axes = [self.fig.add_subplot(s)
                     for s in matplotlib.gridspec.GridSpec(r, c)]
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(self.canvas, parent)
        toolbar.update()
        toolbar.pack(side=tk.TOP)

    def update(self):
        self.canvas.draw()


class TextEditor():
    '''
    I adopted the code from:
        https://www.geeksforgeeks.org/build-a-basic-text-editor-using-tkinter-in-python/
    The only nuance is that I put the text editor in a frame, so it can coexist
    with other widgets in a dialog
    '''

    def __init__(self, parent, init):
        frame = tk.Frame(master=parent)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar = tk.Scrollbar(frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text = tk.Text(frame,
                            width=50, height=20,
                            yscrollcommand=self.scrollbar.set)
        self.text.pack(fill=tk.BOTH, expand=1)
        self.scrollbar.config(command=self.text.yview)
        self.text.insert('1.0', init)

    def get(self):
        return self.text.get('1.0', 'end')

    def upd(self, text):
        self.text.delete('1.0', 'end')
        self.text.insert('1.0', text)


class TableEdit():
    def __init__(self, parent, df):
        frame = tk.Frame(master=parent)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.df = df
        self.table = pandastable.Table(frame, dataframe=self.df,
                                       showtoolbar=True, showstatusbar=True)
        self.table.showIndex()
        self.table.show()


if __name__ == '__main__':
    def goBu():
        print(te.get())
        te.upd('Mobbs')

    mainDialog = MainDialog('Text editor test')
    te = TextEditor(mainDialog, 'hee')
    bu = Button(mainDialog, 'Do something', action=goBu)
    subDialog = SubDialog()
    mainDialog.show()
