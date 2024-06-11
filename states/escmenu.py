import time
import pygame
from config import *
from gui.buttons import Button

class EscMenu:
    def __init__(self, game, screen, bkgImg):
        self.game = game
        self.screen = screen
        self.bkgImg = bkgImg
        
        self.text = self.game.font_title.render('GAME PAUSED', True, WHITE)
        self.text_rect = self.text.get_rect(topleft=(338, 28))

        self.resume_button = Button(565, 284, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, '(R)esume', FNT_TITLE, 32)
        self.quit_button = Button(565, 581, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, '(Q)uit', FNT_TITLE, 32)
    
    def run(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        keys = pygame.key.get_pressed()
        if self.resume_button.is_pressed(mouse_pos, mouse_pressed) or keys[pygame.K_r]:
            print("resume")
            pygame.event.post(pygame.event.Event(self.game.ON_RESUME))
                
        if self.quit_button.is_pressed(mouse_pos, mouse_pressed) or keys[pygame.K_q]:
            print("start")
            pygame.event.post(pygame.event.Event(self.game.ON_STARTSCREEN))
            
            
        #Blit to screen
        self.screen.fill(BLACK)
        self.screen.blit(self.bkgImg, (0, 0))
        self.screen.blit(self.text, self.text_rect.topleft)
        self.screen.blit(self.resume_button.image, self.resume_button.rect)
        self.screen.blit(self.quit_button.image, self.quit_button.rect)        
        