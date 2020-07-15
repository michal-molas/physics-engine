import pygame
import numpy as np
import math

from Wall import Wall

class Rect_Wall(Wall):
    def __init__(self, P1, P2, angle, color, t):
        A = np.array([P1[0], P1[1]])
        C = np.array([P2[0], P2[1]])
        if P1[0] < P2[0]:
            if P1[1] < P2[1]:
                B = np.array([P2[0], P1[1]])
                D = np.array([P1[0], P2[1]])
            else:
                B = np.array([P1[0], P2[1]])
                D = np.array([P2[0], P1[1]])
        else:
            if P1[1] < P2[1]:
                B = np.array([P1[0], P2[1]])
                D = np.array([P2[0], P1[1]])
            else:
                B = np.array([P2[0], P1[1]])
                D = np.array([P1[0], P2[1]])
        pts = [A, B, C, D] 
        super().__init__(pts, angle, color, t)
