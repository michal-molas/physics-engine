import pygame
from settings import *
from User import User
from Floor import Floor

pygame.init()
window = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Physics Engine")

clock = pygame.time.Clock()

shapes = []
user = User()
floor = Floor()

def update(events):
    for s in shapes:
        s.update()

    user.update(events, window, shapes)

def draw_shapes():
    window.fill(WHITE)
    for s in shapes:
        s.draw(window)

def draw_other():
    pygame.draw.rect(window, BLACK, (0, 0, TB_WIDTH, S_HEIGHT))
    floor.draw(window)
    

is_running = True
while is_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
            
    draw_shapes()
    update(events)
    draw_other()
    
    pygame.display.update()

    clock.tick(60)
    
pygame.quit()