import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from AutoHideScrollBar import AutoHideScrollbar
import os


class Notepad:
    root = tk.Tk()

    # Default values for width and height
    width = 1024
    height = 768

    text_area = tk.Text(root)
    menu_bar = tk.Menu(root)
    canvas = None
    # Disable tearoff for menus
    file_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    page_layout_menu = tk.Menu(menu_bar, tearoff=0)
    options_menu = tk.Menu(menu_bar, tearoff=0)

    scroll_bar = AutoHideScrollbar(root)
    file = None

    def __init__(self, **kwargs):

        try:
            self.width = kwargs['width']
        except KeyError:
            pass

        try:
            self.height = kwargs['height']
        except KeyError:
            pass

        self.root.title("Untitled Note | PyNote+")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        left = (screen_width / 2) - (self.width / 2)
        top = (screen_height / 2) - (self.height / 2)

        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, left, top))

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.text_area.grid(sticky=tk.N + tk.E + tk.S + tk.W)

        self.file_menu.add_command(label="New file", command=self.new_file)
        self.file_menu.add_command(label="Open file", command=self.open_file)
        self.file_menu.add_command(label="Save file", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit_application)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.options_menu.add_command(label="Preferences")
        self.menu_bar.add_cascade(label="Options", menu=self.options_menu)
        self.root.config(menu=self.menu_bar)

        self.scroll_bar.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.text_area.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.text_area.yview)

    def save_checker(self):
        result = tkinter.messagebox.askquestion("Warning!", "Do you want to save this file before opening new file?")
        if result == 'yes':
            self.save_file()

    def open_file(self):

        self.file = tk.filedialog.askopenfilename(defaultextension=".txt",
                                                  filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file) + " PyNote+")
            self.text_area.delete(1.0, tk.END)
            # ADD CHOICE TO SAVE EXISTING NOTE BEFORE OPENING NEW FILE

            file = open(self.file, "r")

            self.text_area.insert(1.0, file.read())

            file.close()

    def new_file(self):
        self.root.title("Untitled Note | PyNote+")
        self.file = None
        current_text = self.text_area.get(1.0, tk.END)
        if len(current_text) == 1:
            pass
        else:
            self.save_checker()
        self.text_area.delete(1.0, tk.END)

    def save_file(self):

        if self.file is None:
            self.file = tk.filedialog.asksaveasfilename(initialfile='Untitled Note.txt', defaultextension=".txt",
                                                        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),
                                                                   ("Word Document", "*.docx")])

            if self.file == "":
                self.file = None
            else:
                file = open(self.file, "w")
                file.write(self.text_area.get(1.0, tk.END))
                file.close()
                self.root.title(os.path.basename(self.file) + "| PyNote+")
        else:
            file = open(self.file, "w")
            file.write(self.text_area.get(1.0, tk.END))
            file.close()

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def run(self):
        self.root.mainloop()

    def quit_application(self):
        confirm_exit = tkinter.messagebox.askquestion("Warning!", "Do you want to close the application? ")
        if confirm_exit == 'yes':
            current_text = self.text_area.get(1.0, tk.END)
            if len(current_text) == 1:
                pass
            else:
                result = tkinter.messagebox.askquestion("Warning!", "Do you want to save this file? ")
                if result == "yes":
                    self.save_file()
            self.root.destroy()
