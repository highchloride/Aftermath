#Displays the game over screen
import pygame
from gui.buttons import Button
from config import *
from tools import ImageTool

class GameOver:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
       
        self.gameover_background = pygame.image.load('./img/introBackground.png')
        self.gameover_background = pygame.transform.scale(self.gameover_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.bkg_screencopy = self.game.screencopy
        
        
        self.text = self.game.font_title.render('GAME OVER', True, WHITE)
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        self.restart_button = Button((SCREEN_WIDTH/2) - 225, SCREEN_HEIGHT - 100, 250, 50, WHITE, BLACK, '(R)estart', FNT_TITLE, 32)
        self.quit_button = Button((SCREEN_WIDTH/2) + 75, SCREEN_HEIGHT - 100, 150, 50, WHITE, BLACK, '(Q)uit', FNT_TITLE, 32)

    def run(self):     
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        keys = pygame.key.get_pressed()

        if self.restart_button.is_pressed(mouse_pos, mouse_pressed) or keys[pygame.K_r]:
            pygame.event.post(pygame.event.Event(self.game.ON_NEWGAME))
                
        if self.quit_button.is_pressed(mouse_pos, mouse_pressed) or keys[pygame.K_q]:
            pygame.event.post(pygame.event.Event(self.game.ON_STARTSCREEN))
            #pygame.event.post(pygame.event.Event(pygame.QUIT))

        #self.screen.blit(self.gameover_background, (0, 0))
        self.screen.blit(ImageTool.SimpleBlur(self.game.screencopy), (0,0))    
        self.screen.blit(self.text, self.text_rect.topleft)
        self.screen.blit(self.restart_button.image, self.restart_button.rect)
        self.screen.blit(self.quit_button.image, self.quit_button.rect)
