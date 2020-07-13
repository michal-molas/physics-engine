import math
import numpy as np
import pygame
  
class Line:
    def __init__(self, P1, P2):
        self.A = P2[1] - P1[1]
        self.B = P1[0] - P2[0]
        self.C = P2[0]*P1[1]-P1[0]*P2[1]

        self.P1 = P1 #[P1[0], P1[1]]
        self.P2 = P2 #[P2[0], P2[1]]

    def dist(self, P):
        return abs(self.A*P[0]+self.B*P[1]+self.C)/math.sqrt(self.A**2+self.B**2)

    def compare(self, P):
        #1 - above/right
        #-1 - below/left
        #0 - at
        #(reversed y coordinate!)
        if self.B != 0:
            f = (-self.A*P[0]-self.C)/self.B
            return np.sign(P[1]-f)
        else:
            f = -self.C/self.A
            return np.sign(P[0]-f)

    def collide_circle(self, c):
        d = self.dist(c.S)
        vec = self.P2-self.P1
        perp_vec = np.array([vec[1], -vec[0]])
        line1 = Line(self.P2, self.P2 + perp_vec)
        line2 = Line(self.P1 + perp_vec, self.P1)
        for line in [self, line1, line2]:
            com_line = line.compare(c.S)
            if line.P1[0] != line.P2[0]:
                if (line.P1[0]-line.P2[0]) * com_line <= 0:
                    return
            else:
                if (line.P1[1]-line.P2[1]) * com_line >= 0:
                    return
            
        if d <= c.r:
            t = self.P2-self.P1
            ut = t/np.linalg.norm(t)
            un = np.array([-ut[1], ut[0]])

            c.rel_pos -= un*(c.r-d)

            vn_s = np.dot(un, c.vel)
            vt_s = np.dot(ut, c.vel)

            vn_sp = -vn_s
            vt_sp = vt_s

            vn_p = vn_sp*un
            vt_p = vt_sp*ut

            c.vel = vn_p + vt_p

    def draw(self, window, col):
        pygame.draw.line(window, col, self.P1, self.P2, 2) 

