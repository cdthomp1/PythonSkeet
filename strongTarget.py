import arcade
import random
from globals import *
from target import Target

class StrongTarget(Target):

    def __init__(self):
        super().__init__()
        
        self.radius = TARGET_RADIUS

        self.velocity.dx = random.randint(1,3)
        self.velocity.dy = random.randint(-2,3)
        self.lives = 3
        self.hits = 0
    
    """ The draw function the tough bird, with a radius of 15 with 
    a score that is set to 3 """
    def draw(self):
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y, TARGET_COLOR, font_size=20)
    
    """ This is the hit function. This subtracts one from the score 
    every time the bird gets hit. Then if the score reaches zero
    then the hit tally gets 2 extra points. """
    def hit(self):

        if self.hits < 2:
            self.hits += 1
            self.lives -= 1
        else:
            self.lives -= 1
        
        if self.lives == 0:
            self.alive = False
            self.hits += 5
        return self.hits
