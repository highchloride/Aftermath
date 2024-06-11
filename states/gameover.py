#Displays the game over screen
import pygame
from gui.buttons import Button
from config import *
from tools import Tool

class GameOver:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
       
        #self.gameover_background = pygame.image.load('./img/introBackground.png')
        #self.gameover_background = pygame.transform.scale(self.gameover_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.bkg_screencopy = self.game.screencopy
        
        self.text = self.game.font_title.render('GAME OVER', True, WHITE)
        self.text_rect = self.text.get_rect(topleft=(388, 28))

        self.restart_button = Button(565, 284, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, '(R)estart', FNT_TITLE, 32)
        self.quit_button = Button(565, 581, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, '(Q)uit', FNT_TITLE, 32)

    def run(self):     
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        #keys = pygame.key.get_pressed()
        if self.restart_button.is_pressed(mouse_pos, mouse_pressed):
            pygame.event.post(pygame.event.Event(self.game.ON_NEWGAME))
                
        if self.quit_button.is_pressed(mouse_pos, mouse_pressed):
            pygame.event.post(pygame.event.Event(self.game.ON_STARTSCREEN))

        for event in self.game.events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    print("restart")
                    pygame.event.post(pygame.event.Event(self.game.ON_NEWGAME))
                elif event.key == pygame.K_q:
                    print("start")
                    pygame.event.post(pygame.event.Event(self.game.ON_STARTSCREEN))

        #self.screen.blit(self.gameover_background, (0, 0))
        self.screen.blit(Tool.SimpleBlur(self.game.screencopy), (0,0))    
        self.screen.blit(self.text, self.text_rect.topleft)
        self.screen.blit(self.restart_button.image, self.restart_button.rect)
        self.screen.blit(self.quit_button.image, self.quit_button.rect)
