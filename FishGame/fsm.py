import pygame

#Same code as past FSM

class FSM:
    def __init__(self, initial_state):
        self.state_transitions = {}
        self.current_state = initial_state

    def add_transition(self, input_symbol, state, action=None, next_state=None):
        if next_state == None:
            self.state_transitions[(input_symbol, state)] = (action, self.current_state)
        else:
            self.state_transitions[(input_symbol, state)] = (action, next_state)

    def get_transition(self, input_symbol, state):
        return self.state_transitions[(input_symbol, state)]

    def process(self, input_symbol):
        action = self.get_transition(input_symbol, self.current_state)
        if action[0] is not None:
            action[0]()
        if action[1] is not None:
            self.current_state = action[1]