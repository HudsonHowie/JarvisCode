from jarvisBrain import JarvisBrain
from JarvisManager import JarvisManager
from jarvisSerialComms import JarvisMotors


def gen_random_move():
    from math import ceil
    from random import randrange

    import numpy as np
    from jarvisFileReading import get_config, get_memory
    conf = get_config()["motors"]
    tmp = get_memory()
    tmp1 = []
    for motor in conf:
        info = conf[motor]
        tmp1.append(randrange(info[1], info[2]))

    return np.array(tmp1)


def test_backend():
    manager = JarvisManager.from_socket(None)

    manager.brain.teach_moveset_raw("random_moveset",
                                [
                                    gen_random_move(),
                                    gen_random_move(),
                                    gen_random_move()
                                ])

    manager.perform_movelist("random_moveset")






if __name__ == "__main__":
    test_backend()