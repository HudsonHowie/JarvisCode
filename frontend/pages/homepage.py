from tkinter import *
from tkinter import ttk
from typing import Any

from backend.JarvisManager import JarvisManager

from .pages import ControlPage, PointsPage, ProgramPage


class Homepage:

    def __init__(self, manager: JarvisManager, root: Tk, **kwargs):
        self.master = root
        self.manager = manager
        root.title('Homepage')
        root.geometry("800x600")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.frame = ttk.Frame(root)
        self.frame.grid(column=0, row=0, sticky="nsew")
        self.build_buttons()


    def build_buttons(self):
        Button(self.frame, text="Control", command=lambda: ControlPage.deploy(self.manager, self.master)).grid(column=0, row=0)
        Button(self.frame, text="Programming", command=lambda: ProgramPage.deploy(self.manager, self.master)).grid(column=0, row=1)
        Button(self.frame, text="Points", command=lambda: PointsPage.deploy(self.manager, self.master)).grid(column=0, row=2)
        Button(self.frame, text="Close all tabs", command= lambda: [
            ControlPage.destroy_all(self.master),
            ProgramPage.destroy_all(self.master),
            PointsPage.destroy_all(self.master)
        ])



        for child in self.frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

if __name__ == "__main__":
    root = Tk()

    manager = JarvisManager.from_socket(None)
    homepage = Homepage(manager, root)

    root.mainloop()
