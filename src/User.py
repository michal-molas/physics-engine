import pygame
from Rect import Rect
from settings import *
from Circle import Circle

class User:
    def __init__(self):
        self.lm_pressed = False
        self.rm_pressed = False

        self.sel_shape = "Rect"
        self.sel_color = RED
        
        self.start_pos = None
        self.end_pos = None

    def draw_shape(self, events, window):
        if not self.rm_pressed:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        m_pos = pygame.mouse.get_pos()
                        if m_pos[0] > TB_WIDTH:
                            self.start_pos = m_pos
                            self.lm_pressed = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.lm_pressed:
                            self.end_pos = pygame.mouse.get_pos()
                            self.lm_pressed = False
                            if self.sel_shape == "Rect":
                                return Rect(self.start_pos, self.end_pos, self.sel_color)
                            elif self.sel_shape == "Circle":
                                return Circle(self.start_pos, self.end_pos, self.sel_color)
            if self.lm_pressed:
                if self.sel_shape == "Rect":
                    Rect(self.start_pos, pygame.mouse.get_pos(), self.sel_color).draw(window)
                elif self.sel_shape == "Circle":
                    Circle(self.start_pos, pygame.mouse.get_pos(), self.sel_color).draw(window)
        return None

    def change_shape(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.sel_shape = "Rect"
                if event.key == pygame.K_2:
                    self.sel_shape = "Circle"

    def update(self, events, window, shapes):
        self.change_shape(events)
        s = self.draw_shape(events, window)
        if s is not None:
            shapes.append(s)
            self.stert_pos = None
            self.end_pos = None
            
                
                
            
