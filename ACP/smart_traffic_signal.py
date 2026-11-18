import pygame 
import random

pygame.init()


CAR_COLOR_CHANGE = pygame.USEREVENT +1
SGNAL_CHANGE_EVENT = pygame.USEREVENT  +2

ROAD = pygame.Color("dark grey")
WHITE = pygame.Color("white")
YELLOW = pygame.Color("yellow")
BLUE = pygame.Color("blue")
ORANGE = pygame.Color("orange")
GREEN = pygame.Color("green")
RED = pygame.color("red")

class Car(pygame.sprite.Sprite):
    def __init__(self, colour, width, height)




