import pygame
import math
from settings import *

class Circle:
    def __init__(self, P1, P2, color):
        self.S = [P1[0], P1[1]]
        self.r = int(math.sqrt(pow(P1[0]-P2[0], 2) + pow(P1[1] - P2[1], 2)))
        self.color = color
        
        self.vel = 0

    def gravity(self):
        self.vel += G*DT
        dx = int(self.vel * DT + (G * DT * DT)/2)
        self.S[1] += dx

    def update(self):
        self.gravity()

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.S, self.r)
