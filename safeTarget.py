import arcade
import random
from globals import *
from target import Target

class SafeTarget(Target):

    def __init__(self):
        super().__init__()
        self.radius = TARGET_SAFE_RADIUS

        self.velocity.dx = random.randint(1,5)
        self.velocity.dy = random.randint(-2,5)

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, TARGET_SAFE_RADIUS, TARGET_SAFE_RADIUS, arcade.color.AIR_FORCE_BLUE)

    def hit(self):
        self.alive = False
        return -10