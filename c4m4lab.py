# Import Stats and call mean, median, and mode

# import stats module
from c4m4stats import Stats

# Instantiate the variable with no parameters
my_stats = Stats()

# Instantiate the integer values
data = [8, 7, 3, 9, 1, 4, 3]

# Call statistical methods
print(my_stats.mean(data))   # (8+7+3+9+1+4+3) / 7 = 35 / 7 = 5 
print(my_stats.median(data)) # 4
print(my_stats.mode(data))   # 3

# Call additional statistical methods
print(my_stats.minimum(data)) # 1
print(my_stats.maximum(data)) # 9
print(my_stats.data_range(data)) # 8
print(my_stats.count(data)) # 7
print(my_stats.variance(data)) # sum of each values' squared differences from the mean / number of values = 7.71
print(my_stats.std_dev(data)) # 7.71 ** 0.5 = 2.78

# Instantiate values of two variables 
x=[1,2,3,4,5]
y=[2,4,5,4,5]

# Call linear_regression, r_squared, and predict methods
print(my_stats.linear_regression(x, y)) # linear_regression: y = 0.6x + 2.2
print(my_stats.r_squared(x, y)) # r_squared: 0.6
print(my_stats.predict(x, y, 6)) # predict(6): 5.8

# Flappy_Bird Game
"""
c4m4lab.py

Runner / entry point for the Flappy Bird lab.     
Demonstrates the full game loop using Game from c4m4game.py:
- window setup
- loading/resizing images
- background, ground, bird, pipes, collision, score, restart
"""

import sys
import pygame
from c4m4game import Game
from pathlib import Path

# -------------------------
# Runner (entry point)
# -------------------------
def main() -> None:
    """Run the Flappy Bird game loop."""
    pygame.init()
    screen = pygame.display.set_mode((400, 720))
    clock = pygame.time.Clock()

    base = Path(".")                        # <-- path confirmed correct
    bird_img = str(base / "flappy_bird" / "bird.png")
    pipe_img = str(base / "flappy_bird" / "pipe.png")
    background_img = str(base / "flappy_bird" / "background.png")
    ground_img = str(base / "flappy_bird" / "ground.png")

    game = Game(bird_img, pipe_img, background_img, ground_img)
    game.resize_images()

    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game.active:
                    game.flap()
                if event.key == pygame.K_SPACE and not game.active:
                    game.restart()
            if event.type == SPAWNPIPE:
                game.add_pipe()

        game.show_background(screen)

        if game.active:
            game.show_bird(screen)
            game.update_bird()
            game.move_pipes()
            game.show_pipes(screen)
            game.check_collision()
            game.update_score()
            game.show_score("playing", screen, (255, 255, 255))
        else:
            game.game_over(screen, (255, 255, 255))

        game.show_ground(screen)
        game.move_ground()

        pygame.display.update()
        clock.tick(120)

# Entry point: run demo only when executed as a script (prevents side effects on import)
if __name__ == "__main__":
    main()
