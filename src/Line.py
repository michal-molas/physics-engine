import math
import pygame
  
class Line:
    def __init__(self, P1, P2):
        self.A = P2[1] - P1[1]
        self.B = P1[0] - P2[0]
        self.C = P2[0]*P1[1]-P1[0]*P2[1]

        self.P1 = [P1[0], P1[1]]
        self.P2 = [P2[0], P2[1]]

        print(self.A, self.B, self.C)

        #self.slope = (P2[1]-P1[1])/(P2[0]-P1[0]) if P1[0] != P2[0] else None

    def dist(self, P):
        return abs(self.A*P[0]+self.B*P[1]+self.C)/math.sqrt(self.A**2+self.B**2)

    def compare(self, P):
        #1 - above/right
        #-1 - below/left
        #0 - 1at
        if self.B != 0:
            f = (-self.A*P[0]-self.C)/self.B
            if P[1] > f:
                return 1
            elif P[1] == f:
                return 0
            else:
                return -1
        else:
            f = -self.C/self.A
            if P[0] > f:
                return 1
            elif P[0] == f:
                return 0
            else:
                return -1

    def draw(self, window):
        pygame.draw.line(window, (0,0,255), self.P1, self.P2) 

