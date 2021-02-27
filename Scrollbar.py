import tkinter as tk


class AutoHideScrollBar:

    def __init__(self, p_text_area):
        tk.Scrollbar(p_text_area)

    def set(self, low, high):

        if float(low) <= 0.0 and float(high) >= 1.0:

            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        tk.Scrollbar.set(self, low, high)

    def pack(self, **kw):

        raise (tk.TclError, "pack cannot be used with \
               this widget")

    def place(self, **kw):


        raise (tk.TclError, "place cannot be used  with \
               this widget")
