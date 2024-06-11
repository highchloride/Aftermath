import pygame

#State machine manager
class GameStateManager:
    def __init__(self, currentState):
        self.prevState = ""
        self.currentState = currentState        
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.prevState = self.currentState
        self.currentState = state
        print(self.currentState)
    def get_prev_state(self):
        return self.prevState
