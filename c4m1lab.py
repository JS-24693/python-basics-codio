# -----------------------------
# Lab Challenge: Inherit from parent class; override __init__
# -----------------------------
# parent class
class MP3:
    """Parent class representing an MP3 audio file 
    with artist, title, album, length, and genre."""
    def __init__(self, artist, title, album, length, genre):
        self.artist = artist
        self.title = title
        self.album = album
        self.length = length
        self.genre = genre
    
    def get_artist(self):
        return f"The artist is {self.artist}"
    
    def get_title(self):
        return f"The title is {self.title}"
    
    def get_album(self):
        return f"The album is {self.album}"
    
    def get_length(self):
        return f"The length is {self.length}"
    
    def get_genre(self):
        return f"The genre is {self.genre}"


# child class
class Podcast(MP3):
    """Child class representing a podcast episode with name, title, length, genre, and release date."""
    def __init__(self, name, title, length, genre, date):
        """Initialize podcast attributes: 
        name, title, length (sec), genre, and release date."""
        self.name = name
        self.title = title
        self.length = length
        self.genre = genre
        self.date = date

    def get_name(self):
        """Return formatted podcast name."""
        return f"The name is {self.name}"

    def get_title(self):
        """Return formatted podcast episode title."""
        return f"The title is {self.title}"

    def get_length(self):
        """Return podcast length in minutes and seconds."""
        minutes = self.length // 60
        seconds = self.length % 60
        return f"The length is {minutes} minutes and {seconds} seconds"

    def get_genre(self):
        """Return formatted podcast genre."""
        return f"The genre is {self.genre}"

    def get_date(self):
        """Return formatted podcast release date."""
        return f"The date is {self.date}"

p = Podcast("Planet Money", "Hollywood's Black List", 1460, "economics", "10 July 2020")

print(p.get_name())	    # The name is Planet Money
print(p.get_title())	# The title is Hollywood's Black List
print(p.get_length())	# The length is 24 minutes and 20 seconds
print(p.get_genre())	# The genre is economics
print(p.get_date())	    # The date is 10 July 2020


import pygame
import math

# -----------------------------
# Lab 1: Draw Polygon
# -----------------------------
# Code in main loop
# pygame.draw.polygon(
#        window,
#        (231, 76, 60),
#        [(200, 0), (400, 200), (200, 400), (0, 200)]
#    )

# -----------------------------
# Lab 2: Parent Class - Hexagon
# -----------------------------
class Hexagon:
    """Draws a hexagon using polar → Cartesian conversion."""

    def __init__(self, center, radius, window):
        self.center = center
        self.radius = radius
        self.window = window
        self.points = 6
        self.angle = math.radians(360 / self.points)
        self.color = (179, 55, 113)
        self.stroke_weight = 3

    # helper method to convert polar coordinate system to Cartesian coordinate system
    def calculate_vertices(self):
        """Calculate 6 vertices using cosine and sine."""
        vertices = []
        for i in range(self.points + 1):
            x = math.cos(i * self.angle) * self.radius + self.center[0]
            y = math.sin(i * self.angle) * self.radius + self.center[1]
            vertices.append((x, y))
        return vertices

    def draw(self):
        """Draw the hexagon outline."""
        pygame.draw.polygon(
            self.window,
            self.color,
            self.calculate_vertices(),
            self.stroke_weight
        )


# -----------------------------------------
# Lab 3: Child Class - Polygon (Inheritance)
# -----------------------------------------
class Polygon(Hexagon):
    """General polygon with user-defined vertices and animation."""

    def __init__(self, center, radius, window, points, color=(179, 55, 113)):
        self.center = center
        self.radius = radius
        self.window = window
        self.points = points
        self.angle = math.radians(360 / self.points)
        self.color = color
        self.stroke_weight = 3
        self.grow = 0  # animation variable

    def calculate_vertices(self):
        """Override to animate polygon growth/shrink."""
        vertices = []
        length = self.calculate_length()

        for i in range(self.points + 1):
            x = math.cos(i * self.angle) * length + self.center[0]
            y = math.sin(i * self.angle) * length + self.center[1]
            vertices.append((x, y))
        return vertices
    
    def calculate_length(self):
        """Compute animated radius using sine wave."""
        self.grow += 0.1
        length = math.sin(self.grow) * self.radius
        return length

# -----------------------------
# PyGame Setup
# -----------------------------
pygame.init()
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Inheritance Animation")
clock = pygame.time.Clock()

# -----------------------------
# Global Variables
# -----------------------------
run = True
hexagon = Hexagon((200, 200), 125, window)
polygon1 = Polygon((200, 200), 140, window, 8, (255, 19, 30)) # grow/shrink
# Contrast elements:
# - different center
# - different radius
# - different number of points
# - different color
polygon2 = Polygon((120, 120), 90, window, 5, (0, 180, 255))    # grow/shrink

# -----------------------------
# Main Loop
# -----------------------------
while run:
    pygame.time.delay(100)
    window.fill((55, 55, 55))
    
    pygame.draw.polygon(
    window, 
    (231, 76, 60), 
    [(200, 0), 
     (400, 200), 
     (200, 400), 
     (0, 200)]
    ) # red diamond
    
    hexagon.draw()  # draW hexagon
    polygon1.draw()  # animated polygon
    polygon2.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()  # update window with any changes
    clock.tick(30)

pygame.quit()
