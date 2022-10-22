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
    socket = serial.Serial(port='COM3', baudrate=9600, timeout=5)
    # socket = None
    manager = JarvisManager.from_socket(socket)

    
    root = Tk()
    app = Homepage(manager, root)

    root.mainloop()
 

if __name__ == "__main__":
    test_frontend()
