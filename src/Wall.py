import pygame
import numpy as np
import math

from Line import Line

class Wall:
    def __init__(self, P1, P2, pts, angle, color, t):
        self.color = color
        self.t = t

        self.P_s = np.array([P1[0], P1[1]])
        self.P_e = np.array([P2[0], P2[1]])

        self.angle = angle
        self.pts = pts

        self.rot_pts()
        
        self.lines = []
        for i in range(len(pts)):
            self.lines.append(Line(self.pts[i], self.pts[(i+1)%len(self.pts)]))
    
    def rot_pts(self):
        rot_mat = [[math.cos(self.angle), -math.sin(self.angle)],[math.sin(self.angle), math.cos(self.angle)]]
        for i in range(len(self.pts)):
            self.pts[i] = np.dot(rot_mat, self.pts[i]-self.P_e)+self.P_e

    def draw_collider(self, window):
        for line in self.lines:
            line.draw(window, (0,0,255))

    def collide_circle(self, c):
        for line in self.lines:
            line.collide_circle(c)

    def draw(self, window):
        pts_draw = [[int(x[0]), int(x[1])] for x in self.pts]
        pygame.draw.polygon(window, self.color, pts_draw)
        #self.draw_collider(window)
        
