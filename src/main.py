import pygame
from settings import *
from User import User
from Floor import Floor
import Collisions as col

#TODO 1: Ulepszyć system klikania tak, żeby nie było idiotycznych left/right tylko np in/out
#TODO 2: Ustalić kierunek boków w wielokącie tak żeby było jak w prostokącie np
#TODO 3: Ogólnie trzeba ten kod zrobić czytelny bo nie jest w chuj

pygame.init()

sett = Settings()

window = pygame.display.set_mode((sett.S_WIDTH, sett.S_HEIGHT))
pygame.display.set_caption("Physics Engine")

clock = pygame.time.Clock()

shapes = []
walls = []
user = User(sett)
floor = Floor()

def update(events):
    for s in shapes:
        s.update(events, shapes, sett)

    for w in walls:
        #w.update()
        pass
            
    user.update(events, window, shapes, walls, sett)
    col.perform_collisions(shapes, walls, sett)

def draw_shapes():
    window.fill(sett.WHITE)
    for s in shapes:
        s.draw(window)

    for w in walls:
        w.draw(window, sett)

def draw_other(events):
    pygame.draw.rect(window, sett.BLACK, (0, 0, sett.TB_WIDTH, sett.S_HEIGHT))
    floor.draw(window, sett)
    sett.update(events, window, user) 

is_running = True
while is_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
            
    draw_shapes()
    update(events)
    draw_other(events)
    
    pygame.display.update()

    clock.tick(sett.FPS)
    
pygame.quit()
