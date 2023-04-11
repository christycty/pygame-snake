import pygame 
from pygame.locals import *
import random

class Apple:
    def __init__(self, parent_window, snake_size):
        self.image = pygame.image.load("media/apple.jpg").convert()
        self.window = parent_window

        self.snake_size = snake_size
        self.x = 3 * self.snake_size
        self.y = 3 * self.snake_size
    
    def draw(self):
        self.window.surface.blit(self.image, (self.x, self.y))
        # pygame.display.flip()
    
    def update(self):
        self.x = random.randint(0, self.window.w / self.snake_size - 1)
        self.y = random.randint(0, self.window.h / self.snake_size - 1)
        self.x *= self.snake_size
        self.y *= self.snake_size
