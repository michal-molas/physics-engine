import pygame
import numpy as np
import math

from Wall import Wall

class Polygon_Wall(Wall):
    def __init__(self, pts, angle, color, t):
        super().__init__(pts, angle, color, t)
