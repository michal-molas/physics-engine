import pygame
import sympy as sym

import math
from settings import *
from Shape import Shape

class Circle(Shape):
    def __init__(self, P1, P2, color, t):
        self.r = math.sqrt(pow(P1[0]-P2[0], 2) + pow(P1[1] - P2[1], 2))/2
        super().__init__(P1, P2, color, t)

    def update_pts(self):
        self.S = [self.rel_pos[0], self.rel_pos[1]]

    def check_collisions(self, shapes):
        for s in shapes:
            if s is not self:
                if s.t == "Circle":
                    dist = math.sqrt((self.S[0]-s.S[0])**2 + (self.S[1]-s.S[1])**2)
                    if dist <= s.r + self.r:
                        x = s.r + self.r - dist
                        if s.S[0] != self.S[0]:
                            alpha = math.atan((s.S[1]-self.S[1])/(s.S[0]-self.S[0]))
                        else:
                            alpha = math.pi/2
                        self.rel_pos[0] += x*math.cos(alpha)
                        self.rel_pos[1] += x*math.sin(alpha)
                        self.collide(s)

    def collide(self, s):
        if s.S[0] != self.S[0]:
            phi = math.atan((s.S[1] - self.S[1])/(s.S[0]-self.S[0]))
        else:
            phi = math.pi/2
        if self.vel[0] != 0.0:
            theta1 = math.atan(self.vel[1]/self.vel[0])
        else:
            theta1 = math.pi/2
        if s.vel[0] != 0.0:
            theta2 = math.atan(s.vel[1]/s.vel[0])
        else:
            theta2 = math.pi/2
        v1 = math.sqrt(self.vel[0]**2 + self.vel[1]**2)
        v2 = math.sqrt(s.vel[0]**2 + s.vel[1]**2)
        m1 = DENS*math.pi*pow(self.r, 2)
        m2 = DENS*math.pi*pow(s.r, 2)
        
        vx = v1*math.cos(theta1-phi)*(m1-m2)+2*m2*v2*math.cos(theta2-phi)
        vx = vx/(m1+m2)*math.cos(phi)
        vx += v1*math.sin(theta1-phi)*math.cos(phi+math.pi/2)

        vy = v1*math.cos(theta1-phi)*(m1-m2)+2*m2*v2*math.cos(theta2-phi)
        vy = vy/(m1+m2)*math.sin(phi)
        vy += v1*math.sin(theta1-phi)*math.sin(phi+math.pi/2)

        self.vel = np.array([vx, vy])

    def collide_floor(self):
        if self.rel_pos[1] >= S_HEIGHT - FLOOR_H - self.r:
            self.vel[1] *= -1
            self.rel_pos[1] = S_HEIGHT - FLOOR_H - self.r

    def draw(self, window):
        pygame.draw.circle(window, self.color, [int(self.S[0]), int(self.S[1])], int(self.r))

