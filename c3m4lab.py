# Mutability Labs: Pygame animation + object methods 
# Install in terminal first: pip install pygame  

import pygame
import random

# -----------------------------
# Draw Shapes shown on window when pygame opens
# -----------------------------

def return_shapes():
    """Return a list of shape descriptions to be drawn each frame."""
    return [
        {"type": "circle", "color": (0, 255, 0), "pos": (50, 50), "r": 20},
        {"type": "rect", "color": (0, 0, 255), "rect": (100, 100, 60, 40)},
    ]

# -----------------------------
# Ball Class
# -----------------------------
class Ball:
    """Bouncing ball with movement, color change, and random velocity"""

    def __init__(self, surface, color, x, y, r):
        self.surface = surface
        self.color = color
        self.x = int(x)
        self.y = int(y)
        self.r = r
        self.vel_x = Ball.random_velocity()   # random horizontal velocity
        self.vel_y = Ball.random_velocity()   # random vertical velocity

    def draw(self):
        """Draw ball on screen"""
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.r)

    def update(self):
        """Update ball each frame"""
        self.move()
        self.bounce()

    def move(self):
        """Move ball by velocity"""
        self.x += self.vel_x
        self.y += self.vel_y

    def bounce(self):
        """Bounce ball off window edges and change color"""
        if self.x < self.r or self.x > WIDTH - self.r:
            self.vel_x *= -1
            self.change_color()

        if self.y < self.r or self.y > HEIGHT - self.r:
            self.vel_y *= -1
            self.change_color()

    def change_color(self):
        """Assign random RGB color"""
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        self.color = (red, green, blue)

    @staticmethod
    def random_velocity():
        """Return random velocity between -3 and -1 or 1 and 3"""
        direction = random.choice(["positive", "negative"])
        if direction == "positive":
            return random.randint(1, 3)
        else:
            return random.randint(-3, -1)

# -----------------------------
# Zoo Class Challenge
# -----------------------------
class Zoo:
    """Zoo with animal counts"""

    def __init__(self, big_cats, primates, reptiles, birds):
        self.big_cats = big_cats
        self.primates = primates
        self.reptiles = reptiles
        self.birds = birds

    def total_animals(self):
        """Return total number of animals"""
        return self.big_cats + self.primates + self.reptiles + self.birds

    def total_mammals(self):
        """Return number of mammals (big cats + primates)"""
        return self.big_cats + self.primates

    def most_animals(self):
        """Return category with most animals"""
        if self.big_cats > self.primates and \
           self.big_cats > self.reptiles and \
           self.big_cats > self.birds:
            return "big cats"
    
        if self.reptiles > self.big_cats and \
           self.reptiles > self.primates and \
           self.reptiles > self.birds:
            return "reptiles"

        if self.primates > self.big_cats and \
           self.primates > self.reptiles and \
           self.primates > self.birds:
            return "primates"
        
        if self.birds > self.big_cats and \
           self.birds > self.primates and \
           self.birds > self.reptiles:
            return "birds"

# test conditions
my_zoo = Zoo(10, 30, 90, 120)
print(my_zoo.total_animals())  # 250
print(my_zoo.total_mammals())  # 40
print(my_zoo.most_animals())   # birds

# -----------------------------
# Pygame Setup
# -----------------------------
pygame.init()                   # initialize pygame

WIDTH = 400
HEIGHT = 400

window = pygame.display.set_mode((WIDTH, HEIGHT)) # create a window
pygame.display.set_caption("Bouncing Ball")       # create a caption
clock = pygame.time.Clock()                       # clock controls animation speed

ball = Ball(window, (255, 0, 0), WIDTH // 2, HEIGHT // 2, 20)

# get shapes to draw
SHAPES = return_shapes()

# -----------------------------
# Main Loop to keep window open and lookfor pygame.QUIT
# -----------------------------
run = True
while run:
    pygame.time.delay(100)
    window.fill((120, 120, 120))  # background color
    # draw shapes
    for s in SHAPES:
        if s["type"] == "circle":
            pygame.draw.circle(window, s["color"], s["pos"], s["r"])
        elif s["type"] == "rect":
            pygame.draw.rect(window, s["color"], s["rect"])

    ball.draw()
    ball.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
