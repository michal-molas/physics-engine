import pygame
import numpy as np
import math

from Line import Line

class Wall:
    def __init__(self, P1, P2, angle, color, t):
        self.color = color
        self.t = t

        self.angle = angle
        self.A = np.array([P1[0], P1[1]])
        self.C = np.array([P2[0], P2[1]])
        if P1[0] < P2[0]:
            if P1[1] < P2[1]:
                self.B = np.array([P2[0], P1[1]])
                self.D = np.array([P1[0], P2[1]])
            else:
                self.B = np.array([P1[0], P2[1]])
                self.D = np.array([P2[0], P1[1]])
        else:
            if P1[1] < P2[1]:
                self.B = np.array([P1[0], P2[1]])
                self.D = np.array([P2[0], P1[1]])
            else:
                self.B = np.array([P2[0], P1[1]])
                self.D = np.array([P1[0], P2[1]])

        self.rot_pts()
        
        self.lineAB = Line(self.A, self.B)
        self.lineBC = Line(self.B, self.C)
        self.lineCD = Line(self.C, self.D)
        self.lineDA = Line(self.D, self.A)

        self.w = np.linalg.norm(self.A-self.B)
        self.h = np.linalg.norm(self.B-self.C)

        self.S = np.array([(P1[0]+P2[0])/2, (P1[1]+P2[1])/2])
    
    def rot_pts(self):
        rot_mat = [[math.cos(self.angle), -math.sin(self.angle)],[math.sin(self.angle), math.cos(self.angle)]]
        self.A = np.dot(rot_mat, self.A-self.C)+self.C
        self.B = np.dot(rot_mat, self.B-self.C)+self.C
        self.D = np.dot(rot_mat, self.D-self.C)+self.C

    def draw_collider(self, window):
        self.lineAB.draw(window)
        self.lineBC.draw(window)
        self.lineCD.draw(window)
        self.lineDA.draw(window)

    def draw(self, window):
        pts = [[int(self.A[0]), int(self.A[1])], [int(self.B[0]), int(self.B[1])], [int(self.C[0]), int(self.C[1])], [int(self.D[0]), int(self.D[1])]]
        pygame.draw.polygon(window, self.color, pts)
        #self.draw_collider(window)
        
