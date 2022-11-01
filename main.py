import sys
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
 

def test_other():
    from backend.jarvisSerialComms import JarvisOutputs

    test = JarvisOutputs()
    test.text_to_wav("The quick brown fox jumped over the lazy dog.", None, "test_it.wav")

 
 
if __name__ == "__main__":
 
    import faulthandler

    # test_other()
    # faulthandler.dump_traceback(file=sys.stderr, all_threads=True)
    test_frontend()
