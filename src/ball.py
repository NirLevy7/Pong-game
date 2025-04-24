import pygame
import random
import time


class Ball:
    def __init__(self, x, y, radius, speed=3):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.speed = speed
        self.speed_x = speed * random.choice((1, -1))
        self.speed_y = speed * random.choice((1, -1))

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                           self.rect.center, self.rect.width // 2)

    def move(self):
        if not self.moving:
            if time.time() >= self.reset_time:
                self.moving = True
            else:
                return  # Ball is paused, do nothing
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1

    def reset(self, x, y):
        self.rect.center = (x, y)
        self.speed_x = self.speed * random.choice((1, -1))
        self.speed_y = self.speed * random.choice((1, -1))
        self.moving = False
        self.reset_time = time.time() + 3  # 3 seconds delay
