import pygame
import sys
from config import *

#Archived State machine manager
# class GameStateManager:
#     def __init__(self, currentState):
#         self.prevState = ""
#         self.currentState = currentState        
#     def get_state(self):
#         return self.currentState
#     def set_state(self, state):
#         self.prevState = self.currentState
#         self.currentState = state
#         print(self.currentState)
#     def get_prev_state(self):
#         return self.prevState

class GameState:
    def __init__(self):
        self.next_state = None
    
    def handle_events(self, events):
        pass
    
    def update(self):
        pass
    
    def draw(self, screen):
        pass
    
    def get_next_state(self):
        return self.next_state

# class GameStateManager:
#     def __init__(self, initial_state):
#         self.current_state = initial_state

#     def run(self, screen):
#         clock = pygame.time.Clock()
        
#         while True:
#             events = pygame.event.get()
#             for event in events:
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()

#             self.current_state.handle_events(events)
#             self.current_state.update()
#             self.current_state.draw(screen)

#             next_state = self.current_state.get_next_state()
#             if next_state is not None:
#                 self.current_state = next_state

#             pygame.display.flip()
#             clock.tick(FPS)