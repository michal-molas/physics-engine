import pygame

class Floor:
    def __init__(self):
        pass

    def draw(self, window, sett):
        pygame.draw.rect(window, sett.BROWN, (sett.TB_WIDTH, sett.S_HEIGHT - sett.FLOOR_H, sett.S_WIDTH - sett.TB_WIDTH, sett.FLOOR_H))
