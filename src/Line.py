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

        self.side = "right"

    def dist(self, P):
        return abs(self.A*P[0]+self.B*P[1]+self.C)/math.sqrt(self.A**2+self.B**2)

    def compare(self, P):
        #1 - above/right
        #-1 - below/left
        #0 - at
        if self.B != 0:
            f = (-self.A*P[0]-self.C)/self.B
            return np.sign(P[1]-f)
        else:
            if abs(self.A) < 0.00001:
                self.A = 0.00001
            f = -self.C/self.A
            return np.sign(P[0]-f)

    def check_side(self, P):
        if [P[0], P[1]] != [self.P1[0], self.P1[1]] and [P[0], P[1]] != [self.P2[0], self.P2[1]]:
            val = self.compare(P)
            if self.P1[0] != self.P2[0]:
                if (self.P1[0]-self.P2[0])*val <= 0:
                    return "left"
                else:
                    return "right"
            else:
                if (self.P1[1]-self.P2[1])*val >= 0:
                    return "left"
                else:
                    return "right"

    def approx_result(self, line):
        if self.A*line.B-line.A*line.B == 0:
            return
        line1 = self
        line2 = line
        if self.B == 0:
            line1, line2 = line2, line1
        if line1.compare(line2.P1) == -line1.compare(line2.P2):
            P1 = line2.P1
            P2 = line2.P2
            for i in range(30):
                half_P = np.array([(P1[0]+P2[0])/2, (P1[1] + P2[1])/2])
                if line1.compare(half_P) == -line1.compare(P1):
                    P2 = half_P
                else:
                    P1 = half_P
            return P1
        return

    def check_intersection(self, line):
        res = self.approx_result(line)
        if res is None:
            return False
        else:
            line1 = self
            line2 = line
            if self.B == 0:
                line1, line2 = line2, line1
            if line1.P1[0] > line1.P2[0]:
                if res[0] <= line1.P1[0] and res[0] >= line1.P2[0]:
                    return True
            else:
                if res[0] >= line1.P1[0] and res[0] <= line1.P2[0]:
                    return True
            return False

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

