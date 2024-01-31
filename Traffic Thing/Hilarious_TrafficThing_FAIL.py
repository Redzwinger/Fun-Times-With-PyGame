import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CAR_WIDTH, CAR_HEIGHT = 30, 15
CAR_SPEED = 3

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction

    def update(self):
        if self.direction == "up":
            self.rect.y -= CAR_SPEED
            if self.rect.bottom < road_horizontal.top:
                self.rect.top = road_horizontal.bottom
        elif self.direction == "down":
            self.rect.y += CAR_SPEED
            if self.rect.top > road_horizontal.bottom:
                self.rect.bottom = road_horizontal.top
        elif self.direction == "left":
            self.rect.x -= CAR_SPEED
            if self.rect.right < road_vertical.left:
                self.rect.left = road_vertical.right
        elif self.direction == "right":
            self.rect.x += CAR_SPEED
            if self.rect.left > road_vertical.right:
                self.rect.right = road_vertical.left

        if self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.top > HEIGHT:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossroad Simulation")

all_sprites = pygame.sprite.Group()

road_horizontal = pygame.Rect(0, HEIGHT // 2, WIDTH, 100)
road_vertical = pygame.Rect(WIDTH // 2, 0, 100, HEIGHT)

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if random.random() < 0.02:
        direction = random.choice(["up", "down", "left", "right"])
        if direction == "up":
            car = Car(random.randint(road_horizontal.left, road_horizontal.right - CAR_WIDTH), road_horizontal.top, direction)
        elif direction == "down":
            car = Car(random.randint(road_horizontal.left, road_horizontal.right - CAR_WIDTH), road_horizontal.bottom - CAR_HEIGHT, direction)
        elif direction == "left":
            car = Car(road_vertical.left, random.randint(road_vertical.top, road_vertical.bottom - CAR_HEIGHT), direction)
        elif direction == "right":
            car = Car(road_vertical.right - CAR_WIDTH, random.randint(road_vertical.top, road_vertical.bottom - CAR_HEIGHT), direction)
        all_sprites.add(car)

    all_sprites.update()

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, road_horizontal)
    pygame.draw.rect(screen, WHITE, road_vertical)
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

# Confoundedly Crafted By Redzwinger #