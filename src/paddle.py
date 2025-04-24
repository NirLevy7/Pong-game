import pygame

class Paddle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def move(self, up=True):
        if up and self.rect.top > 0:
            self.rect.y -= self.speed  # Subtract speed to move up
        if not up and self.rect.bottom < 600:
            self.rect.y += self.speed  # Add speed to move down
