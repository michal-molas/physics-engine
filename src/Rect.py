import pygame
from settings import *
from Shape import Shape

class Rect(Shape):
    def __init__(self, P1, P2, color):
        self.w = abs(P1[0]-P2[0])
        self.h = abs(P1[1]-P2[1])
        super().__init__(P1, P2, color)

    def update_pts(self):
        self.A = [int(self.rel_pos[0] - self.w//2), int(self.rel_pos[1] - self.h//2)]
        self.B = [int(self.rel_pos[0] - self.w//2), int(self.rel_pos[1] + self.h//2)]
        self.C = [int(self.rel_pos[0] + self.w//2), int(self.rel_pos[1] + self.h//2)]
        self.D = [int(self.rel_pos[0] + self.w//2), int(self.rel_pos[1] - self.h//2)]

    def collide_floor(self):
        if self.rel_pos[1] >= S_HEIGHT - FLOOR_H - self.h//2:
            self.vel *= 0
            self.rel_pos[1] = S_HEIGHT - FLOOR_H - self.h//2

    def draw(self, window):
        pygame.draw.polygon(window, self.color, [self.A, self.B, self.C, self.D])
