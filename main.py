import pygame
import time 
from pygame.locals import *
import snake
import apple

class Window:
    def __init__(self, w=520, h=520):
        self.w = w
        self.h = h
        self.surface = pygame.display.set_mode((self.w, self.h))
        
    def update(self):
        pygame.display.flip()

    def render_background(self):
        # bg = pygame.image.load("media/background.jpg")
        # self.surface.blit(bg, (0, 0))
        self.surface.fill((235, 235, 235))
    
    def play_background_music(self):
        pygame.mixer.music.load("media/bg_music_1.mp3")
        pygame.mixer.music.play()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("snake game :>")
        pygame.mixer.init()
        
        self.window = Window()
        self.window.play_background_music()
        self.snake = snake.Snake(self.window, 5)
        self.snake.draw()
        self.apple = apple.Apple(self.window, self.snake.h)
        self.running = True
        self.gameover = False
    
    def eat(self):
        return (self.snake.x[0] == self.apple.x and self.snake.y[0] == self.apple.y)

    def collide(self):
        for i in range(1, self.snake.length):
            if (self.snake.x[0] == self.snake.x[i] \
                and self.snake.y[0] == self.snake.y[i]):
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length-5}", True, (0, 0, 0))
        self.window.surface.blit(score, (800, 10))

    def display_game_over(self):
        self.window.render_background()
        font = pygame.font.SysFont('arial', 25)
        line1 = font.render(f"Game Over :(   Score: {self.snake.length-5}", True, (0, 0, 0))
        self.window.surface.blit(line1, (50, 200))
        line2 = font.render(f"Press Enter to replay, press Escape to exit", True, (0, 0, 0))
        self.window.surface.blit(line2, (50, 250))
        pygame.display.flip()


    def play_sound(self, sound):
        pygame.mixer.music.pause()
        sound = pygame.mixer.Sound(f"media/{sound}.mp3")
        pygame.mixer.Sound.play(sound)
        pygame.mixer.music.unpause()
    
    
    def reset_game(self):
        pygame.mixer.music.unpause()
        self.snake = snake.Snake(self.window, 5)
        self.snake.draw()
        self.apple = apple.Apple(self.window, self.snake.h)
        self.gameover = False

    def play(self):
        self.window.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.eat():
            self.play_sound("ding")
            self.apple.update()
            self.snake.lengthen()
        
        if self.collide():
            self.play_sound("crash")
            pygame.mixer.music.pause()
            self.display_game_over()
            self.gameover = True
    
    # Game Loop
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False 

                    if not self.gameover:
                        if event.key == K_UP:
                            self.snake.update_direction('up')
                            
                        if event.key == K_DOWN:
                            self.snake.update_direction('down')

                        if event.key == K_LEFT:
                            self.snake.update_direction('left')

                        if event.key == K_RIGHT:
                            self.snake.update_direction('right')
                    
                    else:
                        if event.key == K_RETURN:
                            self.reset_game()
                    
                elif event.type == QUIT:
                    self.running = False  
            
            if not self.gameover:
                self.play()
            time.sleep(0.1)

if __name__ == "__main__":
    game = Game()
    game.run()