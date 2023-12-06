#FishGame
#Sam Virsik

import pygame
import random
import sys
import time

from spearfish import Spearfish #Class for running the spearfishing segment of the game
from fsm import FSM #Class for the finite state machine
from chase import Chase

class FishGame:
    SCREEN_WIDTH = 1100
    SCREEN_HEIGHT = 700
    FPS = 60
    WHITE = (255, 255, 255)
    score = 0

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("FishGame")

    def make_tansitions(self):
        #add_transition(input_symbol, state, action, next_state)
        self.fsm.add_transition("game_start", "game_prep", self.spearfish_run_game, "spearfishing")

        self.fsm.add_transition("done_spearfishing", "spearfishing", "spearfish_review_catch", "review_catch")

        self.fsm.add_transition("done_reviewing", "review_catch", "tell_legal_status", "tell_legal_status")

        self.fsm.add_transition("illegals", "tell_legal_status", "cops_chase", "chasing")
        self.fsm.add_transition("no_illegals", "tell_legal_status", "spearfish_run_game", "spearfishing")
        self.fsm.add_transition("no_illegals_max_fish", "tell_legal_status", "display_score", "game_end")

        self.fsm.add_transition("score_displayed", "game_end") #End game

        self.fsm.add_transition("escaped", "chasing", "tell_they_escaped", "display_escaped")
        self.fsm.add_transition("got_caught", "chasing", "display_score", "game_end")

        self.fsm.add_transition("escaped_max_fish", "chasing", "display_score", "game_end")

        self.fsm.add_transition("told_them", "display_escaped", "spearfish_run_game", "spearfishing")


    def run(self):
        chase = Chase(self.screen, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        chase.run_game()

        self.fsm = FSM("game_prep")
        self.make_tansitions()
        #spearfish = Spearfish(screen, SCREEN_WIDTH, SCREEN_HEIGHT, score)

        input = "game_start"
        running = True
        while running:
            next = self.fsm.process(input)

            self.fsm.process(next)
            #The reason that there are if statements for the FSM and not just 
            # simple function calls is because some of the next actions cannot 
            # be described simply in a function call. Thus the FSM gives us the 
            # info we need about where we are and the if statements encode ALL 
            # of the thing we need to do next in the game. 
            # For example I need to college the variable score from spearfish.run_game()
            # but that cannot be done in the usual action() type call. 

            #The FSM uses a dictionary - not if statements. This is just for 
            # more complicated next actions:


            #instead of this nasty method, simply make a function for each raw input that then processes the input and calls all the neccessary. Don't have these if statements for it, just direct it to a function based on what string it is
            if next[0] == "spearfish.run_game":
                if input == "game_start": #if its not the first time I want to delete the spearfishing instance of the past
                    score = spearfish.run_game()
                else: 
                    del spearfish
                    spearfish = Spearfish(self.screen, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, score)
                    score = spearfish.run_game()
                input = "done_spearfishing"
            elif next[0] == "spearfish.tell_legal_status":
                input = spearfish.tell_legal_status()
            
            else: #for all non-special cases
                next[0]()
            self.fsm.current_state = next[1]
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x): #make it easier to kill the game if needed
                    running = False
                    pygame.quit()

        pygame.quit()
        sys.exit()

    def spearfish_run_game(self):
        pass
    def spearfish_review_catch():
        pass
    def tell_legal_status():
        pass
    def cops_chase():
        pass
    def display_score():
        pass
    def tell_they_escaped():
        pass
    def display_score():
        pass

if __name__ == "__main__":
    game = FishGame()
    game.run()