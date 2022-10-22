import os
from typing import Dict, List, Union

import serial
from typing_extensions import Literal

from backend import jarvisFileReading


class JarvisComms:

    _debug: bool
    comms: serial.Serial

    def __init__(self, com: Union[serial.Serial, None]):
        if com:
            self.comms = com 
            self._debug = False
        else:
            self.comms = None   # type: ignore
            self._debug = True

            
        

    def _write_read(self, msg: str):
        self.comms.write(bytes(msg + '\n', 'utf-8'))
  


class JarvisMotors(JarvisComms):
    
    motor_info: Dict[str, List[float]]

    def __init__(self, com: Union[serial.Serial, None]):
        super().__init__(com)
        self.motor_info = jarvisFileReading.get_config()["motors"]


    def get_motor_info(self) ->  Dict[str, List[float]]:
        return self.motor_info
      
    
    def get_motor_names(self) -> List[str]:
        return self.motor_info.keys()  # type: ignore

 
    def set_motor_config(self, motor: str, setting: Literal["min", "max", "home"], val: float): 
        tmp = self.motor_info[motor]

        if setting == "min":
            tmp[1] = val

        if setting == "max":
            tmp[2] = val
        
        if setting == "home":
            tmp[3] = val

        jarvisFileReading.write_motor_config(motor, tmp)

        # debugging, change to simple assignment when confirmed working.
        self.motor_info = jarvisFileReading.get_config()["motors"]
        

    def move_motor(self, name: str, amt: float): 
        assert name in self.motor_info, f"{name} is not in the config's motors."

        tmp = self.motor_info[name]
        assert tmp[1] <= amt and tmp[2] >= amt, f"[{name}] wanted: {amt}, min: {tmp[1]}, max: {tmp[2]}"

        if self._debug:
            print(f"Moving motor {name} to {amt}.\n\tRaw data: {tmp[0] + amt}")
        else:
            self._write_read(str(tmp[0] + amt))

        

from pydub import AudioSegment


class JarvisOutputs(JarvisComms):

    outputs: Dict[str, float]

    def __init__(self, com: Union[serial.Serial, None]):
        super().__init__(com)

        self.outputs = jarvisFileReading.get_config()["outputs"]


    def get_output_info(self) ->  Dict[str, float]:
        return self.outputs
      
    
    def get_output_names(self) -> List[str]:
        return self.outputs.keys()  # type: ignore
        

    
    def speak_mp3(self, filepath: str):
        sound: AudioSegment = AudioSegment.from_file(filepath)
        sound.export(os.path.dirname(filepath), format="wav")
        return




if __name__ == "__main__":
    test = JarvisMotors(None)
    test.move_motor("LS", 450)
