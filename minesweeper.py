import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
WHITE, BLACK, GRAY, DARK_GRAY, RED, BLUE, GREEN = (255, 255, 255), (0, 0, 0), (
    192, 192, 192), (169, 169, 169), (255, 0, 0), (0, 0, 255), (0, 255, 0)

CELL_FONT = pygame.font.SysFont('comicsans', WIDTH // 20)
BUTTON_FONT = pygame.font.SysFont('comicsans', 30)

class Minesweeper:
    def __init__(self, grid_size, num_mines):
        self.grid_size, self.num_mines = grid_size, num_mines
        self.cell_size = WIDTH // grid_size
        self.grid = [['' for _ in range(grid_size)] for _ in range(grid_size)]
        self.visible = [[False] * grid_size for _ in range(grid_size)]
        self.flags = [[False] * grid_size for _ in range(grid_size)]
        self.mines = self.generate_mines()
        self.calculate_numbers()
        self.game_over = self.win = False

    def generate_mines(self):
        mines = set()
        while len(mines) < self.num_mines:
            mines.add((random.randint(0, self.grid_size - 1),
                      random.randint(0, self.grid_size - 1)))
        for x, y in mines:
            self.grid[y][x] = 'M'
        return mines

    def calculate_numbers(self):
        for x, y in self.mines:
            for nx, ny in self.get_neighbors(x, y):
                if self.grid[ny][nx] != 'M':
                    self.grid[ny][nx] = self.grid[ny][nx] + \
                        1 if isinstance(self.grid[ny][nx], int) else 1

    def get_neighbors(self, x, y):
        return [(x + dx, y + dy) for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                if 0 <= x + dx < self.grid_size and 0 <= y + dy < self.grid_size]

    def reveal(self, x, y):
        if self.visible[y][x] or self.flags[y][x] or self.game_over:
            return
        self.visible[y][x] = True
        if self.grid[y][x] == 'M':
            self.game_over = True
        elif self.grid[y][x] == '':
            for nx, ny in self.get_neighbors(x, y):
                self.reveal(nx, ny)
        self.check_win()

    def toggle_flag(self, x, y):
        if not self.visible[y][x]:
            self.flags[y][x] = not self.flags[y][x]

    def check_win(self):
        if all(self.visible[y][x] or (x, y) in self.mines for y in range(self.grid_size) for x in range(self.grid_size)):
            self.win, self.game_over = True, True

    def draw(self, screen):
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                rect = pygame.Rect(x * self.cell_size, y *
                                   self.cell_size, self.cell_size, self.cell_size)
                if self.visible[y][x]:
                    pygame.draw.rect(screen, WHITE, rect)
                    if self.grid[y][x] == 'M':
                        pygame.draw.circle(
                            screen, RED, rect.center, self.cell_size // 4)
                    elif isinstance(self.grid[y][x], int):
                        self.draw_text(screen, str(
                            self.grid[y][x]), rect.center, BLUE)
                else:
                    pygame.draw.rect(
                        screen, DARK_GRAY if self.flags[y][x] else GRAY, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)
        if self.game_over:
            self.show_message(screen, "You Win!" if self.win else "Game Over!")

    def draw_text(self, screen, text, center, color):
        label = CELL_FONT.render(text, True, color)
        screen.blit(label, label.get_rect(center=center))

    def show_message(self, screen, text):
        label = BUTTON_FONT.render(text, True, GREEN if self.win else RED)
        screen.blit(label, label.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 40)))
        reset_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 20, 200, 50)
        pygame.draw.rect(screen, DARK_GRAY, reset_button)
        pygame.draw.rect(screen, BLACK, reset_button, 2)
        self.draw_text(screen, "Restart", reset_button.center, WHITE)
        return reset_button

def difficulty_screen(screen):
    screen.fill(BLACK)
    options = [('Easy', 10, 10), ('Medium', 15, 30), ('Hard', 20, 50)]
    buttons = []
    for i, (label, _, _) in enumerate(options):
        button = pygame.Rect(WIDTH // 2 - 100, 150 + i * 100, 200, 50)
        pygame.draw.rect(screen, GRAY, button)
        pygame.draw.rect(screen, BLACK, button, 2)
        text = BUTTON_FONT.render(label, True, BLACK)
        screen.blit(text, text.get_rect(center=button.center))
        buttons.append((button, label))
    pygame.display.flip()
    return buttons, options

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Minesweeper')
    clock = pygame.time.Clock()

    difficulty = None
    while difficulty is None:
        buttons, options = difficulty_screen(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button, label in buttons:
                    if button.collidepoint(event.pos):
                        difficulty = next(
                            filter(lambda opt: opt[0] == label, options))[1:]

    game = Minesweeper(*difficulty)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.game_over:
                    reset_button = game.show_message(screen, "")
                    if reset_button.collidepoint(event.pos):
                        main()
                else:
                    x, y = pygame.mouse.get_pos()
                    x, y = x // game.cell_size, y // game.cell_size
                    if event.button == 1:
                        game.reveal(x, y)
                    elif event.button == 3:
                        game.toggle_flag(x, y)

        screen.fill(BLACK)
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
