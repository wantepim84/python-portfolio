import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
GRID_WIDTH = WIDTH // BLOCK_SIZE
GRID_HEIGHT = HEIGHT // BLOCK_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Optimized Shapes and Colors
SHAPES = [
    # S Shape
    [((0, 0), (0, 1), (1, 1), (1, 2)),
     ((0, 1), (1, 0), (1, 1), (2, 0))],

    # Z Shape
    [((0, 1), (0, 2), (1, 0), (1, 1)),
     ((0, 0), (1, 0), (1, 1), (2, 1))],

    # I Shape
    [((0, 1), (1, 1), (2, 1), (3, 1)),
     ((1, 0), (1, 1), (1, 2), (1, 3))],

    # O Shape (Square)
    [((0, 0), (0, 1), (1, 0), (1, 1))],

    # T Shape
    [((0, 1), (1, 0), (1, 1), (1, 2)),
     ((0, 1), (1, 1), (1, 2), (2, 1)),
     ((1, 0), (1, 1), (1, 2), (2, 1)),
     ((0, 1), (1, 0), (1, 1), (2, 1))],

    # L Shape
    [((0, 0), (1, 0), (1, 1), (1, 2)),
     ((0, 1), (1, 1), (2, 1), (2, 0)),
     ((1, 0), (1, 1), (1, 2), (2, 2)),
     ((0, 1), (0, 2), (1, 1), (2, 1))],

    # J Shape
    [((0, 2), (1, 0), (1, 1), (1, 2)),
     ((0, 0), (0, 1), (1, 1), (2, 1)),
     ((1, 0), (1, 1), (1, 2), (2, 0)),
     ((0, 1), (1, 1), (2, 1), (2, 2))]
]

SHAPE_COLORS = [CYAN, BLUE, ORANGE, YELLOW, GREEN, MAGENTA, RED]

class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = SHAPE_COLORS[SHAPES.index(shape)]
        self.rotation = 0

    def current_shape(self):
        return self.shape[self.rotation % len(self.shape)]

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for (x, y), color in locked_positions.items():
        grid[y][x] = color
    return grid

def convert_shape_format(piece):
    positions = []
    shape = piece.current_shape()
    for block in shape:
        x, y = block
        positions.append((piece.x + x, piece.y + y))
    return positions

def valid_space(piece, grid):
    accepted_positions = [[(j, i) for j in range(
        GRID_WIDTH) if grid[i][j] == BLACK] for i in range(GRID_HEIGHT)]
    accepted_positions = [j for sub in accepted_positions for j in sub]

    formatted = convert_shape_format(piece)
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def get_shape():
    return Piece(GRID_WIDTH // 2 - 2, 0, random.choice(SHAPES))

def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, True, color)
    surface.blit(label, (WIDTH / 2 - label.get_width() /
                 2, HEIGHT / 2 - label.get_height() / 2))

def draw_grid(surface, grid):
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            pygame.draw.rect(surface, grid[i][j],
                             (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

    for i in range(GRID_HEIGHT):
        pygame.draw.line(surface, WHITE, (0, i * BLOCK_SIZE),
                         (WIDTH, i * BLOCK_SIZE))
    for j in range(GRID_WIDTH):
        pygame.draw.line(surface, WHITE, (j * BLOCK_SIZE, 0),
                         (j * BLOCK_SIZE, HEIGHT))

def clear_rows(grid, locked):
    increment = 0
    for i in range(GRID_HEIGHT - 1, -1, -1):
        row = grid[i]
        if BLACK not in row:
            increment += 1
            ind = i
            for j in range(GRID_WIDTH):
                del locked[(j, i)]

    if increment > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                new_key = (x, y + increment)
                locked[new_key] = locked.pop(key)
    return increment

def draw_score(surface, score):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render(f'Score: {score}', True, WHITE)
    surface.blit(label, (10, 10))

def draw_restart_button(surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Restart', True, WHITE)
    button_rect = label.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    surface.blit(label, button_rect)
    return button_rect

def main():
    locked_positions = {}
    grid = create_grid()
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_speed = 0.27
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1

        shape_pos = convert_shape_format(current_piece)
        for pos in shape_pos:
            x, y = pos
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                locked_positions[(pos[0], pos[1])] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10

        draw_grid(screen, grid)
        draw_score(screen, score)

        if check_lost(locked_positions):
            draw_text_middle("Game Over", 40, WHITE, screen)
            restart_button = draw_restart_button(screen)
            pygame.display.update()

            # Wait for restart
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            main()
                clock.tick(15)
            break

        pygame.display.update()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tetris')
main()
