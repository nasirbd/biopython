#!/usr/bin/env python
# Created: Thu Jul 13 12:09:58 2000
# Last changed: Time-stamp: <00/12/03 12:10:58 thomas>
# thomas@cbs.dtu.dk, http://www.cbs.dtu.dk/thomas
# File: xbb_utils.py

import sys

sys.path.insert(0, '.')

try:  # Python 2
    import Tkinter as tk
    import ttk
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.ttk as ttk

try:
    import tkFileDialog as filedialog  # Python 2
except ImportError:
    from tkinter import filedialog  # Python 3


class NotePad(tk.Toplevel):
    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar)
        self.filemenu.add_command(label="Save", command=self.save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Dismiss", command=self.destroy)

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.configure(menu=self.menubar)
        self.yscroll = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.tid = tk.Text(self, yscrollcommand=self.yscroll.set)
        self.yscroll.configure(command=self.tid.yview)
        self.tid.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.yscroll.pack(side=tk.RIGHT, fill=tk.Y)

    def text_id(self):
        return self.tid

    def insert(self, start, txt):
        self.tid.insert(start, txt)

    def save(self):
        fd = filedialog.SaveFileDialog(self)
        file = fd.go(key="test")
        if file:
            with open(file, 'w') as fid:
                fid.write(self.tid.get(0.0, tk.END))
