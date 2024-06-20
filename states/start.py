#Displays the start menu
import pygame
from config import *
from gamestatemanager import GameState
from states.fieldmap import FieldMap
from gui.buttons import Button

class Start(GameState):
    def __init__(self, game, screen):
        super().__init__()
        self.game = game
        self.screen = screen
        self.title = self.game.font_title.render('AFTERMATH', True, WHITE)
        self.title_rect = self.title.get_rect(topleft=(391,28))
        
        self.play_button = Button(565, 284, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, 'New Game', FNT_TITLE, 32)
        self.quit_button = Button(565, 581, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, 'Quit', FNT_TITLE, 32)

    def handle_events(self, events):
        # for event in events:
        #     if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        #         self.next_state = GameplayState()
        pass
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        if self.play_button.is_pressed(mouse_pos, mouse_pressed):
            #pygame.event.post(pygame.event.Event(self.game.ON_NEWGAME))
            self.next_state = self.game
        elif self.quit_button.is_pressed(mouse_pos, mouse_pressed):
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def draw(self, screen):
        self.screen.fill(ORANGE)    
        self.screen.blit(self.title, self.title_rect)      
        self.screen.blit(self.play_button.image, self.play_button.rect)
        self.screen.blit(self.quit_button.image, self.quit_button.rect)

# class Start:
#     def __init__(self, game, screen):
#         self.game = game
#         self.screen = screen

        #self.intro_background = pygame.image.load('./img/introBackground.png')
        #self.intro_background = pygame.transform.scale(self.intro_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # self.title = self.game.font_title.render('AFTERMATH', True, WHITE)
        # self.title_rect = self.title.get_rect(topleft=(391,28))
        
        # self.play_button = Button(565, 284, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, 'New Game', FNT_TITLE, 32)
        # self.quit_button = Button(565, 581, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, 'Quit', FNT_TITLE, 32)

    #def run(self):     
        #Sometimes the mixer likes to play on its own, so we'll stop it here
        # if pygame.mixer.music.get_busy():
        #     pygame.mixer.music.stop()

        #Process Events
        #for event in pygame.event.get():
        #    if event.type == self.game.ON_STARTSCREEN:
        #         pygame.event.post(pygame.event.Event(self.game.ON_STARTSCREEN))
        #     if event.type == pygame.VIDEORESIZE:
        #         self.intro_background = pygame.transform.smoothscale(self.intro_background, self.screen.get_size())

        # mouse_pos = pygame.mouse.get_pos()
        # mouse_pressed = pygame.mouse.get_pressed()
        
        # if self.play_button.is_pressed(mouse_pos, mouse_pressed):
        #     pygame.event.post(pygame.event.Event(self.game.ON_NEWGAME))
        # elif self.quit_button.is_pressed(mouse_pos, mouse_pressed):
        #     pygame.event.post(pygame.event.Event(pygame.QUIT))

        #self.screen.blit(self.intro_background, (0, 0))
        # self.screen.fill(ORANGE)    
        # self.screen.blit(self.title, self.title_rect)      
        # self.screen.blit(self.play_button.image, self.play_button.rect)
        # self.screen.blit(self.quit_button.image, self.quit_button.rect)
