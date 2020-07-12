import numpy as np
import pygame

pygame.init()

class Settings:
    def __init__(self):
        self.S_WIDTH = 800
        self.S_HEIGHT = 800

        self.TB_WIDTH = 150

        self.FLOOR_H = 100

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (0, 255, 255)
        self.BROWN = (139,69,19)

        self.G = 9.81
        self.DT = 0.2
        self.DENS = 1000.0

        self.FPS = 60

        #input_box_G
        self.font = pygame.font.Font(None, 32)
        self.input_box = pygame.Rect(10, 100, self.TB_WIDTH - 20, 32)
        self.active = False
        self.color_inactive = pygame.Color('blue')
        self.color_active = pygame.Color('green')
        self.color = self.color_inactive
        self.text = str(self.G)

        #color_buttons
        self.red_box = pygame.Rect(10, 10, 20, 20)
        self.green_box = pygame.Rect(30, 10, 20, 20)
        self.blue_box = pygame.Rect(50, 10, 20, 20)

        #shape_buttons

    def update(self, events, window, user):
        self.update_color_buttons(events, window, user)
        self.update_box_G(events, window)

    def update_color_buttons(self, events, window, user):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.red_box.collidepoint(event.pos):
                    user.sel_color = self.RED
                elif self.green_box.collidepoint(event.pos):
                    user.sel_color = self.GREEN
                elif self.blue_box.collidepoint(event.pos):
                    user.sel_color = self.BLUE
        pygame.draw.rect(window, self.RED, self.red_box)
        pygame.draw.rect(window, self.GREEN, self.green_box)
        pygame.draw.rect(window, self.BLUE, self.blue_box)
        
    def update_box_G(self, events, window):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_box.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False
                    self.text = str(self.G)
                self.color = self.color_active if self.active else self.color_inactive
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        self.active = False
                        if float(self.text) <= 99.9:
                            self.G = float(self.text)
                        else:
                            self.G = 99.9
                        self.text = str(self.G)
                        self.color = self.color_active if self.active else self.color_inactive
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif len(self.text) < 6:
                        if event.unicode in ["0","1","2","3","4","5","6","7","8","9"]:
                            self.text += event.unicode
                        elif event.unicode in [".", ","] and "." not in self.text:
                            self.text += "."
                        
        txt_surface = self.font.render(self.text, True, self.color)
        window.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
        pygame.draw.rect(window, self.color, self.input_box, 2)
