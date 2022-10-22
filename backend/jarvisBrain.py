from typing import Any, Dict, Union

import numpy as np

from backend import jarvisFileReading


class JarvisBrain:

    memory: Dict[str, Any]

    def __init__(self):
        self.memory = jarvisFileReading.get_memory_numpy()
    
        
    def get_move_names(self) -> list[str]:
        return self.memory["movements"].keys()
    

    def get_movelist_names(self) -> list[str]:
        return self.memory["movelist"].keys()
 
    
    def get_moves(self) -> Dict[str, list[float]]:
        tmp: dict[str, 'np.ndarray[tuple, Any]'] = self.memory["movements"]

        tmp1 = dict()
        for (key, val) in tmp.items():
            tmp1[key] = val.tolist()
        return tmp1

         
    def get_movelists(self) -> Dict[str, list[str]]:
        return self.memory["movelists"]
 

    def get_moves_numpy(self) -> Dict[str, 'np.ndarray[tuple, Any]']:
        return self.memory["movements"]
    

    def has_move(self, name: str) -> bool:
        return name in self.memory["movements"]
    

    def has_movelist(self, name: str) -> bool:
        return name in self.memory["movelists"]
    
    def forget_move(self, name: str): 
        jarvisFileReading.delete_movement(name)

        # debugging, change to simple assignment when confirmed working.
        self.memory = jarvisFileReading.get_memory_numpy()
 
    def forget_movelist(self, name: str): 
        jarvisFileReading.delete_movelist(name)

        # debugging, change to simple assignment when confirmed working.
        self.memory = jarvisFileReading.get_memory_numpy()
 
    

    def teach_movement(self, name: str, movement: Union[list[float], 'np.ndarray[tuple, Any]']):
        jarvisFileReading.write_memory_point(name, movement)

        # debugging, change to simple assignment when confirmed working.
        self.memory = jarvisFileReading.get_memory_numpy()


    def teach_movelist(self, name: str, moves: list[str]):
        for nme in moves:
            assert nme in self.memory["movements"], f"Unknown move: \"{nme}\". Cannot build moveset without knowing all moves."
       
        jarvisFileReading.write_memory_movelist(name, moves)

         # debugging, change to simple assignment when confirmed working.
        self.memory = jarvisFileReading.get_memory_numpy()


    def teach_movelist_raw(self, name: str, moves: list['np.ndarray[tuple, Any]']):
        names: list[str] = []
        for idx, move in enumerate(moves):
            tmp = f"{name}_{idx}"
            self.teach_movement(tmp, move)
            names.append(tmp)

        self.teach_movelist(name, names)


