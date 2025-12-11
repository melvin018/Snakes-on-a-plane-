# ...existing code...
#!/usr/bin/env python3
import sys
import random
import pygame

# Simple Snake game using pygame
# Save as a .py file and run: python filename.py

# Configuration
CELL_SIZE = 20
GRID_W, GRID_H = 30, 20
SCREEN_W, SCREEN_H = CELL_SIZE * GRID_W, CELL_SIZE * GRID_H
FPS_START = 8
FPS_MAX = 25
FPS_INCREASE_EAT = 0.5

# Colors
BG = (18, 18, 18)
GRID = (30, 30, 30)
SNAKE_HEAD = (0, 200, 0)
SNAKE_BODY = (0, 150, 0)
FOOD = (200, 50, 50)
TEXT = (220, 220, 220)


def rnd_cell(exclude=None):
    exclude = exclude or set()
    while True:
        p = (random.randrange(GRID_W), random.randrange(GRID_H))
        if p not in exclude:
            return p


def draw_grid(surf):
    for x in range(0, SCREEN_W, CELL_SIZE):
        pygame.draw.line(surf, GRID, (x, 0), (x, SCREEN_H))
    for y in range(0, SCREEN_H, CELL_SIZE):
        pygame.draw.line(surf, GRID, (0, y), (SCREEN_W, y))


def draw_rect(surf, pos, color):
    r = pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surf, color, r)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    def new_game():
        mid = (GRID_W // 2, GRID_H // 2)
        snake = [mid, (mid[0] - 1, mid[1]), (mid[0] - 2, mid[1])]
        direction = (1, 0)  # moving right
        pending_dir = direction
        food = rnd_cell(set(snake))
        score = 0
        fps = FPS_START
        return snake, direction, pending_dir, food, score, fps

    snake, direction, pending_dir, food, score, fps = new_game()
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False

                if not game_over:
                    if event.key in (pygame.K_LEFT, pygame.K_a):
                        pending_dir = (-1, 0)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        pending_dir = (1, 0)
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        pending_dir = (0, -1)
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        pending_dir = (0, 1)
                else:
                    if event.key == pygame.K_r:
                        snake, direction, pending_dir, food, score, fps = new_game()
                        game_over = False

        if not game_over:
            # Prevent reversing directly
            if pending_dir != (-direction[0], -direction[1]):
                direction = pending_dir

            head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            # Wall collision
            if not (0 <= head[0] < GRID_W and 0 <= head[1] < GRID_H):
                game_over = True
            # Self collision
            elif head in snake:
                game_over = True
            else:
                snake.insert(0, head)
                if head == food:
                    score += 1
                    fps = min(FPS_MAX, fps + FPS_INCREASE_EAT)
                    food = rnd_cell(set(snake))
                else:
                    snake.pop()

        # Draw
        screen.fill(BG)
        draw_grid(screen)
        draw_rect(screen, food, FOOD)
        if snake:
            draw_rect(screen, snake[0], SNAKE_HEAD)
            for seg in snake[1:]:
                draw_rect(screen, seg, SNAKE_BODY)

        score_surf = font.render(f"Score: {score}", True, TEXT)
        screen.blit(score_surf, (8, 8))

        if game_over:
            over_surf = font.render("Game Over - Press R to restart or Q/Esc to quit", True, TEXT)
            rect = over_surf.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2))
            screen.blit(over_surf, rect)

        pygame.display.flip()
        clock.tick(max(1, int(fps)))

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()