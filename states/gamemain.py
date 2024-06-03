#This is the main game state. It is largely a container and controller for substates.
import pygame
from gamestatemanager import GameStateManager
from states.fieldmap import FieldMap
from states.escmenu import EscMenu
from states.slotsgame import Slots
from config import *

class GameMain:
    def __init__(self, game, screen):
        self.screen = screen
        self.game = game

        self.subStateManager = GameStateManager('fieldmap')
        self.fieldmap = FieldMap(self.game, self.screen)
        self.escmenu = EscMenu(self.game, self.screen, None)
        self.slots = Slots(self.game, self.screen)

        self.subStates = {'fieldmap':self.fieldmap, 'escmenu':self.escmenu, 'slots':self.slots}
        
        self.clock = pygame.time.Clock()
        self.timer = 0
        
    def run(self):
        self.subStates[self.subStateManager.get_state()].run()
        #Manage events for the game substates  
        for event in self.game.events:
             if event.type == self.game.ON_RESUME:
                 self.subStateManager.set_state('fieldmap')     
             elif event.type == self.game.ON_STARTSCREEN:
                 pygame.event.post(pygame.event.Event(self.game.ON_STARTSCREEN))
             elif event.type == pygame.KEYUP:
                 if event.key == pygame.K_ESCAPE:
                     if self.subStateManager.currentState == 'fieldmap':
                        self.escmenu.bkgImg = self.fieldmap.image
                        self.subStateManager.set_state('escmenu')
                     elif self.subStateManager.currentState == 'escmenu':
                        self.subStateManager.set_state('fieldmap')   
