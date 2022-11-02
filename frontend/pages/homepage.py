import time
from threading import Thread
from tkinter import *
from tkinter import ttk

from backend.JarvisManager import JarvisManager

from .pages import (AdminPage, AdminPromptPage, ControlPage, MoveListPage,
                    PointsPage)


def count(manager: JarvisManager):
    try:
        manager.move_motor("LT", 500)
        manager.move_motor("LI", 500)
        manager.move_motor("LM", 440)
        manager.move_motor("LR", 225)
        manager.move_motor("LP", 225)
        manager.move_motor("LT", 500)
        manager.move_motor("RT", "max")
        manager.move_motor("RI", "min")
        manager.move_motor("RM", "max")
        manager.move_motor("RR", "max")
        manager.move_motor("RP", "max")
        time.sleep(.5)
        manager.move_motor("LI", 275)
        time.sleep(.5)
        manager.move_motor("LM", 300)
        time.sleep(.5)
        manager.move_motor("LR", 375)
        time.sleep(.5)
        manager.move_motor("LP", 400)
        time.sleep(.5)
        manager.move_motor("LT", 330) # used to be 300
        time.sleep(.5)
        manager.move_motor("RI", "max")
        time.sleep(.5)
        manager.move_motor("RM", "min")
        time.sleep(.5)
        manager.move_motor("RR", "min")
        time.sleep(.5)
        manager.move_motor("RP", "min")
        time.sleep(.5)
        manager.move_motor("RT", "min")
    except Exception as e:
        print(str(e))

    
def nod(manager: JarvisManager):
    manager.move_motor("HT", 300)
    time.sleep(.15)
    manager.move_motor("HT", 150)
    time.sleep(.15)
    manager.move_motor("HT", 300)
    time.sleep(.15)
    manager.move_motor("HT", 150)
    time.sleep(.15)
    manager.move_motor("HT", 300)





class Homepage:

    def __init__(self, manager: JarvisManager, root: Tk, **kwargs):
        self.root = root
        self.manager = manager
        root.title('Homepage')
        root.geometry("800x600")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.style = ttk.Style(root)
        # self.style.theme_use('alt')
        self.style.configure("HomePage.TFrame", background="#26343E")
        self.style.configure("HomePage.TLabel", font=("Helvetica", 24), background="#26343E", foreground="white")
    
        self.frame = ttk.Frame(root, style="HomePage.TFrame")
        self.frame.grid(column=0, row=0, sticky="nsew")

        self.build_child_pages()

        ttk.Label(self.frame, style="HomePage.TLabel", text="Welcome to the Jarvis Controller!") \
            .grid(column=1, row=0)

        self.build_demos()

     
        for i in range(3):
            self.frame.grid_columnconfigure(i, weight=1)
        
        for child in self.frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)




    def build_child_pages(self):
        ttk.Button(self.frame, text="Control", command=lambda: ControlPage.deploy(self.manager, self.root)) \
                .grid(column=0, row=0)
        ttk.Button(self.frame, text="Movelists", command=lambda: MoveListPage.deploy(self.manager, self.root)) \
                .grid(column=0, row=1)
        ttk.Button(self.frame, text="Points", command=lambda: PointsPage.deploy(self.manager, self.root)) \
                .grid(column=0, row=3)
        ttk.Button(self.frame, text="Admin", command= lambda: AdminPromptPage.deploy(self.manager, self.root)) \
                .grid(column=0, row=4)
        ttk.Button(self.frame, text="Close all tabs", command= lambda: [
            ControlPage.destroy_all(self.root),
            PointsPage.destroy_all(self.root),
            MoveListPage.destroy_all(self.root),
            AdminPage.destroy_all(self.root),
            AdminPromptPage.destroy_all(self.root)
        ]).grid(column=0, row=5)

       
 
    def build_demos(self):
        ttk.Button(self.frame, text="Count", command=lambda: Thread(None, count, args=(self.manager,)).start()) \
                .grid(column=2, row=0)
        ttk.Button(self.frame, text="Nod", command=lambda:  Thread(None, nod, args=(self.manager,)).start()) \
                .grid(column=2, row=1)



if __name__ == "__main__":
    root = Tk()

    manager = JarvisManager.from_socket(None)
    homepage = Homepage(manager, root)

    root.mainloop()
