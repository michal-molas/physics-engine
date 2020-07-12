import pygame
import numpy as np
import math

from Circle import Circle
from Wall import Wall

class User:
    def __init__(self, sett):
        self.lm_pressed = False
        self.rm_pressed = False

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
                            if self.sel_shape == "Circle":
                                return Circle(self.start_pos, self.end_pos, self.sel_color, self.sel_shape, sett)
                            elif self.sel_shape == "Wall":
                                return Wall(self.start_pos, self.end_pos, self.angle, self.sel_color, self.sel_shape)
            if self.lm_pressed:
                if self.sel_shape == "Circle":
                    Circle(self.start_pos, pygame.mouse.get_pos(), self.sel_color, self.sel_shape, sett).draw(window)
                elif self.sel_shape == "Wall":
                    Wall(self.start_pos, pygame.mouse.get_pos(), self.angle, self.sel_color, self.sel_shape).draw(window)
        return None

    def rotate_wall(self, events):
        if self.lm_pressed and self.sel_shape == "Wall":
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.angle = (self.angle+math.pi/12)%(2*math.pi)
                    if event.button == 5:
                        self.angle = (self.angle-math.pi/12)%(2*math.pi)

    def change_shape(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.sel_shape = "Circle"
                if event.key == pygame.K_2:
                    self.sel_shape = "Wall"

    def update(self, events, window, shapes, walls, sett):
        self.change_shape(events)
        self.rotate_wall(events)
        s = self.draw_shape(events, window, sett)
        if s is not None:
            if s.t == "Circle":
                shapes.append(s)
                self.stert_pos = None
                self.end_pos = None
            elif s.t == "Wall":
                self.angle = 0.0
                walls.append(s)
                self.stert_pos = None
                self.end_pos = None
            
