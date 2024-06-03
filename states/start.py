#Displays the start menu
import pygame
from config import *
from gui.buttons import Button

class Start:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen

        self.intro_background = pygame.image.load('./img/introBackground.png')
        self.intro_background = pygame.transform.scale(self.intro_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.title = self.game.font_title.render('AFTERMATH', True, WHITE)
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH/2, 100))
        
        self.play_button = Button((SCREEN_WIDTH/2) - 275, SCREEN_HEIGHT - 100, 150, 50, WHITE, BLACK, '(P)lay', FNT_TITLE, 32)        
        self.quit_button = Button((SCREEN_WIDTH/2) + 175, SCREEN_HEIGHT - 100, 150, 50, WHITE, BLACK, '(Q)uit', FNT_TITLE, 32)   
        
    def run(self):     
        #Sometimes the mixer likes to play on its own, so we'll stop it here
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

        #Process Events
        #for event in pygame.event.get():
        #    if event.type == self.game.ON_STARTSCREEN:
        #         pygame.event.post(pygame.event.Event(self.game.ON_STARTSCREEN))
        #     if event.type == pygame.VIDEORESIZE:
        #         self.intro_background = pygame.transform.smoothscale(self.intro_background, self.screen.get_size())


        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        keys = pygame.key.get_pressed()
        if self.play_button.is_pressed(mouse_pos, mouse_pressed) or keys[pygame.K_p]:
            pygame.event.post(pygame.event.Event(self.game.ON_NEWGAME))
        elif self.quit_button.is_pressed(mouse_pos, mouse_pressed) or keys[pygame.K_q]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        self.screen.blit(self.intro_background, (0, 0))
        self.screen.blit(self.title, self.title_rect)      
        self.screen.blit(self.play_button.image, self.play_button.rect)
        self.screen.blit(self.quit_button.image, self.quit_button.rect)