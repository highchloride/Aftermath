from time import sleep
import pygame
import random
from config import *

class Slots:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen

        self.values = ["C","C","C","G","G","G","L","L","L","O","O","O","B","7","S"]
        self.reel1 = None
        self.reel2 = None
        self.reel3 = None
        print("Ready! Press R to spin!")
    
    def spin(self):
        self.reel1 = random.choice(self.values)
        self.reel2 = random.choice(self.values)
        self.reel3 = random.choice(self.values)
        print("Spinning...")
        sleep(1)
        
        print(self.reel1, self.reel2, self.reel3)
        print("Pull again?")

    def run(self):
        self.screen.fill(BLACK)
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.spin()
        
