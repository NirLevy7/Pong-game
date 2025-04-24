import pygame
import random

class Ball:
    def __init__(self, x, y, radius):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.speed_x = 5 * random.choice((1, -1))
        self.speed_y = 5 * random.choice((1, -1))

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.rect.center, self.rect.width // 2)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1
