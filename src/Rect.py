import pygame
from settings import *

class Rect:
    def __init__(self, P1, P2, color):
        self.A = [P1[0], P1[1]]
        self.B = [P2[0], P1[1]]
        self.C = [P2[0], P2[1]]
        self.D = [P1[0], P2[1]]

        self.color = color

        self.vel = 0

    def gravity(self):
        self.vel += G*DT
        dx = int(self.vel * DT + (G * DT * DT)/2)
        self.A[1] += dx
        self.B[1] += dx
        self.C[1] += dx
        self.D[1] += dx
        
    def update(self):
        self.gravity()

    def draw(self, window):
        pygame.draw.polygon(window, self.color, [self.A, self.B, self.C, self.D])
