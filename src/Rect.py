import pygame
import sympy as sym

from settings import *
from Shape import Shape

class Rect(Shape):
    def __init__(self, P1, P2, color, t):
        self.w = abs(P1[0]-P2[0])
        self.h = abs(P1[1]-P2[1])
        super().__init__(P1, P2, color, t)

    def update_pts(self):
        self.A = [self.rel_pos[0] - self.w//2, self.rel_pos[1] - self.h//2]
        self.B = [self.rel_pos[0] - self.w//2, self.rel_pos[1] + self.h//2]
        self.C = [self.rel_pos[0] + self.w//2, self.rel_pos[1] + self.h//2]
        self.D = [self.rel_pos[0] + self.w//2, self.rel_pos[1] - self.h//2]
        
    def check_collisions(self, shapes):
        for s in shapes:
            pass

    def collide(self, shape):
        self.vel *= -1
    
    def collide_walls(self):
        if self.rel_pos[1] >= S_HEIGHT - FLOOR_H - self.h/2:
            self.vel *= -1
            self.rel_pos[1] = S_HEIGHT - FLOOR_H - self.h/2

    def draw(self, window):
        pts = [[int(self.A[0]), int(self.A[1])], [int(self.B[0]), int(self.B[1])], [int(self.C[0]), int(self.C[1])], [int(self.D[0]), int(self.D[1])]]
        pygame.draw.polygon(window, self.color, pts)
