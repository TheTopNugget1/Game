# Imports
import pygame


# Sprite class tiles
class Tile(pygame.sprite.Sprite):
    def __int__(self, height, width, pos_x, pos_y, color):
        super().__int__()
        self.image = pygame.Surface([height, width])
        self.image.fill(color)
        self.rect = self.image.get_rect()
