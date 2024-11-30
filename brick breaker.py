import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 850, 600
BALL_RADIUS = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
NUM_BRICKS_X = 10
NUM_BRICKS_Y = 5
FPS = 60
MAX_LIVES = 3  # Number of lives

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BRICK_COLOR = (0, 255, 0)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Brick Breaker')

# Set up fonts
font = pygame.font.SysFont('Comic Sans', 24)

class Paddle:
    def __init__(self):
        self.x = WIDTH // 2 - PADDLE_WIDTH // 2
        self.y = HEIGHT - PADDLE_HEIGHT - 10
        self.speed = 10

    def move(self, dx):
        self.x += dx
        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH - PADDLE_WIDTH:
            self.x = WIDTH - PADDLE_WIDTH

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y,
                         PADDLE_WIDTH, PADDLE_HEIGHT))

class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - PADDLE_HEIGHT - BALL_RADIUS - 20
        self.dx = random.choice([-4, 4])
        self.dy = -4

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), BALL_RADIUS)

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - PADDLE_HEIGHT - BALL_RADIUS - 20
        self.dx = random.choice([-4, 4])
        self.dy = -4

    def increase_speed(self):
        self.dx *= 1.1
        self.dy *= 1.1

class Brick:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

def generate_bricks(level):
    """Generate a new brick layout with the same color for all bricks."""
    bricks = []
    for y in range(NUM_BRICKS_Y):
        for x in range(NUM_BRICKS_X):
            bricks.append(Brick(x * (BRICK_WIDTH + 5) + 35,
                                y * (BRICK_HEIGHT + 5) + 35, BRICK_COLOR))
    return bricks

def main():
    paddle = Paddle()
    ball = Ball()
    level = 1  # Start at level 1
    bricks = generate_bricks(level)  # Generate initial brick layout
    clock = pygame.time.Clock()
    score = 0
    lives = MAX_LIVES  # Start with 3 lives
    running = True

    # Main game loop
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move paddle based on keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-paddle.speed)
        if keys[pygame.K_RIGHT]:
            paddle.move(paddle.speed)

        # Move ball
        ball.move()

        # Ball collision with walls
        if ball.x <= BALL_RADIUS or ball.x >= WIDTH - BALL_RADIUS:
            ball.dx *= -1
        if ball.y <= BALL_RADIUS:
            ball.dy *= -1

        # Ball collision with paddle
        if paddle.y <= ball.y + BALL_RADIUS <= paddle.y + PADDLE_HEIGHT and \
           paddle.x <= ball.x <= paddle.x + PADDLE_WIDTH:
            ball.dy *= -1
            score += 1

        # Ball falls below screen (missed the ball)
        if ball.y >= HEIGHT:
            lives -= 1
            if lives > 0:
                ball.reset()  # Reset ball position if player still has lives
            else:
                game_over_text = font.render(
                    "Game Over! Press 'R' to Restart", True, WHITE)
                screen.blit(game_over_text, (WIDTH // 2 - 140, HEIGHT // 2))
                pygame.display.flip()

                # Wait for restart or quit
                waiting_for_restart = True
                while waiting_for_restart:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            waiting_for_restart = False
                            running = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                main()  # Restart the game
                                waiting_for_restart = False
                                running = False

                break  # Exit the current game loop if game over

        # Check for brick collisions
        for brick in bricks[:]:
            if brick.rect.collidepoint(ball.x, ball.y):
                ball.dy *= -1
                bricks.remove(brick)
                score += 5

        # Draw game objects
        paddle.draw()
        ball.draw()
        for brick in bricks:
            brick.draw()

        # Draw score and lives
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 100, 10))

        if len(bricks) == 0:
            win_text = font.render(
                f"You Win! Press 'R' to Restart - Level {level}", True, WHITE)
            screen.blit(win_text, (WIDTH // 2 - 160, HEIGHT // 2))
            pygame.display.flip()
            # Wait for restart and move to the next level
            waiting_for_restart = True
            while waiting_for_restart:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting_for_restart = False
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            level += 1  # Increase level
                            ball.increase_speed()  # Increase ball speed
                            # Generate new brick layout
                            bricks = generate_bricks(level)
                            score = 0  # Reset score
                            lives = MAX_LIVES  # Reset lives
                            waiting_for_restart = False
                            running = False
            break  # Exit the current game loop if the player wins
        # Update screen
        pygame.display.flip()

    pygame.quit()
if __name__ == '__main__':
    main()
