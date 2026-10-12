import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
bg = pygame.transform.scale(pygame.image.load("forest.jpg"), (800, 600))
animal = pygame.transform.scale(pygame.image.load("tiger.png"), (300, 300))
font = pygame.font.SysFont(None, 40)
heading = font.render("Wildlife Information", True, (255, 255, 255))
fact = font.render("Tigers have unique stripes!", True, (255, 255, 255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg, (0, 0))
    screen.blit(heading, (200, 30))
    screen.blit(animal, (250, 120))
    screen.blit(fact, (180, 480))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

