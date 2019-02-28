from globals import *
from target import Target
import random
import arcade
from point import Point

class StandardTarget(Target):
    def __init__(self):
        super().__init__()
        self.radius = TARGET_RADIUS

        self.velocity.dx = random.randint(1,5)
        self.velocity.dy = random.randint(-2,5)

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, TARGET_RADIUS, arcade.color.CARROT_ORANGE)

    def hit(self):
        self.alive = False
        return 1
        