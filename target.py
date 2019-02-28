import arcade
from abc import ABC
from abc import abstractmethod
from point import Point
from velocity import Velocity
from globals import *
import math
import random
from flying_object import Flying_Object

import globals

class Target(Flying_Object, ABC):

    def __init__(self):
        super().__init__()
        self.center.y = random.randint(10, 490)
    
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def hit(self):
        pass