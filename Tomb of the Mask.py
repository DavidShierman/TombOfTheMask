import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tomb of the Mask")

# Define the grid parameters
num_columns = 30
num_rows = 30
cell_width = screen_width // num_columns
cell_height = screen_height // num_rows

# Restart Score
score = 0

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (235, 0, 0)
BLUE = (0, 0, 225)
GREEN = (0, 255, 0)

# Grid
grid_layout = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXOOXXXXLXLLLLLLLXMOXOOOOOOX",
    "MLLLOOLLLLLLLXXXXXLXLOOOOOOLLX",
    "XLXXXXXXXXLLLXLLLXLXLOOOOOOXLX",
    "XLLLXLLLLXLLXXLXLXLXLOOOXXXXLX",
    "XXXLOOLXXXXLXXLXLLLXLOOOXLLLLX",
    "XMOLOOLXLXLLLXLXXXXXLOOOXLLXXX",
    "XOOLOLLXLLLXLXLLLLLLLXOLXXLXLX",
    "XOOLOLLXXLLLLXXLXXXXOOOXLLLLLX",
    "XOXLOLLXMOOOXXXLXLLXXXMLLLXXLX",
    "XOXLOLLXOOOOXXXLXLLLLXXLXLXXLX",
    "XOXLOLLXLOLLXXXLXLXOLMXLLLXXLX",
    "XOXLOLLXLXOLXXXLXLMOOOXLOMXXLX",
    "XLLLOLLXLOOLXXXLXXOOOOXLLLLLLX",
    "XLMLOXLXLOOXXXXLMLOLOOXOOXXXXX",
    "XLXLOXLLLLLLLLXLXLOOOXXXLXLLLX",
    "XLXLLLLLOOOMXLXLMLOOOLOOOOLOLX",
    "XLXOXXXXXOOMXLXLXLOOXLXOOOLMLX",
    "XLMOLLLLLLLLLLXLXLOOXLXOOOLOXX",
    "XLXXOOOOOOOXLXXLXLOOOLOOOOLOLX",
    "XLLOOOOOOXOXLXXLXLOOXLXXOOLOOX",
    "XLLXXMOOOLOOOOOLXLLLXLXMOOLOOX",
    "XXLXXXXOOOOOOOOMXXLLXLXOOXLOOX",
    "XLLLLLLLLOMOOOOXXMMXXLXLLLLLLX",
    "XLXOOOOOXLOOOOOLLLLLLLLLLXXOLX",
    "XLLLXOOOOOOXOXOLXLLLLLLLLXXOLX",
    "XXMLOOOOOOOXLLLLLLLXXLXXXXXXLX",
    "XLLLLXOOOOXXOOOLXXLOXLLLLLLXLX",
    "XLLXLLLLLLLLLLLLXMLLLLLLLXLLLM",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Parse grid
walls = [(x, y) for y, row in enumerate(grid_layout) for x, cell in enumerate(row) if cell == 'X']
collectibles = [(x, y) for y, row in enumerate(grid_layout) for x, cell in enumerate(row) if cell == 'L']
lavas = [(x, y) for y, row in enumerate(grid_layout) for x, cell in enumerate(row) if cell == 'M']

# Find number of starting points
starting_points = sum(row.count("L") for row in grid_layout)
print(starting_points)

# Define player starting position (ensure it's a clear spot)
player_x = 4
player_y = 1

direction = None

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle key presses for moving the player, but only if not already moving
        elif event.type == pygame.KEYDOWN and direction is None:
            if event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"
            elif event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"

    # Move player in the direction
    if direction:
        new_x, new_y = player_x, player_y
        if direction == "LEFT":
            new_x -= 1
        elif direction == "RIGHT":
            new_x += 1
        elif direction == "UP":
            new_y -= 1
        elif direction == "DOWN":
            new_y += 1

        # Check for collisions
        if (new_x, new_y) not in walls and 0 <= new_x < num_columns and 0 <= new_y < num_rows:
            player_x, player_y = new_x, new_y
        else:
            direction = None  # Stop moving if on a wall

    # Check for collectible collisions
    if (player_x, player_y) in collectibles:
        collectibles.remove((player_x, player_y))
        score += 1

    if (player_x, player_y) in lavas:
        print ("You have perrished :(")
        print ("Your score is: " + str(score))
        # Quit Pygame
        pygame.quit()
        sys.exit()

    if score == starting_points:
        if direction == None:
            print ("You win!")
            pygame.quit()
            sys.exit()

    # Clear screen
    screen.fill(BLACK)
    
    # Draw grid
    for x in range(0, screen_width, cell_width):
        pygame.draw.line(screen, WHITE, (x, 0), (x, screen_height))
    for y in range(0, screen_height, cell_height):
        pygame.draw.line(screen, WHITE, (0, y), (screen_width, y))

    # Draw walls
    for wall in walls:
        pygame.draw.rect(screen, BLUE, (wall[0] * cell_width, wall[1] * cell_height, cell_width, cell_height))

    # Draw collectibles
    for collectible in collectibles:
        pygame.draw.rect(screen, GREEN, (collectible[0] * cell_width +5, collectible[1] * cell_height +5, cell_width /2, cell_height /2))

    for lava in lavas:
        pygame.draw.rect(screen, RED, (lava[0] * cell_width, lava[1] * cell_height, cell_width, cell_height))

    # Draw player
    pygame.draw.rect(screen, YELLOW, (player_x * cell_width, player_y * cell_height, cell_width, cell_height))
    pygame.draw.rect(screen, BLACK, (player_x * cell_width + 2, player_y * cell_height + 2, cell_width /4, cell_height /4))
    pygame.draw.rect(screen, BLACK, (player_x * cell_width + 14, player_y * cell_height + 2, cell_width /4, cell_height /4))

    # Update
    pygame.display.flip()
    clock.tick(18)  # frame delay    



# Quit Pygame
pygame.quit()
sys.exit()
