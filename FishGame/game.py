#FishGame
#Sam Virsik

import pygame
import random
import sys
import time

from spearfish import Spearfish #Class for running the spearfishing segment of the game
from fsm import FSM #Class for the finite state machine
from chase import Chase

pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
FPS = 60
WHITE = (255, 255, 255)
score = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FishGame")

chase = Chase(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
chase.run_game()

def set_up_transitions(fsm):
    #add_transition(input_symbol, state, action, next_state)
    fsm.add_transition("game_start", "spearfishing", "spearfish.run_game", "spearfishing")
    fsm.add_transition("done_spearfishing", "spearfishing", "spearfish.tell_legal_status", "review_catch")
    fsm.add_transition("no_illegals", "review_catch", "spearfish.run_game", "spearfishing")
    fsm.add_transition("are_illegals", "review_catch", "cops_chase", "chasing")
    fsm.add_transition("caught", "chasing", "game_over", "over")
    fsm.add_transition("not_caught", "chasing", "spearfish.run_game", "spearfishing")

fsm = FSM("spearfishing")
set_up_transitions(fsm) #gets the fsm transitions set up

spearfish = Spearfish(screen, SCREEN_WIDTH, SCREEN_HEIGHT, score)

input = "game_start"
running = True
while running:
    next = fsm.get_transition(input, fsm.current_state)
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
            spearfish = Spearfish(screen, SCREEN_WIDTH, SCREEN_HEIGHT, score)
            score = spearfish.run_game()
        input = "done_spearfishing"
    elif next[0] == "spearfish.tell_legal_status":
        input = spearfish.tell_legal_status()
    
    else: #for all non-special cases
        next[0]()
    fsm.current_state = next[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x): #make it easier to kill the game if needed
            running = False
            pygame.quit()

pygame.quit()
sys.exit()