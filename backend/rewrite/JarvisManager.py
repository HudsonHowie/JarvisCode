from jarvisBrain import JarvisBrain
from jarvisMotors import JarvisMotors


class JarvisManager:

    motors: JarvisMotors
    brain: JarvisBrain


    def __init__(self, controller: JarvisMotors, brain: JarvisBrain):
        self.motors = controller
        self.brain = brain


    def goto_move(self, name: str):
        assert name in self.brain.memory["movements"], f"{name} not in memory's moveset."    
     
        tmp = self.brain.memory["movements"][name]
        index = 0  
        for motor in self.motors.config["motors"]:
            self.motors.move_motor(motor, tmp[index])
            index += 1

    def perform_movelist(self, name: str):
        assert name in self.brain.memory["movelists"], f"{name} not in memory's movelists."    
        for movename in self.brain.memory["movelists"][name]:
            self.goto_move(movename)
    