import json
import os
from typing import Annotated, Any, Dict, Tuple, Union

import numpy as np

MOTOR_COUNT = 23


def get_config() -> Dict[str, Any]:
    with open(os.path.dirname(__file__) + "/config.json", "r") as f:
        return json.load(f)



def get_memory() -> Dict[str, list[float]]:
    with open(os.path.dirname(__file__) + "/memory.json", "r") as f:
        return json.load(f)


def get_memory_numpy() -> Dict[str, 'np.ndarray[tuple, Any]']:
    with open(os.path.dirname(__file__) + "/memory.json", "r") as f:
        memory = json.load(f)
        for mem in memory["movements"]:
            memory["movements"][mem] = np.array(memory["movements"][mem])
        return memory


def write_motor_config(name: str, val: list[float]):
    config = json.load(open(os.path.dirname(__file__) + "/config.json", "r"))

    # checks that name is in config, throws error otherwises
    assert name in config["motors"], f"{name} not in the config's motor list."

    config["motors"][name] = val

    json.dump(config, open(os.path.dirname(__file__) + "/config.json", "w"), indent=4)


def write_output_config(name: str, val: list[float]):
    config = json.load(open(os.path.dirname(__file__) + "/config.json", "r"))

    # checks that name is in config, throws error otherwises
    assert name in config["outputs"], f"{name} not in the config's sensor list."

    config["outputs"][name] = val

    json.dump(config, open(os.path.dirname(__file__) + "/config.json", "w"), indent=4)

    

    


def write_memory_point(name: str, val: Union[list[float], 'np.ndarray[tuple, Any]']):
    # clean up numpy to make it writeable to file
    if type(val) == np.ndarray:
        val = val.tolist() # type: ignore 

    # check that all motors are properly set.
    assert len(val) == MOTOR_COUNT, f"{val} has length {len(val)}, which is not {MOTOR_COUNT} (for all motors)."

    mem = json.load(open(os.path.dirname(__file__) + "/memory.json", "r"))

    mem["movements"][name] = val

    json.dump(mem, open(os.path.dirname(__file__) + "/memory.json", "w"), indent=4)


def write_memory_movelist(name: str, moves: list[str]):
    mem = json.load(open(os.path.dirname(__file__) + "/memory.json", "r"))
    mem["movelists"][name] = moves
    json.dump(mem, open(os.path.dirname(__file__) + "/memory.json", "w"), indent=4)






if __name__ == "__main__":

    from math import ceil
    conf = get_config()["motors"]
    tmp = get_memory()
    tmp1 = []
    for motor in conf:
        tmp1.append( ceil((conf[motor][1] + conf[motor][2]) / 2))


    print(tmp1)
    write_memory_point("first", tmp1)

    
    # print(get_config())
    # try:
    #     write_memory_point("second", [0, 0, 0])
    # except AssertionError:
    #     print("test failed successfully")

    # write_memory_point("third", [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    # print(get_memory_numpy())
