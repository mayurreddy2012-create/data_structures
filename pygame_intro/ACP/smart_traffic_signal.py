```python
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Smart Traffic Signal")

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
BOUNDARY = pygame.USEREVENT + 1

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(50, 250))
        self.speed = 4
        self.direction = 1

    def update(self):
        self.rect.x += self.speed * self.direction

        if self.rect.right >= 750 and self.direction == 1:
            self.rect.right = 750
            pygame.event.post(pygame.event.Event(BOUNDARY))

        elif self.rect.left <= 50 and self.direction == -1:
            self.rect.left = 50
            pygame.event.post(pygame.event.Event(BOUNDARY))

car = Car()
sprites = pygame.sprite.Group(car)
signal = GREEN

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == BOUNDARY:
            car.direction *= -1
            signal = RED if signal == GREEN else GREEN
            car.image.fill(signal)

    sprites.update()
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, (50, 230, 700, 70))
    sprites.draw(screen)
    pygame.draw.rect(screen, BLACK, (350, 50, 100, 150))
    pygame.draw.circle(screen, signal, (400, 125), 30)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```
