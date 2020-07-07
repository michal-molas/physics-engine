import pygame

import math
from settings import *
from Shape import Shape

class Circle(Shape):
    def __init__(self, P1, P2, color, t):
        self.r = math.sqrt(pow(P1[0]-P2[0], 2) + pow(P1[1] - P2[1], 2))/2
        super().__init__(P1, P2, color, t)

    def update_pts(self):
        self.S = [self.rel_pos[0], self.rel_pos[1]]

    def collide_walls(self):
        if self.rel_pos[1] >= S_HEIGHT - FLOOR_H - self.r:
            self.vel[1] *= -1
            self.rel_pos[1] = S_HEIGHT - FLOOR_H - self.r
        if self.rel_pos[1] <= self.r:
            self.vel[1] *= -1
            self.rel_pos[1] = self.r
        if self.rel_pos[0] <= TB_WIDTH + self.r:
            self.vel[0] *= -1
            self.rel_pos[0] = TB_WIDTH + self.r
        if self.rel_pos[0] >= S_WIDTH - self.r:
            self.vel[0] *= -1
            self.rel_pos[0] = S_WIDTH - self.r
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [int(self.S[0]), int(self.S[1])], int(self.r))

