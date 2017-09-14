"""
A Simple Text Editor in Python

"""

import tkinter as tk
import tkinter.filedialog as fdialogue
from properties import *
import tkinter.ttk as ttk

FILELOCATION = ""

def save_as(text):
    """ Save new file """
    t = text.get("1.0", "end-1c")
    save_location = fdialogue.asksaveasfilename()
    newfile = open(save_location, 'w+')
    newfile.write(t)
    newfile.close()

def already_open(text):
    """ Check if another file is already opened in buffer
        Used for opening another file if a file is already opened in buffer
    """
    filetext = text.get("1.0", "end-1c")
    if len(filetext) == 0:
        return False
    return True

def save_file(text):        
    """ Save the file """
    text = text.get("1.0", "end-1c")
    global FILELOCATION
    # Check if the file in current buffer is new
    if len(FILELOCATION) == 0:
        save_as(text)
    else:
        opened_file = open(FILELOCATION, 'w')
        opened_file.write(text)

def new_file():
    """ Create new file """
    

def open_file(text):
    """ Open new file in editor """
    global FILELOCATION
    file_location = fdialogue.askopenfilename()
    opened_file = open(file_location)
    temt = [line for line in opened_file]
    text_string = "".join(temt)
    if already_open(text):
        text.delete("1.0", "end-1c")
    text.insert("1.0", text_string)
    opened_file.close()
    FILELOCATION = file_location

def app():
    root = tk.Tk()
    main_frame = tk.Frame(root)
    main_frame.master.title("Text Editor")
    main_frame.configure(background=TOOLBAR_BGCOLOR)
    main_frame.pack(fill=tk.BOTH, expand=True)
    nav_bar = tk.Canvas(main_frame)
    nav_bar.pack(side=tk.TOP)
    text = tk.Text(main_frame)
    text.configure(background=EDITOR_BGCOLOR)
    text.pack(fill=tk.BOTH, expand=True)
    newfile_button = tk.Button(nav_bar, text="New", command=lambda: new_file(text))
    newfile_button.configure(background=BUTTONS_BGCOLOR)
    newfile_button.pack(side=tk.LEFT)
    saveas_button = tk.Button(nav_bar, text="Save As", command=lambda: save_as(text))
    saveas_button.configure(background=BUTTONS_BGCOLOR)
    saveas_button.pack(side=tk.LEFT)
    save_button = tk.Button(nav_bar, text="Save", command=lambda: save_file(text))
    save_button.configure(background=BUTTONS_BGCOLOR)
    save_button.pack(side=tk.LEFT)
    open_button = tk.Button(nav_bar, text="Open", command=lambda: open_file(text))
    open_button.configure(background=BUTTONS_BGCOLOR)
    open_button.pack(side=tk.LEFT)
    return root    

if __name__ == '__main__':
    """ This is master	branch """
    ROOT = app()
    ROOT.mainloop()
