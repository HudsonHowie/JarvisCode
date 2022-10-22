from tkinter import Tk

import serial

from backend import JarvisManager
from frontend import Homepage


def test_backend():
    socket = serial.Serial(port='COM3', baudrate=9600, timeout=5)
    # socket = None
    manager = JarvisManager.from_socket(socket)

    
    manager.perform_movelist("random_moveset")

    
def test_frontend():
    # socket = serial.Serial(port='COM3', baudrate=9600, timeout=5)
    socket = None
    manager = JarvisManager.from_socket(socket)

    
    root = Tk()
    app = Homepage(manager, root)

    root.mainloop()
 

def test():
    import tkinter
    from tkinter import ttk

    root = tkinter.Tk()

    style = ttk.Style()
    style.map("C.TButton",
        foreground=[('pressed', 'red'), ('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )

    colored_btn = ttk.Button(text="Test", style="C.TButton").pack()

    root.mainloop()

if __name__ == "__main__":
 
    # test()
    test_frontend()
