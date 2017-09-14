"""
A Simple Text Editor in Python

"""

import tkinter as tk
import tkinter.filedialog as fdialogue
from properties import *
import tkinter.ttk as ttk

FILELOCATION = ""

def save_as():
    """ Save new file """
    global TEXT
    t = TEXT.get("1.0", "end-1c")
    save_location = fdialogue.asksaveasfilename()
    new_file = open(save_location, 'w+')
    new_file.write(t)
    new_file.close()

def already_open():
    """ Check if another file is already opened in buffer
        Used for opening another file if a file is already opened in buffer
    """
    global TEXT
    text = TEXT.get("1.0", "end-1c")
    if len(text) == 0:
        return False
    return True

def save_file():        
    """ Save the file """
    global TEXT
    text = TEXT.get("1.0", "end-1c")
    global FILELOCATION
    # Check if the file in current buffer is new
    if len(FILELOCATION) == 0:
        save_as()
    else:
        opened_file = open(FILELOCATION, 'w')
        opened_file.write(text)

def open_file():
    """ Open new file in editor """
    global FILELOCATION
    file_location = fdialogue.askopenfilename()
    opened_file = open(file_location)
    text = [line for line in opened_file]
    text_string = "".join(text)
    global TEXT
    if already_open():
        TEXT.delete("1.0", "end-1c")
    TEXT.insert("1.0", text_string)
    opened_file.close()
    FILELOCATION = file_location

if __name__ == '__main__':
    """ This is master	branch """
    ROOT = tk.Tk()
    MAIN_FRAME = tk.Frame(ROOT)
    MAIN_FRAME.master.title("Text Editor")
    MAIN_FRAME.configure(background=TOOLBAR_BGCOLOR)
    MAIN_FRAME.pack(fill=tk.BOTH, expand=True)
    NAV_BAR = tk.Canvas(MAIN_FRAME)
    NAV_BAR.pack(side=tk.TOP)
    TEXT = tk.Text(MAIN_FRAME)
    TEXT.configure(background=EDITOR_BGCOLOR)
    TEXT.pack(fill=tk.BOTH, expand=True)
    SAVEAS_BUTTON = tk.Button(NAV_BAR, text="Save As", command=save_as)
    SAVEAS_BUTTON.configure(background=BUTTONS_BGCOLOR)
    SAVEAS_BUTTON.pack(side=tk.LEFT)
    SAVE_BUTTON = tk.Button(NAV_BAR, text="Save", command=save_file)
    SAVE_BUTTON.configure(background=BUTTONS_BGCOLOR)
    SAVE_BUTTON.pack(side=tk.LEFT)
    OPEN_BUTTON = tk.Button(NAV_BAR, text="Open", command=open_file)
    OPEN_BUTTON.configure(background=BUTTONS_BGCOLOR)
    OPEN_BUTTON.pack(side=tk.LEFT)
    ROOT.mainloop()
