import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pet Food Game")
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (800, 600))
pet_img = pygame.transform.scale(
    pygame.image.load("pet.png"), (60, 60)
)
food_img = pygame.transform.scale(
    pygame.image.load("food.png"), (30, 30)
)
pet = pet_img.get_rect(center=(400, 300))
foods = pygame.sprite.Group()
for i in range(10):
    food = pygame.sprite.Sprite()
    food.image = food_img
    food.rect = food_img.get_rect(
        topleft=(random.randint(0, 770), random.randint(0, 570))
    )
    foods.add(food)
font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    pet.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    pet.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    pet.clamp_ip(screen.get_rect())
    pygame.sprite.spritecollide(
        type("Pet", (), {"rect": pet})(), foods, True
    )
    screen.blit(background, (0, 0))
    screen.blit(pet_img, pet)
    foods.draw(screen)
    if not foods:
        text = font.render("You collected all the food!", True, (255, 255, 0))
        screen.blit(text, text.get_rect(center=(400, 300)))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

