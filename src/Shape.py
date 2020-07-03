import pygame
from settings import *
import numpy as np


class Shape:
    def __init__(self, P1, P2, color):
        self.color = color
        
        self.vel = np.array([0.0, 0.0])
        self.rel_pos = np.array([(P1[0]+P2[0])//2, (P1[1]+P2[1])//2])

        self.update_pts()

    def move(self, d, mag):
        if mag != 0:
            self.rel_pos += d * mag

    def gravity(self):
        self.vel += [0, G*DT]
        dy = int(self.vel[1] * DT + (G * DT * DT)/2)
        self.move(DOWN, dy)

    def update(self):
        self.gravity()
        self.collide_floor()
        self.update_pts()
        
        
        

    
