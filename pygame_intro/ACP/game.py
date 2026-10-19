
import pygame
import random

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Player and Enemies")
player = pygame.Rect(375, 275, 50, 50)


enemies = []
for i in range(7):
    x = random.randint(0, 750)
    y = random.randint(0, 550)
    enemy = pygame.Rect(x, y, 50, 50)
    enemies.append(enemy)

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    for enemy in enemies[:]:
        if player.colliderect(enemy):
            score += 1
            enemies.remove(enemy)

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), player)

    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.update()
pygame.quit()

