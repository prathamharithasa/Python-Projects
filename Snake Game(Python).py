import pygame
import random

# Initialize
pygame.init()

# Screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('🐍 Snake Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red   = (200, 0, 0)
green = (0, 200, 0)
light_blue = (173, 216, 230)
gray = (120, 120, 120)

# Game settings
clock = pygame.time.Clock()
snake_block = 20

# Fonts
font = pygame.font.SysFont('consolas', 24)
big_font = pygame.font.SysFont('consolas', 36, bold=True)

# Score display
def draw_score(score):
    value = font.render(f"Score: {score}", True, black)
    screen.blit(value, [width - 150, 10])

# Persist high score
def load_high_score(path='highscore.txt'):
    try:
        with open(path, 'r') as f:
            return int(f.read().strip())
    except Exception:
        return 0

def save_high_score(score, path='highscore.txt'):
    try:
        hs = load_high_score(path)
        if score > hs:
            with open(path, 'w') as f:
                f.write(str(score))
    except Exception:
        pass

# Snake
def draw_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        if i == len(snake_list) - 1:
            pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block], border_radius=6)
        else:
            pygame.draw.rect(screen, gray, [x[0], x[1], snake_block, snake_block], border_radius=4)

# Message box
def show_message(msg, size=24, color=black, y_offset=0):
    text = pygame.font.SysFont('consolas', size, bold=True).render(msg, True, color)
    rect = text.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(text, rect)

# Start screen (press SPACE to open difficulty selector)
def start_screen():
    screen.fill(light_blue)
    show_message("Welcome to Snake Game", 45, black, -40)
    show_message("Press SPACE to Start", 30, black, 10)
    show_message("Controls: Arrow Keys or W A S D", 20, gray, 50)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Show difficulty options after SPACE
                    screen.fill(light_blue)
                    show_message("Select Difficulty", 40, black, -60)
                    show_message("1 - Easy (Slow)    2 - Medium (Normal)    3 - Hard (Fast)", 18, gray, 0)
                    pygame.display.update()

                    while True:
                        for ev in pygame.event.get():
                            if ev.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if ev.type == pygame.KEYDOWN:
                                # Easy
                                if ev.key in (pygame.K_1, pygame.K_e):
                                    return 8   # slow
                                # Medium (default)
                                if ev.key in (pygame.K_2, pygame.K_m, pygame.K_SPACE):
                                    return 15  # normal
                                # Hard
                                if ev.key in (pygame.K_3, pygame.K_h):
                                    return 25  # fast

# Main Game Loop (accept speed)
def game_loop(snake_speed):
    while True:  # Outer loop for restarting the game
        game_over = False
        game_close = False

        # Start positions snapped to grid
        x = round((width // 2) / snake_block) * snake_block
        y = round((height // 2) / snake_block) * snake_block
        dx = 0
        dy = 0

        snake = []
        snake_len = 1

        food_x = random.randrange(0, width - snake_block, snake_block)
        food_y = random.randrange(0, height - snake_block, snake_block)

        while not game_over:
            while game_close:
                screen.fill(light_blue)
                final_score = snake_len - 1
                save_high_score(final_score)
                high_score = load_high_score()

                show_message("Game Over!", 36, red, -70)
                show_message(f"Final Score: {final_score}", 28, black, -20)
                show_message(f"High Score: {high_score}", 24, gray, 20)
                show_message("Press C to Play Again or Q to Quit", 24, black, 60)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                        elif event.key == pygame.K_c:
                            game_close = False
                            game_over = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    # Allow Arrow keys or WASD and prevent reversing direction on the same axis
                    if event.key in (pygame.K_LEFT, pygame.K_a) and dx == 0:
                        dx = -snake_block
                        dy = 0
                    elif event.key in (pygame.K_RIGHT, pygame.K_d) and dx == 0:
                        dx = snake_block
                        dy = 0
                    elif event.key in (pygame.K_UP, pygame.K_w) and dy == 0:
                        dy = -snake_block
                        dx = 0
                    elif event.key in (pygame.K_DOWN, pygame.K_s) and dy == 0:
                        dy = snake_block
                        dx = 0

            # Move
            x += dx
            y += dy

            # Boundary collision
            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            screen.fill(white)

            # Draw food
            pygame.draw.rect(screen, green, [food_x, food_y, snake_block, snake_block], border_radius=5)

            # Snake mechanics
            head = [x, y]
            snake.append(head)
            if len(snake) > snake_len:
                del snake[0]

            # Self collision
            for segment in snake[:-1]:
                if segment == head:
                    game_close = True

            draw_snake(snake_block, snake)
            draw_score(snake_len - 1)

            pygame.display.update()

            # Eating food
            if x == food_x and y == food_y:
                # re-roll until food not on snake
                while True:
                    new_x = random.randrange(0, width - snake_block, snake_block)
                    new_y = random.randrange(0, height - snake_block, snake_block)
                    if [new_x, new_y] not in snake:
                        food_x, food_y = new_x, new_y
                        break
                snake_len += 1

            clock.tick(snake_speed)

# Run the game
selected_speed = start_screen()
game_loop(selected_speed)
