import pygame

import math
from Shape import Shape

class Circle(Shape):
    def __init__(self, P1, P2, color, t, sett):
        self.r = math.sqrt(pow(P1[0]-P2[0], 2) + pow(P1[1] - P2[1], 2))/2
        self.m = sett.DENS*math.pi*pow(self.r, 2)
        if self.m == 0:
            self.m = 0.0001
        super().__init__(P1, P2, color, t, sett)

    def update_pts(self):
        self.S = [self.rel_pos[0], self.rel_pos[1]]

    def collide_walls(self, sett):
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
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [int(self.S[0]), int(self.S[1])], int(self.r))

