import tkinter as tk


class AutoHideScrollbar(tk.Scrollbar):
    # Define set method for auto hiding function
    def set(self, low, high):

        if float(low) <= 0.0 and float(high) >= 1.0:
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        tk.Scrollbar.set(self, low, high)

    # Since this class will be used with grid method. Other geometry methods
    # should not be used. Thus, raise error when tried to.
    def pack(self, **kw):

        raise (tk.TclError, "pack cannot be used with \
               this widget")

    def place(self, **kw):

        raise (tk.TclError, "place cannot be used  with \
               this widget")
