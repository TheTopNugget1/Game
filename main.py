# Reference section ----------------------------------------------------------------------------------------------------

# These are the sites I used to help me get a handel on Python and Pycharm
# https://www.youtube.com/watch?v=YWN8GcmJ-jA - for learning how to use pygame
# https://www.youtube.com/watch?v=mDKM-JtUhhc - for learning the best ways to use python

# Brief section --------------------------------------------------------------------------------------------------------

# I am going to make a platform shooter game called Brr, in python.
# BRR is a visual 2d platformer with added combat as a side thingy, I am going to be making this in pygame.

# The premise of the game is that you are a prisoner of war and are imprisoned on an enemy warship,
# Your goal is to escape on an escape pod.

# After the loading screen the player has a choice between 2 characters, a melee and a ranger survivor.
# There are going to at least 3 levels and all of them are quite long.
# Once you finish each section in each level you gain a buff to your basic stats.
# Your basic stats are movement speed, jump height, and fire rate.
# There will also be enemy turrets that attack the player, and these may come in various types.

# When you finish the last area the game displays “You Have Escaped!”

# -Player
#  •	One-shot death.
#  •	Is able to move in all directions.
#  •	Melee or ranged attacks.
#  •	Has a changeable movement speed and jump height and fire rate.
# -Turrets
#  •	One-shot death.
#  •	Locked in place.
#  •	Ranged fire.
# -Game world
#  •	Scrolling camera.
#  •	3 areas
#  •	Platforms are stationary, moving or bouncy.
# -User interface
#  •	Loading screen.
#  •	Game menu.
#  •	Character select.

# Imports section ------------------------------------------------------------------------------------------------------

import pygame
import sys

# Code section ---------------------------------------------------------------------------------------------------------


# Sprite class tiles
class Tile(pygame.sprite.Sprite):

    def __init__(self, height, width, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([height, width])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


# General Settings
pygame.init()
clock = pygame.time.Clock()

# Game Screen

# First Level Map
level_map = [
    '                    ',  # 1
    '                    ',  # 2
    '                    ',  # 3
    '                    ',  # 4
    '                    ',  # 5
    '                    ',  # 6
    '           X        ',  # 7
    '                    ',  # 8
    '      XXXXXXXXX     ',  # 9
    'XXXXXXXXXXXXXXX   XX'   # 10
] 

# Screen settings
block_size = 64
screen_width = 1200
screen_height = len(level_map) * block_size
screen = pygame.display.set_mode((screen_width, screen_height))
test_tile = Tile(50, 50, 100, 100, (255, 0, 0))

# Print output
print(screen_width)
print(screen_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    test_tile.draw(screen)

    pygame.display.update()
    clock.tick(60)
