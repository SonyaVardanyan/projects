#!/usr/bin/python3
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 200
GROUND_HEIGHT = 20
GRAVITY = 1
SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chrome Dino Game")

# Load the images
dino = pygame.image.load('images/dino.png')
# dino = pygame.transform.rotate(dino,220)
cactus = pygame.image.load('images/cactus.png')
cloud = pygame.image.load('images/cloud.png')
background = pygame.image.load('images/background.jpg')

# Scale the images
dino = pygame.transform.scale(dino, (40, 40))
cactus = pygame.transform.scale(cactus, (20, 30))
cloud = pygame.transform.scale(cloud, (40, 20))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Create Dino   
dino_x, dino_y = 50, HEIGHT - GROUND_HEIGHT - 120
dino_vel = 0
dino_jump = 10
jumping = False

# Create Cactus
cactus_x = WIDTH
cactus_y = HEIGHT - GROUND_HEIGHT - 50

# Create Cloud
cloud_x = WIDTH
cloud_y = random.randint(20, 80)

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_text(surf, text, x, y):
    text_surface = font.render(text, True, WHITE)
    surf.blit(text_surface, (x, y))

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not jumping:
            dino_vel = -dino_jump
            jumping = True

    # Update Dino
    dino_y += dino_vel
    dino_vel += GRAVITY

    if dino_y >= HEIGHT - GROUND_HEIGHT - 60:
        dino_y = HEIGHT - GROUND_HEIGHT - 60
        jumping = False

    # Update Cactus
    cactus_x -= SPEED
    if cactus_x < -20:
        cactus_x = WIDTH
        score += 1

    # Update Cloud
    cloud_x -= 1
    if cloud_x < -40:
        cloud_x = WIDTH
        cloud_y = random.randint(20, 80)

    # Draw everything
    screen.blit(background, (0, 0))
    screen.blit(dino, (dino_x, dino_y))
    screen.blit(cactus, (cactus_x, cactus_y))
    screen.blit(cloud, (cloud_x, cloud_y))
    draw_text(screen, f"Score: {score}", 10, 10)

    pygame.display.update()

    # Check for collision
    if dino_x + 40 > cactus_x and dino_x < cactus_x + 20:
        if dino_y + 40 > cactus_y:
            running = False

    clock.tick(30)

pygame.quit()