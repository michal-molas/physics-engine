import pygame
from settings import *

class Floor:
    def __init__(self):
        pass

    def draw(self, window):
        pygame.draw.rect(window, BROWN, (TB_WIDTH, S_HEIGHT - FLOOR_H, S_WIDTH - TB_WIDTH, FLOOR_H))
