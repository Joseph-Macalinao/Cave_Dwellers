import pygame #import pygame
from pygame.locals import ( #import pygame.locals to use keys
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
import tkinter # use to get height and width of screen to make correct window size
info = tkinter.Tk()
width = info.winfo_screenwidth() 
height = info.winfo_screenheight()

pygame.init() #initialize pygame

screen = pygame.display.set_mode([width, height-60])

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

    screen.fill((0, 100, 0))
    pygame.display.flip()

pygame.quit()