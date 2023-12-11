#FishGame
#Sam Virsik

import pygame
import sys
import time

from spearfish import Spearfish
from fsm import FSM
from chase import Chase

class FishGame:
    SCREEN_WIDTH = 1100
    SCREEN_HEIGHT = 700
    FPS = 60
    WHITE = (255, 255, 255)
    score = 0
    total_fish = 0
    got_caught = False
    num_cops_chase = 0 #this is the number of times they have been chased. Important for knowing how hard to make each cops chase

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("FishGame")

    def make_tansitions(self):
        #General form: add_transition(input_symbol, state, action, next_state)
        self.fsm.add_transition("game_start", "game_prep", self.spearfish_run_game, "spearfishing")

        self.fsm.add_transition("done_spearfishing", "spearfishing", self.spearfish_review_catch, "review_catch")

        self.fsm.add_transition("illegals", "review_catch", self.illegal_message, "ill_mes")
        self.fsm.add_transition("no_illegals", "review_catch", self.legal_message, "leg_mes")
        self.fsm.add_transition("no_illegals_max_fish", "review_catch", self.display_score, "game_end")

        self.fsm.add_transition("displayed", "ill_mes", self.cops_chase, "chasing")
        self.fsm.add_transition("displayed", "leg_mes", self.spearfish_run_game, "spearfishing")

        self.fsm.add_transition("score_displayed", "game_end", self.end_game, "over") #End game
        
        self.fsm.add_transition("escaped", "chasing", self.tell_they_escaped, "display_escaped")
        self.fsm.add_transition("got_caught", "chasing", self.display_score, "game_end")

        self.fsm.add_transition("escaped_max_fish", "chasing", self.display_score, "game_end")

        self.fsm.add_transition("told_them", "display_escaped", self.spearfish_run_game, "spearfishing")

    def run(self):
        self.fsm = FSM("game_prep")
        self.make_tansitions()

        self.input = "game_start"
        self.running = True
        while self.running:
            self.fsm.process(self.input)
        pygame.quit()
        sys.exit()

    def spearfish_run_game(self):
        self.spearfish = Spearfish(self.screen, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.score)
        self.score = self.spearfish.run_game() 
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
        caught = self.chase.run_game(3 + self.num_cops_chase)
        if not caught and (self.total_fish >=50):
            self.input = "escaped_max_fish"
        elif caught:
            self.score = 0
            self.input = "got_caught"
            self.got_caught = True
        elif not caught:
            self.input = "escaped"
        self.num_cops_chase += 1

    def display_score(self):
        self.screen.fill((255, 255, 255))
        pygame.display.flip()
        time.sleep(1)

        if self.got_caught:
            font = pygame.font.Font(None, 36)
            message = font.render("You got caught! All fish were confiscated.", True, (0, 0, 0))
            self.screen.blit(message, (60, 80))
            pygame.display.flip()
            time.sleep(1.5)

        font = pygame.font.Font(None, 100)
        message = font.render("Final Score: " + str(self.score), True, (0, 0, 0))
        self.screen.blit(message, (200, 200))
        pygame.display.flip()
        time.sleep(3)

        self.input = "score_displayed"

    def tell_they_escaped(self):
        self.screen.fill((255, 255, 255))
        pygame.display.flip()
        time.sleep(1)
        font = pygame.font.Font(None, 36)
        message = font.render("You Escaped!", True, (0, 0, 0))
        self.screen.blit(message, (60, 80))
        pygame.display.flip()
        time.sleep(1)

        news = pygame.image.load("Images/news_article.png")
        news = pygame.transform.scale(news, (800, 250))
        self.screen.blit(news, (200, 200))
        pygame.display.flip()
        time.sleep(3)

        self.input = "told_them"
    
    def end_game(self):
        self.running = False

if __name__ == "__main__":
    game = FishGame()
    game.run()