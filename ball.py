import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 770)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(3, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > 600:
            self.rect.x = random.randint(0, 770)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.randint(3, 8)
