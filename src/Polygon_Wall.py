import pygame
import numpy as np
import math

from Wall import Wall
from Line import Line

class Polygon_Wall(Wall):
    def __init__(self, pts, angle, color, t, win):
        rev = False
        if Line(pts[0], pts[1]).check_side(pts[2]) == "right":
            #pts.reverse()
            rev = not rev
        start_side = "left" if rev else "right"
        other_side = "right" if start_side == "left" else "left"
        for i in range(3, len(pts)):
            side = start_side if i%2 == 0 else other_side
            line1 = Line(pts[i-2], pts[0])
            line2 = Line(pts[i-1], pts[i-2])
            if line1.check_side(pts[i]) == side and line2.check_side(pts[i]) == side:
                rev = not rev
            else:
                break
        '''        
        if len(pts) % 2 == 0:
            line1 = Line(pts[len(pts)-3], pts[0])
            line2 = Line(pts[len(pts)-2], pts[len(pts)-3])
            line1.draw(win, (0,255,0))
            line2.draw(win, (0,255,0))
            if line1.check_side(pts[len(pts)-1]) == "right" and line2.check_side(pts[len(pts)-1]) == "right":
                rev = not rev
                #pts.reverse()
        '''
        if rev:
            pts.reverse()
        super().__init__(pts, angle, color, t)
