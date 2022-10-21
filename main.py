from tkinter import Tk

from backend import JarvisBrain, JarvisManager, JarvisMotors
from frontend.pages.homepage import Homepage


def test_backend():
    manager = JarvisManager.from_socket(None)

    
    manager.perform_movelist("random_moveset")

    
def test_frontend():
    manager = JarvisManager.from_socket(None)

    
    root = Tk()
    app = Homepage(manager, root)

    root.mainloop()
 

if __name__ == "__main__":
    test_frontend()




    # 1, 1
    # 1, 2
    # 1, 3
    # ...1, 11
            
    # 2, 1
    # 2, 2
    # 2, 3
    # ...2, 11
            
    # 3, 1
    # 3, 2
    # 3, 3
    # ...3, 11
            