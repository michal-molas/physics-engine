import pygame
import numpy as np
import math

from Wall import Wall
from Line import Line

class Polygon_Wall(Wall):
    def __init__(self, pts, angle, color, t):
        if Line(pts[0], pts[1]).check_side(pts[2]) == "right":
            pts.reverse()
        super().__init__(pts, angle, color, t)
