import pygame
import numpy as np
import math

from Wall import Wall

class Triangle_Wall(Wall):
    def __init__(self, P1, P2, angle, color, t):
        A = np.array([P1[0], P1[1]])
        vec = np.array([P2[0], P2[1]])-np.array([P1[0], P1[1]])
        B = A + vec + np.array([vec[1], -vec[0]])/math.sqrt(3)
        C = A + vec + np.array([-vec[1], vec[0]])/math.sqrt(3)
        pts = [A, B, C] 
        super().__init__(P1, P2, pts, angle, color, t)
