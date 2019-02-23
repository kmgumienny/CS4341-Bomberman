# This is necessary to find the main code
import sys
sys.path.insert(0, '../bomberman')
# Import necessary stuff
from entity import CharacterEntity
from colorama import Fore, Back
import random
from reinforcement_utils import getState

class TestCharacter(CharacterEntity):

    
                        
    def __init__(self, name, avatar, x, y, states):
        CharacterEntity.__init__(self, name, avatar, x, y)
        self.states = states
        self.updated_states = {}
        self.last_move = None
                        
    def do(self, wrld):    
        state = getState(wrld, self, 3)
        if self.last_move != None:
            if state in self.updated_states:
                if self.last_move in self.updated_states[state]:
                    self.updated_states[state][self.last_move] = (self.updated_states[state][self.last_move][0]+1, 0)
                else:
                    self.updated_states[state][self.last_move] = (1, 0)
            else:
                self.updated_states[state] = {self.last_move: (1, 0)}
        
        possible_actions = [(1, 0, 0), (1, 1, 0), (1, -1, 0), (-1, 0, 0), (-1, 1, 0), (-1, -1, 0), (0, -1, 0), (0, 1, 0)]
                        #(0, 0, 1), (1, 0, 1), (1, 1, 1), (1, -1, 1), (-1, 0, 1), (-1, 1, 1), (-1, -1, 1), (0, -1, 1), (0, 1, 1)]
        
        curr_max = -999999999
        move = None
        if (not state in self.states):
            move = random.choice(possible_actions)
        else:
            for m, values in self.states[state].items():
                if values[1] > curr_max:
                    curr_max = values[1]
                    move = m
                    
            if random.random() < 10000.0/(self.states[state][move][0]):
                move = random.choice(possible_actions)
        x, y, b = move
        self.move(x, y)
        if b == 1:
            self.place_bomb()
            
        self.last_move = move
