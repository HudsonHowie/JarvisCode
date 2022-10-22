from typing import Union
import serial

from backend.jarvisBrain import JarvisBrain
from backend.jarvisSerialComms import JarvisMotors, JarvisOutputs


class JarvisManager:

    motors: JarvisMotors
    outputs: JarvisOutputs
    brain: JarvisBrain


    def __init__(self, controller: JarvisMotors, outputs: JarvisOutputs, brain: JarvisBrain):
        self.motors = controller
        self.brain = brain
        self.outputs = outputs


    @classmethod
    def from_socket(cls, socket: Union[serial.Serial, None]):
        return cls(JarvisMotors(socket), JarvisOutputs(socket), JarvisBrain())


    def perform_move(self, name: str):
        assert name in self.brain.memory["movements"], f"{name} not in memory's moveset."    
     
        tmp = self.brain.memory["movements"][name]
        index = 0  
        for motor in self.motors.motor_info:
            self.motors.move_motor(motor, tmp[index])
            index += 1

    def perform_movelist(self, name: str):
        assert name in self.brain.memory["movelists"], f"{name} not in memory's movelists."    
        for movename in self.brain.memory["movelists"][name]:
            self.perform_move(movename)
    