from typing import Any, Dict, Literal, Union

import jarvisFileReading
import numpy as np
import serial


class JarvisMotors:
    
    _debug: bool
    comms: serial.Serial
    config: Dict[str, Any]

    def __init__(self, debug: bool = False):
        if not debug:
            self.comms = serial.Serial(port='COM3', baudrate=9600, timeout=5)
        else:
            self.comms = None   # type: ignore

        self._debug = debug
        self.config = jarvisFileReading.get_config()
        
 
    def set_motor_config(self, motor: str, setting: Literal["min", "max", "home"], val: float): 
        tmp = self.config["motors"][motor]

        if setting == "min":
            tmp[1] = val

        if setting == "max":
            tmp[2] = val
        
        if setting == "home":
            tmp[3] = val

        jarvisFileReading.write_motor_config(motor, tmp)

        # debugging, change to simple assignment when confirmed working.
        self.config = jarvisFileReading.get_config()
        

    def move_motor(self, name: str, amt: float): 
        assert name in self.config["motors"], f"{name} is not in the config's motors."

        tmp = self.config["motors"][name]
        assert tmp[1] <= amt and tmp[2] >= amt, f"[{name}] wanted: {amt}, min: {tmp[1]}, max: {tmp[2]}"

        if self._debug:
            print(f"Moving motor {name} to {amt}.\n\tRaw data: {tmp[0] + amt}")
        else:

            self._write_read(str(tmp[0] + amt))

        
    def _write_read(self, msg: str):
        self.comms.write(bytes(msg + '\n', 'utf-8'))
  
            



if __name__ == "__main__":
    test = JarvisMotors(True)
    test.move_motor("LS", 450)
