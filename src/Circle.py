import pygame

import math
import numpy as np
from Shape import Shape
from Line import Line

class Circle(Shape):
    def __init__(self, P1, P2, color, t, sett):
        self.r = math.sqrt(pow(P1[0]-P2[0], 2) + pow(P1[1] - P2[1], 2))/2
        self.m = sett.DENS*math.pi*pow(self.r, 2)
        if self.m == 0:
            self.m = 0.0001
        super().__init__(P1, P2, color, t, sett)

    def update_pts(self):
        self.S = self.rel_pos

    def corners_collide(self, w):
        for corn in w.pts:
            n = self.S - corn
            n_m = np.linalg.norm(n)
            if n_m <= self.r:
                un = n/n_m
                ut = np.array([-un[1], un[0]])

                self.rel_pos += un*(self.r-n_m)

                vn_s = np.dot(un, self.vel)
                vt_s = np.dot(ut, self.vel)

                vn_sp = -vn_s
                vt_sp = vt_s

                vn_p = vn_sp*un
                vt_p = vt_sp*ut

                self.vel = vn_p + vt_p

    def collide_walls(self, walls, sett):
        if self.rel_pos[1] >= sett.S_HEIGHT - sett.FLOOR_H - self.r:
            self.vel[1] *= -1
            self.rel_pos[1] = sett.S_HEIGHT - sett.FLOOR_H - self.r
        if self.rel_pos[1] <= self.r:
            self.vel[1] *= -1
            self.rel_pos[1] = self.r
        if self.rel_pos[0] <= sett.TB_WIDTH + self.r:
            self.vel[0] *= -1
            self.rel_pos[0] = sett.TB_WIDTH + self.r
        if self.rel_pos[0] >= sett.S_WIDTH - self.r:
            self.vel[0] *= -1
            self.rel_pos[0] = sett.S_WIDTH - self.r
        
        for w in walls:
            w.collide_circle(self)       
            self.corners_collide(w)
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [int(self.S[0]), int(self.S[1])], int(self.r))

