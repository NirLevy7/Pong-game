import pygame
import sys
from paddle import Paddle
from ball import Ball

pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
CLOCK = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    paddle1 = Paddle(50, HEIGHT // 2 - 50, 10, 100)
    paddle2 = Paddle(WIDTH - 60, HEIGHT // 2 - 50, 10, 100)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move(up=True)
        if keys[pygame.K_s]:
            paddle1.move(up=False)
        if keys[pygame.K_UP]:
            paddle2.move(up=True)
        if keys[pygame.K_DOWN]:
            paddle2.move(up=False)

        # Ball movement and collision
        ball.move()
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.speed_x *= -1
        if ball.rect.left <= 0 or ball.rect.right >= WIDTH:
            ball.rect.center = (WIDTH // 2, HEIGHT // 2)
            ball.speed_x *= random.choice((1, -1))
            ball.speed_y *= random.choice((1, -1))

        # Draw
        SCREEN.fill(BLACK)
        paddle1.draw(SCREEN)
        paddle2.draw(SCREEN)
        ball.draw(SCREEN)
        pygame.display.flip()
        CLOCK.tick(60)

if __name__ == "__main__":
    main()
