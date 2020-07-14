import pygame
import numpy as np
import math

from Circle import Circle
from Rect_Wall import Rect_Wall
from Triangle_Wall import Triangle_Wall

class User:
    def __init__(self, sett):
        self.lm_pressed = False
        self.rm_pressed = False

        self.holding = False

        self.sel_shape = "Circle"
        self.sel_color = sett.RED
        
        self.start_pos = None
        self.end_pos = None

        self.angle = 0.0

    def draw_shape(self, events, window, sett):
        if not self.rm_pressed:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        m_pos = pygame.mouse.get_pos()
                        if m_pos[0] > sett.TB_WIDTH:
                            self.start_pos = m_pos
                            self.lm_pressed = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.lm_pressed:
                            self.end_pos = pygame.mouse.get_pos()
                            self.lm_pressed = False
                            if abs(self.end_pos[1]-self.start_pos[1])>10 and abs(self.end_pos[0]-self.start_pos[0])>10:
                                if self.sel_shape == "Circle":
                                    return Circle(self.start_pos, self.end_pos, self.sel_color, self.sel_shape, sett)
                                elif self.sel_shape == "Rect_Wall":
                                    return Rect_Wall(self.start_pos, self.end_pos, self.angle, self.sel_color, self.sel_shape)
                                elif self.sel_shape == "Triangle_Wall":
                                    return Triangle_Wall(self.start_pos, self.end_pos, self.angle, self.sel_color, self.sel_shape)
            if self.lm_pressed:
                if self.sel_shape == "Circle":
                    Circle(self.start_pos, pygame.mouse.get_pos(), self.sel_color, self.sel_shape, sett).draw(window)
                elif self.sel_shape == "Rect_Wall":
                    Rect_Wall(self.start_pos, pygame.mouse.get_pos(), self.angle, self.sel_color, self.sel_shape).draw(window, sett)
                elif self.sel_shape == "Triangle_Wall":
                    Triangle_Wall(self.start_pos, pygame.mouse.get_pos(), self.angle, self.sel_color, self.sel_shape).draw(window, sett)
        return None

    def click_wall(self, events, walls):
        if self.sel_shape == "Mouse":
            for event in events:
                m_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.lm_pressed = True
                        for w in walls:
                            if w.detect_click(m_pos):
                                if not w.selected:
                                    for wa in walls:
                                        wa.selected = False
                                    w.selected = True
                                    self.holding = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.lm_pressed = False
                        self.holding = False
                        for w in walls:
                            w.selected = False
                            w.update_pts()
            for w in walls:
                if w.selected:
                    m_pos = pygame.mouse.get_pos()
                    w.centroid = np.array([m_pos[0], m_pos[1]])
                    w.update_pts()
                    self.rotate_wall(events, walls)
                        
    def rotate_wall(self, events, walls):
        if self.lm_pressed:
            if self.sel_shape[-5:] == "_Wall":
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 4:
                            self.angle = (self.angle+math.pi/12)%(2*math.pi)
                        if event.button == 5:
                            self.angle = (self.angle-math.pi/12)%(2*math.pi)
                        return
            elif self.holding:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 4:
                            for w in walls:
                                if w.selected:
                                    w.angle = (w.angle+math.pi/12)%(2*math.pi)
                        if event.button == 5:
                            for w in walls:
                                if w.selected:
                                    w.angle = (w.angle-math.pi/12)%(2*math.pi)

    def change_shape(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    self.sel_shape = "Mouse"
                if event.key == pygame.K_1:
                    self.sel_shape = "Circle"
                if event.key == pygame.K_2:
                    self.sel_shape = "Rect_Wall"
                if event.key == pygame.K_3:
                    self.sel_shape = "Triangle_Wall"

    def update(self, events, window, shapes, walls, sett):
        self.click_wall(events, walls)
        self.change_shape(events)
        self.rotate_wall(events, walls)
        s = self.draw_shape(events, window, sett)
        if s is not None:
            if s.t == "Circle":
                shapes.append(s)
                self.stert_pos = None
                self.end_pos = None
            elif s.t[-5:] == "_Wall":
                self.angle = 0.0
                walls.append(s)
                self.stert_pos = None
                self.end_pos = None
            
