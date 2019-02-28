from globals import *
from flying_object import Flying_Object
import arcade
import math

class Bullet(Flying_Object):

    def __init__(self):
        super().__init__()
        self.speed = 10
        self.alive = True
        self.radius = BULLET_RADIUS


    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, BULLET_RADIUS, arcade.color.BLACK_OLIVE)

    def fire(self, angle):
        self.velocity.dx = math.cos(math.radians(angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(angle)) * self.speed