import pygame
from settings import *
from User import User
from Floor import Floor
import Collisions as col

pygame.init()

sett = Settings()

window = pygame.display.set_mode((sett.S_WIDTH, sett.S_HEIGHT))
pygame.display.set_caption("Physics Engine")

clock = pygame.time.Clock()

shapes = []
user = User(sett)
floor = Floor()

def update(events):
    for s in shapes:
        s.update(shapes, sett)

    user.update(events, window, shapes, sett)
    col.perform_collisions(shapes, sett)

def draw_shapes():
    window.fill(sett.WHITE)
    for s in shapes:
        s.draw(window)

def draw_other(events):
    pygame.draw.rect(window, sett.BLACK, (0, 0, sett.TB_WIDTH, sett.S_HEIGHT))
    floor.draw(window, sett)
    sett.update_box(events, window)
    

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
