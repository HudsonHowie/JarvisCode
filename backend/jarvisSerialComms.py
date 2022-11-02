import os
import uuid
import wave
from typing import Dict, List, Optional, Tuple, Union

import pyttsx3
import serial
from typing_extensions import Literal

from . import jarvisFileReading


class JarvisComms:

    _debug: bool
    comms: serial.Serial

    def __init__(self, com: Optional[serial.Serial] = None):
        if com:
            self.comms = com
            self._debug = False
        else:
            self.comms = None   # type: ignore
            self._debug = True

    def _write_read(self, msg: str):
        self.comms.write(bytes(msg + '\n', 'utf-8'))


class JarvisMotors(JarvisComms):

    motor_info: Dict[str, jarvisFileReading.MotorInfo]

    def __init__(self, com: Optional[serial.Serial] = None):
        super().__init__(com)
        self.motor_info = jarvisFileReading.get_config()["motors"]

    def get_motor_info(self) -> Dict[str, jarvisFileReading.MotorInfo]:
        return self.motor_info

    def get_motor_names(self) -> List[str]:
        return self.motor_info.keys()  # type: ignore
    
    def get_motor_full_names(self) -> List[str]:
        return [val[4] for val in self.motor_info.values()]
    
    def get_motor_min(self, name: str) -> int:
        assert name in self.motor_info
        return self.motor_info[name][1]
    
    def get_motor_max(self, name: str) -> int:
        assert name in self.motor_info
        return self.motor_info[name][2]
    
    def get_motor_home(self, name: str) -> int:
        assert name in self.motor_info
        return self.motor_info[name][3]
    
    def get_motor_full_name(self, name: str) -> str:
        assert name in self.motor_info
        return self.motor_info[name][4]
    
    def get_motor_locked(self, name: str) -> bool:
        assert name in self.motor_info
        return self.motor_info[name][5]

    def set_motor_config(self, motor: str, setting: Literal["min", "max", "home"], val: int):
        tmp = self.motor_info[motor]

        if setting == "min":
            tmp[1] = val # type: ignore

        if setting == "max":
            tmp[2] = val # type: ignore

        if setting == "home":
            tmp[3] = val # type: ignore

        jarvisFileReading.write_motor_config(motor, tmp)

        # debugging, change to simple assignment when confirmed working.
        self.motor_info = jarvisFileReading.get_config()["motors"]

    def move_motor(self, name: str, amt: int):
        assert name in self.motor_info, f"{name} is not in the config's motors."

        tmp = self.motor_info[name]
        assert tmp[1] <= amt and tmp[2] >= amt, f"[{name}] wanted: {amt}, min: {tmp[1]}, max: {tmp[2]}"

        if tmp[5]:
            raise AssertionError(f"[{name}] is locked. Please unlock motor to use.")
        
        if self._debug:
            print(f"Moving motor {name} to {amt}.\n\tRaw data: {tmp[0] + amt}")
        else:
            self._write_read(str(tmp[0] + amt))

    def lock_motor(self, motor: str, val: bool):
        assert motor in self.motor_info, f"{motor} is not in the config's motors."

        if self._debug:
            if val:
                print(f"Locking motor {motor}.")
            else:
                print(f"Unlocking motor {motor}.")
            

        self.motor_info[motor][5] = val # type: ignore
        jarvisFileReading.write_motor_config(motor, self.motor_info[motor])

        # debugging, change to simple assignment when confirmed working.
        self.motor_info = jarvisFileReading.get_config()["motors"]


        



class JarvisOutputs(JarvisComms):

    SEND_SIZE = 1024


    outputs: Dict[str, int]
    engine: pyttsx3.Engine

    def __init__(self, com: Optional[serial.Serial] = None, engine: Union[pyttsx3.Engine, None] = None):
        super().__init__(com)
        self.outputs = jarvisFileReading.get_config()["outputs"]
        if engine:
            self.engine = engine
        else:
            self.engine = pyttsx3.init()

        self.engine.setProperty('rate', 140)

    def get_output_info(self) -> Dict[str, int]:
        return self.outputs

    def get_output_names(self) -> List[str]:
        return self.outputs.keys()  # type: ignore

    def text_to_wav(self, text: str, dir: Union[str, None] = None, fname: Union[str, None] = None) -> str:
        if fname and dir:
            filename = os.path.join(dir, fname)
        elif fname and not dir:
            filename = fname
        elif not fname and dir:
            filename = os.path.join(dir, f"{uuid.uuid4()}.wav")
        else:
            filename = f"{uuid.uuid4()}.wav"

        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()
        return os.path.abspath(filename)
    

    def stream_wav_over_serial(self, filename: str):
        with wave.open(filename, 'rb') as wf:
            self.comms.write('start_wav')
            to_send = wf.readframes(JarvisOutputs.SEND_SIZE)
            while to_send != b'':
                self.comms.write(to_send)
                to_send = wf.readframes(JarvisOutputs.SEND_SIZE)
            self.comms.write('end_wav')



if __name__ == "__main__":

    test = JarvisMotors(None)
    test.move_motor("LS", 450)

    test1 = JarvisOutputs()
    path = test1.text_to_wav("testing", "./tests", "testing_it.wav")
    os.system(f"mpv {path}")
    os.remove(path)
