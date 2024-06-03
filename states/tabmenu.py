import pygame
from config import *
from gui.buttons import Button

class TabMenu:
    def __init__(self, game, screen, bkgImg):
        self.game = game
        self.screen = screen
        self.bkgImg = bkgImg
        
        #self.top_menu_back = 
        
        
    def run(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.bkgImg, (0, 0))
        
