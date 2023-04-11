import pygame 
from pygame.locals import *

class Snake:
    def __init__(self, parent_window, length):
        self.window = parent_window
        self.length = length

        self.block = pygame.image.load("media/block.png").convert()
        # block size
        self.h, self.w = self.block.get_rect().size
        self.x = [self.w] * length 
        self.y = [self.h] * length
        self.stepsize = self.h
        self.direction = 'right'

    def draw(self):
        for i in range(self.length):
            self.window.surface.blit(self.block, (self.x[i], self.y[i]))
        # pygame.display.update()

    def move_up(self):
        self.direction = 'up'
        return (self.y[0] - self.stepsize >= 0)

    def move_down(self):
        self.direction = 'down'
        return (self.y[0] + self.stepsize <= self.window.h - self.h)

    def move_left(self):
        self.direction = 'left'
        return (self.x[0] - self.stepsize >= 0)
    
    def move_right(self):
        self.direction = 'right'
        return (self.x[0] + self.stepsize <= self.window.w - self.w)
    
    def move_body(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
    
    def walk(self):
        if self.direction == 'up':
            res = self.move_up()
            if res:
                self.move_body()
                self.y[0] -= self.stepsize

        elif self.direction == 'down':
            res = self.move_down()
            if res:
                self.move_body()
                self.y[0] += self.stepsize

        elif self.direction == 'left':
            res = self.move_left()
            if res:
                self.move_body()
                self.x[0] -= self.stepsize

        else:
            res = self.move_right()
            if res:
                self.move_body()
                self.x[0] += self.stepsize
        
        self.draw()
    
    def update_direction(self, direction):
        self.direction = direction 
    
    def lengthen(self):
        self.length += 1
        self.x.append(self.x[-1])
        self.y.append(self.y[-1])