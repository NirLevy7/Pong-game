import random
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


def reset_ball(ball):
    ball.reset(WIDTH // 2, HEIGHT // 2)


def main():
    font = pygame.font.Font(None, 60)
    score1 = 0
    score2 = 0
    game_over = False
    paddle1 = Paddle(50, HEIGHT // 2 - 50, 10, 100)
    paddle2 = Paddle(WIDTH - 60, HEIGHT // 2 - 50, 10, 100)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 10, speed=3)
    reset_ball(ball)

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

        # Restart if game is over
        if game_over and keys[pygame.K_r]:
            score1 = 0
            score2 = 0
            reset_ball(ball)
            game_over = False

        # Game logic only if not over
        if not game_over:
            ball.move()
            if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
                ball.speed_x *= -1

            if ball.rect.left <= 0:
                score2 += 1
                if score2 == 5:
                    game_over = True
                else:
                    reset_ball(ball)

            if ball.rect.right >= WIDTH:
                score1 += 1
                if score1 == 5:
                    game_over = True
                else:
                    reset_ball(ball)

        # Draw
        SCREEN.fill(BLACK)
        paddle1.draw(SCREEN)
        paddle2.draw(SCREEN)
        ball.draw(SCREEN)

        # Draw score
        score_text = font.render(f"{score1}   {score2}", True, WHITE)
        SCREEN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

        # Game Over message
        if game_over:
            winner = "Player 1 Wins :)" if score1 == 5 else "Player 2 Wins :)"
            win_text = font.render(winner, True, WHITE)
            SCREEN.blit(
                win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - 30))

            restart_text = pygame.font.Font(None, 40).render(
                "Press R to restart", True, WHITE)
            SCREEN.blit(restart_text, (WIDTH // 2 -
                        restart_text.get_width() // 2, HEIGHT // 2 + 30))

        pygame.display.flip()
        CLOCK.tick(60)


if __name__ == "__main__":
    main()
