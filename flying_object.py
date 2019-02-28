import arcade
from abc import ABC
from abc import abstractmethod
from point import Point
from velocity import Velocity
from globals import *
import math


class Flying_Object(ABC):

    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0
        self.alive = True
        self.velocity = Velocity()
        self.velocity.dx = 0
        self.velocity.dy = 0

    @abstractmethod
    def draw(self):
        pass

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

        print("TARGET ADVANCE")

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if (self.center.y >= SCREEN_HEIGHT or self.center.x >= SCREEN_WIDTH):
            return True
        else:
            return False
       