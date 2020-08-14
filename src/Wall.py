import pygame
import numpy as np
import math

from Line import Line

class Wall:
    def __init__(self, pts, angle, color, t):
        self.color = color
        self.t = t

        self.selected = False

        self.angle = angle
        self.pts = pts

        A = 0.0
        n = len(self.pts)
        for i in range(n):
            A += self.pts[i][0]*self.pts[(i+1)%n][1]-self.pts[(i+1)%n][0]*self.pts[i][1]
        A /= 2
        c_x = 0.0
        c_y = 0.0
        for i in range(n):
            c_x += (self.pts[i][0]+self.pts[(i+1)%n][0])*(self.pts[i][0]*self.pts[(i+1)%n][1]-self.pts[(i+1)%n][0]*self.pts[i][1])
            c_y += (self.pts[i][1]+self.pts[(i+1)%n][1])*(self.pts[i][0]*self.pts[(i+1)%n][1]-self.pts[(i+1)%n][0]*self.pts[i][1])
        if A != 0:
            c_x /= (A*6)
            c_y /= (A*6)
        else:
            c_x = pts[0][0]
            c_y = pts[0][1]

        self.centroid = np.array([c_x, c_y])

        self.rot_pts()

        self.rel_pts = [p - self.centroid for p in pts] 
        
        self.lines = []
        for i in range(len(pts)):
            self.lines.append(Line(self.pts[i], self.pts[(i+1)%len(self.pts)]))

        self.turnes = []
        for i in range(len(self.lines)):
            self.turnes.append(self.lines[i].check_side(self.lines[i-1].P1))

        self.convex_lines = []
        self.triangles_cut = []

        self.detect_hitbox()

    def detect_hitbox(self):
        self.triangles_cut = []
        self.convex_lines = self.lines.copy()
        found = True
        while found:
            found = False
            for i in range(len(self.convex_lines)):
                if self.convex_lines[i].turn == "left" and self.convex_lines[(i+1)%len(self.convex_lines)].turn == "right":
                    found = True
                    self.triangles_cut.append([self.convex_lines[i], self.convex_lines[(i+1)%len(self.convex_lines)], Line(self.convex_lines[(i+1)%len(self.convex_lines)].P2, self.convex_lines[i].P1)])
                    if i == len(self.convex_lines)-1:
                        self.convex_lines = self.convex_lines[1:i] + [Line(self.convex_lines[i].P1, self.convex_lines[(i+1)%len(self.convex_lines)].P2)]
                    else:
                        self.convex_lines = self.convex_lines[:i] + [Line(self.convex_lines[i].P1, self.convex_lines[(i+1)%len(self.convex_lines)].P2)] + self.convex_lines[(i+2):]
                    break
                
    def update_pts(self):
        for i in range(len(self.pts)):
            self.pts[i] = self.rel_pts[i] + self.centroid
        self.rot_pts()
        for i in range(len(self.lines)):
            self.lines[i] = Line(self.pts[i], self.pts[(i+1)%len(self.pts)])
            self.lines[i].turn = self.turnes[i]
        self.detect_hitbox()
        
    def rot_pts(self):
        rot_mat = [[math.cos(self.angle), -math.sin(self.angle)],[math.sin(self.angle), math.cos(self.angle)]]
        for i in range(len(self.pts)):
            self.pts[i] = np.dot(rot_mat, self.pts[i]-self.centroid)+self.centroid

    def draw_collider(self, window, sett):
        for line in self.lines:
            line.draw(window, sett.BLUE)

    def collide_circle(self, c):
        for line in self.lines:
            line.collide_circle(c)

    def detect_click(self, mouse_pos):
        for t in self.triangles_cut:
            cnt = 0
            for line in t:
                if line.check_side(mouse_pos) == "right":
                    cnt += 1
            if cnt == 3:
                return False
        
        for line in self.convex_lines:
            if line.check_side(mouse_pos) == "right":
                return False
        return True

    def update(self):
        self.update_pts()
    
    def draw(self, window, sett):
        pts_draw = [[int(x[0]), int(x[1])] for x in self.pts]
        pygame.draw.polygon(window, self.color, pts_draw)
        '''
        for line in self.convex_lines:
            line.draw(window, sett.BLUE)
        for t in self.triangles_cut:
            for line in t:
                line.draw(window, sett.GREEN)
        '''
        '''
        if self.selected:
            self.draw_collider(window, sett)

        '''
        
