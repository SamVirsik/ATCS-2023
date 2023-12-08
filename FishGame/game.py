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
    total_fish = 0

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("FishGame")

    def make_tansitions(self):
        #add_transition(input_symbol, state, action, next_state)
        self.fsm.add_transition("game_start", "game_prep", self.spearfish_run_game, "spearfishing")

        self.fsm.add_transition("done_spearfishing", "spearfishing", self.spearfish_review_catch, "review_catch")

        self.fsm.add_transition("illegals", "review_catch", self.illegal_message, "ill_mes")
        self.fsm.add_transition("no_illegals", "review_catch", self.legal_message, "leg_mes")
        self.fsm.add_transition("no_illegals_max_fish", "review_catch", self.display_score, "game_end")

        self.fsm.add_transition("displayed", "ill_mes", self.cops_chase, "chasing")
        self.fsm.add_transition("displayed", "leg_mes", self.spearfish_run_game, "spearfishing")

        #self.fsm.add_transition("illegals", "tell_legal_status", self.cops_chase, "chasing")
        #self.fsm.add_transition("no_illegals", "tell_legal_status", self.spearfish_run_game, "spearfishing")
        #self.fsm.add_transition("no_illegals_max_fish", "tell_legal_status", self.display_score, "game_end")

        self.fsm.add_transition("score_displayed", "game_end") #End game
        
        self.fsm.add_transition("escaped", "chasing", self.tell_they_escaped, "display_escaped")
        self.fsm.add_transition("got_caught", "chasing", self.display_caught, "game_end")

        self.fsm.add_transition("done", "display_caught", self.display_score, "game_end")

        self.fsm.add_transition("escaped_max_fish", "chasing", self.display_score, "game_end")

        self.fsm.add_transition("told_them", "display_escaped", self.spearfish_run_game, "spearfishing")


    def run(self):
        #chase = Chase(self.screen, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        #chase.run_game()

        self.fsm = FSM("game_prep")
        self.make_tansitions()

        self.input = "game_start"
        self.running = True
        while self.running:
            self.fsm.process(self.input)
            #self.fsm.process(next)

        pygame.quit()
        sys.exit()

    def spearfish_run_game(self):
        self.spearfish = Spearfish(self.screen, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.score)
        self.score += self.spearfish.run_game() 
        self.total_fish += 10

        self.input = "done_spearfishing"

    def spearfish_review_catch(self):
        illegals = self.spearfish.check_for_illegals()
        if illegals:
            self.input = "illegals"
        elif (not illegals) and (self.total_fish >=50):
            self.input = "no_illegals_max_fish"
        elif not illegals:
            self.input = "no_illegals"

    def illegal_message(self):
        self.spearfish.tell_legal_status()
        del self.spearfish
        self.input = "displayed"

    def legal_message(self):
        self.spearfish.tell_legal_status()
        del self.spearfish
        self.input = "displayed"

    def cops_chase(self):
        self.chase = Chase(self.screen, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        caught = self.chase.run_game()
        if caught:
            self.input = "got_caught"
        else:
            self.input = "escaped"

    def display_score(self):
        self.screen.fill((255, 255, 255))
        pygame.display.flip()
        time.sleep(1)
        font = pygame.font.Font(None, 36)
        score = str(self.score)
        message = font.render(score, True, (0, 0, 0))
        self.screen.blit(message, (60, 80))
        pygame.display.flip()
        time.sleep(0.3)

        self.input = 


    def display_caught(self):
        self.screen.fill((255, 255, 255))
        pygame.display.flip()
        time.sleep(1)
        font = pygame.font.Font(None, 36)
        message = font.render("Uh oh", True, (0, 0, 0))
        self.screen.blit(message, (60, 80))
        pygame.display.flip()
        time.sleep(0.3)

        self.input = "score_displayed"

    def tell_they_escaped(self):
        self.screen.fill((255, 255, 255))
        pygame.display.flip()
        time.sleep(1)
        font = pygame.font.Font(None, 36)
        message = font.render("You Escaped!", True, (0, 0, 0))
        self.screen.blit(message, (60, 80))
        pygame.display.flip()
        time.sleep(0.3)

        self.input = "escaped"

    def display_score(self):
        pass

if __name__ == "__main__":
    game = FishGame()
    game.run()