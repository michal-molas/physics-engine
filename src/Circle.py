import pygame

import math
import numpy as np
from Shape import Shape
from Line import Line

class Circle(Shape):
    def __init__(self, P1, P2, color, t, sett):
        self.r = math.sqrt(pow(P1[0]-P2[0], 2) + pow(P1[1] - P2[1], 2))/2
        self.m = sett.DENS*math.pi*pow(self.r, 2)
        if self.m == 0:
            self.m = 0.0001
        super().__init__(P1, P2, color, t, sett)

    def update_pts(self):
        self.S = self.rel_pos

    def cw_collide(self, P1, P2, P3, P4, line12, line13, line24):
        d = line12.dist(self.S)
        c12 = line12.compare(self.S)
        if P1[0] != P2[0]:
            if (P1[0]-P2[0]) * c12 <= 0:
                return
        else:
            if (P1[1]-P2[1]) * c12 >= 0:
                return

        c13 = line13.compare(self.S)
        if P1[0] != P3[0]:
            if (P1[0]-P3[0]) * c13 <= 0:
                return
        else:
            if (P1[1]-P3[1]) * c13 >= 0:
                return

        c24 = line24.compare(self.S)
        if P2[0] != P4[0]:
            if (P2[0]-P4[0]) * c24 >= 0:
                return
        else:
            if (P2[1]-P4[1]) * c24 <= 0:
                return
        if d <= self.r:
            t = P2-P1
            ut = t/np.linalg.norm(t)
            un = np.array([-ut[1], ut[0]])

            self.rel_pos -= un*(self.r-d)

            vn_s = np.dot(un, self.vel)
            vt_s = np.dot(ut, self.vel)

            vn_sp = -vn_s
            vt_sp = vt_s

            vn_p = vn_sp*un
            vt_p = vt_sp*ut

            self.vel = vn_p + vt_p

    def ccorners_collide(self, w):
        corners = [w.A, w.B, w.C, w.D]
        for corn in corners:
            n = self.S - corn
            n_m = np.linalg.norm(n)
            if n_m <= self.r:
                un = n/n_m
                ut = np.array([-un[1], un[0]])

                self.rel_pos += un*(self.r-n_m)

                vn_s = np.dot(un, self.vel)
                vt_s = np.dot(ut, self.vel)

                vn_sp = -vn_s
                vt_sp = vt_s

                vn_p = vn_sp*un
                vt_p = vt_sp*ut

                self.vel = vn_p + vt_p

    def collide_walls(self, walls, sett):
        if self.rel_pos[1] >= sett.S_HEIGHT - sett.FLOOR_H - self.r:
            self.vel[1] *= -1
            self.rel_pos[1] = sett.S_HEIGHT - sett.FLOOR_H - self.r
        if self.rel_pos[1] <= self.r:
            self.vel[1] *= -1
            self.rel_pos[1] = self.r
        if self.rel_pos[0] <= sett.TB_WIDTH + self.r:
            self.vel[0] *= -1
            self.rel_pos[0] = sett.TB_WIDTH + self.r
        if self.rel_pos[0] >= sett.S_WIDTH - self.r:
            self.vel[0] *= -1
            self.rel_pos[0] = sett.S_WIDTH - self.r
        
        for w in walls:        
            ##AB
            self.cw_collide(w.A, w.B, w.D, w.C, w.lineAB, w.lineDA, w.lineBC)
            ##BC
            self.cw_collide(w.B, w.C, w.A, w.D, w.lineBC, w.lineAB, w.lineCD)  
            ##CD
            self.cw_collide(w.C, w.D, w.B, w.A, w.lineCD, w.lineBC, w.lineDA) 
            ##DA
            self.cw_collide(w.D, w.A, w.C, w.B, w.lineDA, w.lineCD, w.lineAB)
            self.ccorners_collide(w)
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [int(self.S[0]), int(self.S[1])], int(self.r))

