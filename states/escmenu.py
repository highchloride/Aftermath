import pygame
from config import *
from gui.buttons import Button

class EscMenu:
    def __init__(self, game, screen, bkgImg):
        self.game = game
        self.screen = screen
        self.bkgImg = bkgImg
        
        self.button_Return = Button((SCREEN_WIDTH/2) - 75, (SCREEN_HEIGHT/2) - 100, 200, 50, WHITE, BLACK, 'Return', FNT_TITLE, 32)  
        self.button_Quit = Button((SCREEN_WIDTH/2) - 75, (SCREEN_HEIGHT/2) + 100, 200, 50, WHITE, BLACK, 'Quit', FNT_TITLE, 32)  
    
    def run(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        if self.button_Return.is_pressed(mouse_pos, mouse_pressed):
            pygame.event.post(pygame.event.Event(self.game.ON_RESUME))
            
        if self.button_Quit.is_pressed(mouse_pos, mouse_pressed):
            pygame.event.post(pygame.event.Event(self.game.ON_STARTSCREEN))

        self.screen.fill(BLACK)
        self.screen.blit(self.bkgImg, (0, 0))
        self.screen.blit(self.button_Return.image, self.button_Return.rect)
        self.screen.blit(self.button_Quit.image, self.button_Quit.rect)        
        