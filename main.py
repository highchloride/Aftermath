import pygame
from sprites import *
from config import *
from states import *
import sys

#State Machine
from gamestatemanager import GameState
from states.start import Start
from states.fieldmap import FieldMap
# from states.start import Start
# from states.gameover import GameOver
# from states.gamemain import GameMain

class Game:
    #Custom Events
    ON_DEATH = pygame.event.custom_type()
    ON_NEWGAME = pygame.event.custom_type()
    ON_STARTSCREEN = pygame.event.custom_type()
    ON_RESUME = pygame.event.custom_type()
    
    running = False
    
    def __init__(self):
        pygame.init()    
        pygame.display.set_caption("AFTERMATH")
        pygame.font.init()
        pygame.mixer.init()
        
        #Creates the base screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
        #Base game clock
        self.clock = pygame.time.Clock()
        #Holds the blurred image background for gameMain menus
        self.screencopy = None
        #Title font
        self.font_title = pygame.font.Font(FNT_TITLE, 128)
        #One variable for one events call
        self.events = None
        #Persistent variable for the game 
        self.game = FieldMap(self, self.screen)
        
        pygame.key.set_repeat() 

        #State Machine
        #self.gameStateManager = GameStateManager('start')
        self.current_state = Start(self, self.screen)
        #initial_state = Start(self, self.screen)
        #self.manager = GameStateManager(initial_state)
        

        #State declarations
        # self.start = Start(self, self.screen)
        # self.gameover = GameOver(self, self.screen)
        # self.gamemain = GameMain(self, self.screen) #Parent for game substates
        
        #State dictionary
        #self.states = {'start':self.start, 'gamemain':self.gamemain, 'gameover':self.gameover}  


    #Largely either changes states or runs them
    def run(self):
        #time_delta = self.clock.tick(60)/1000.0
        
        while True:
            self.events = pygame.event.get()
            #Process Events
            # for event in self.events:
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         sys.exit()
            #     if event.type == self.ON_DEATH:
            #         self.gameStateManager.set_state('gameover')                    
            #     if event.type == self.ON_NEWGAME:
            #         self.gamemain = GameMain(self, self.screen)
            #         self.states.update({'gamemain':self.gamemain})
            #         self.gameStateManager.set_state('gamemain')
            #     if event.type == self.ON_STARTSCREEN:
            #         self.start = Start(self, self.screen)
            #         self.states.update({'start':self.start})
            #         self.gameStateManager.set_state('start')

            #Call the active state's run logic
            #self.states[self.gameStateManager.get_state()].run()

            #Call all other updates and tick the clock
            pygame.display.update()
            
#events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #if event.type == pygame.ON_NEWGAME:

            #self.current_state.handle_events(self.events)
            #self.current_state.update()
            #self.current_state.draw(self.screen)

            next_state = self.current_state.get_next_state()
            if next_state is not None:
                self.current_state = next_state

            pygame.display.flip()
            self.clock.tick(FPS)

       
#Insertion Point
if __name__ == '__main__':
    game = Game()
    game.run()