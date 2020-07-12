import pygame
from settings import *
import numpy as np

class Shape:
    def __init__(self, P1, P2, color, t, sett):
        self.color = color
        self.t = t

        self.F_g = np.array([0.0, self.m*sett.G])
        self.F_e = np.array([0.0, 0.0])

        self.F_res = self.F_g + self.F_e

        self.acc = self.F_res/self.m
        self.vel = np.array([0.0, 0.0])
        self.rel_pos = np.array([(P1[0]+P2[0])/2, (P1[1]+P2[1])/2])

        self.update_pts()

    def update_forces(self, sett):
        self.F_g = np.array([0.0, self.m*sett.G])
        self.F_e = np.array([0.0, 0.0])

        self.F_res = self.F_g + self.F_e

        self.acc = self.F_res/self.m

    def change_vel(self, sett):
        self.vel += self.acc*sett.DT

    def move(self, sett):
        self.rel_pos[0] += self.vel[0]*sett.DT + self.acc[0]*sett.DT*sett.DT/2
        self.rel_pos[1] += self.vel[1]*sett.DT + self.acc[1]*sett.DT*sett.DT/2

    def update(self, events, shapes, sett):
        self.F_res = self.F_g + self.F_e
        self.acc = self.F_res/self.m

        self.update_forces(sett)
        self.move(sett)
        self.change_vel(sett)
        self.update_pts()
        

        
        
        

    
