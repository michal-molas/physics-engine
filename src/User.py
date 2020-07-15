import pygame
import numpy as np
import math

from Circle import Circle
from Rect_Wall import Rect_Wall
from Triangle_Wall import Triangle_Wall
from Polygon_Wall import Polygon_Wall

class User:
    def __init__(self, sett):
        self.lm_pressed = False

        self.holding = False
        self.hold_shape = None
        
        self.poly_drawing = False
        self.poly_pts = []

        self.sel_shape = "Mouse"
        self.sel_color = sett.RED
        
        self.start_pos = None
        self.end_pos = None

        self.angle = 0.0

    def draw_shape(self, events, window, sett):
        if self.sel_shape != "Mouse" and self.sel_shape != "Polygon_Wall":
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
                            if self.end_pos is not None and self.start_pos is not None:
                                if abs(self.end_pos[1]-self.start_pos[1])>10 and abs(self.end_pos[0]-self.start_pos[0])>10:
                                    if self.sel_shape == "Circle":
                                        return Circle(self.start_pos, self.end_pos, self.sel_color, self.sel_shape, sett)
                                    elif self.sel_shape == "Rect_Wall":
                                        return Rect_Wall(self.start_pos, self.end_pos, self.angle, self.sel_color, self.sel_shape)
                                    elif self.sel_shape == "Triangle_Wall":
                                        return Triangle_Wall(self.start_pos, self.end_pos, self.angle, self.sel_color, self.sel_shape)
            if self.lm_pressed:
                if self.start_pos is not None:
                    if self.sel_shape == "Circle":
                        Circle(self.start_pos, pygame.mouse.get_pos(), self.sel_color, self.sel_shape, sett).draw(window)
                    elif self.sel_shape == "Rect_Wall":
                        Rect_Wall(self.start_pos, pygame.mouse.get_pos(), self.angle, self.sel_color, self.sel_shape).draw(window, sett)
                    elif self.sel_shape == "Triangle_Wall":
                        Triangle_Wall(self.start_pos, pygame.mouse.get_pos(), self.angle, self.sel_color, self.sel_shape).draw(window, sett)
        return None

    def draw_polygon(self, events, window, sett):
        if self.poly_drawing:
            m_pos = pygame.mouse.get_pos()
            if len(self.poly_pts) == 1:
                pygame.draw.line(window, self.sel_color, self.poly_pts[0], m_pos)
            elif len(self.poly_pts) > 1:
                draw_pts = self.poly_pts.copy()
                draw_pts.append(np.array([m_pos[0], m_pos[1]]))
                Polygon_Wall(draw_pts, self.angle, self.sel_color, self.sel_shape).draw(window, sett)
        if self.sel_shape == "Polygon_Wall":
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        m_pos = pygame.mouse.get_pos()
                        if m_pos[0] > sett.TB_WIDTH:
                            p = np.array([m_pos[0], m_pos[1]])
                            self.poly_pts.append(p)
                            if not self.poly_drawing:
                                self.poly_drawing = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.poly_drawing:
                            if len(self.poly_pts) > 2:
                                self.poly_drawing = False
                                return Polygon_Wall(self.poly_pts, self.angle, self.sel_color, self.sel_shape)
                    if event.key == pygame.K_ESCAPE:
                        self.poly_pts = []
                        self.poly_drawing = False
        else:
            self.poly_pts = []
            self.poly_drawing = False
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
        else:
            if self.holding:
                for w in walls:
                    self.lm_pressed = False
                    self.holding = False
                    for w in walls:
                        w.selected = False
                        w.update_pts()
        
                        
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

    def reset_values(self):
        self.angle = 0.0
        self.start_pos = None
        self.end_pos = None
    
    def change_shape(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if self.sel_shape != "Mouse":
                        self.reset_values()
                    self.sel_shape = "Mouse"
                if event.key == pygame.K_2:
                    if self.sel_shape != "Circle":
                        self.reset_values()
                    self.sel_shape = "Circle"
                if event.key == pygame.K_3:
                    if self.sel_shape != "Rect_Wall":
                        self.reset_values()
                    self.sel_shape = "Rect_Wall"
                if event.key == pygame.K_4:
                    if self.sel_shape != "Triangle_Wall":
                        self.reset_values()
                    self.sel_shape = "Triangle_Wall"
                if event.key == pygame.K_5:
                    if self.sel_shape != "Polygon_Wall":
                        self.reset_values()
                    self.sel_shape = "Polygon_Wall"

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
        poly = self.draw_polygon(events, window, sett)
        if poly is not None:
            walls.append(poly)
            self.poly_pts = []
            
