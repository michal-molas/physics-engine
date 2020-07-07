import pygame
from settings import *
import numpy as np

class Shape:
    def __init__(self, P1, P2, color, t):
        self.color = color
        self.t = t

        self.acc = np.array([0.0, G])
        self.vel = np.array([0.0, 0.0])
        self.rel_pos = np.array([(P1[0]+P2[0])/2, (P1[1]+P2[1])/2])

        self.update_pts()

    def change_vel(self):
        self.vel += self.acc*DT

    def move(self):
        self.rel_pos[0] += self.vel[0]*DT + self.acc[0]*DT*DT/2
        self.rel_pos[1] += self.vel[1]*DT + self.acc[1]*DT*DT/2

    def update(self, shapes):
        self.move()
        self.change_vel()
        self.check_collisions(shapes)
        self.collide_floor()
        self.update_pts()

        
        
        

    
