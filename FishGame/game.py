#FishGame
#Sam Virsik

import pygame
import random
import sys
import time

from fish import Fish
from fsm import FSM
from harpoon import Harpoon
from person import Person

pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
FPS = 60
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FishGame")

background_img = pygame.image.load("Images/GOPR1518.JPG")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load images
person_img = pygame.image.load("Images/character.png")
harpoon_img = pygame.image.load("Images/harpoon.png")
coast_guard_img = pygame.image.load("Images/Coast Guard.jpg")

gray_snapper = pygame.image.load("Images/Gray snapper.png")
goliath_grouper = pygame.image.load("Images/Goliath Grouper.png")
snook = pygame.image.load("Images/Snook.png")
yellowfin_tuna = pygame.image.load("Images/Yellowfin Tuna.png")
tarpon = pygame.image.load("Images/TarponFish.png")

gray_snapper = pygame.transform.scale(gray_snapper, (200, 100))
goliath_grouper = pygame.transform.scale(goliath_grouper, (300, 150))
snook = pygame.transform.scale(snook, (250, 75))
yellowfin_tuna = pygame.transform.scale(yellowfin_tuna, (300, 150))
tarpon = pygame.transform.scale(tarpon, (225, 125))

coast_guard_img = pygame.transform.scale(coast_guard_img, (500, 300))
person_img = pygame.transform.scale(person_img, (250, 100))
harpoon_img = pygame.transform.scale(harpoon_img, (int(harpoon_img.get_width() * 0.085), int(harpoon_img.get_height() * 0.085)))

#(image, speed, score)
fish_info = {"gray_snapper": (gray_snapper, 2, 15), "goliath_grouper": (goliath_grouper, 1, 100), "snook": (snook, 3, 20), "yellowfin_tuna": (yellowfin_tuna, 4, 50), "tarpon": (tarpon, 2, 75)} 

#To store all types of caught fish
illegal_fish = ["goliath_grouper", "tarpon"]

caught_fish = []

#class Game_Bot:
#    def __init__(self, initial_state):

#myFSM = FSM("hi!")

def check_for_illegals():
    for i in illegal_fish:
        if i in caught_fish:
            return True
    return False

def tell_legal_status():
    if check_for_illegals():
        font = pygame.font.Font(None, 36)
        message = font.render("You board your boat", True, (0, 0, 0))
        screen.blit(message, (10, 20))
        pygame.display.flip()
        time.sleep(0.5)
        font = pygame.font.Font(None, 36)
        message = font.render("You look at your catch", True, (0, 0, 0))
        screen.blit(message, (30, 50))
        pygame.display.flip()
        time.sleep(0.5)
        font = pygame.font.Font(None, 36)
        message = font.render("Uh oh", True, (0, 0, 0))
        screen.blit(message, (60, 80))
        pygame.display.flip()
        time.sleep(0.5)
        font = pygame.font.Font(None, 36)
        message = font.render("You caught some illegal fish", True, (0, 0, 0))
        screen.blit(message, (70, 110))
        pygame.display.flip()
        time.sleep(0.5)
        font = pygame.font.Font(None, 36)
        message = font.render("You look up", True, (0, 0, 0))
        screen.blit(message, (100, 140))
        pygame.display.flip()
        time.sleep(2)
        font = pygame.font.Font(None, 80)
        message = font.render("The cops are chasing you", True, (255, 0, 0))
        screen.blit(message, (200, 200))
        pygame.display.flip()
        time.sleep(2)
        screen.blit(coast_guard_img, (400, 300))
        pygame.display.flip()
        time.sleep(2)

    else: 
        font = pygame.font.Font(None, 36)
        message = font.render("Yay you didn't catch any illegals!", True, (255, 0, 0))
        screen.blit(message, (10, 20))
        pygame.display.flip()
        time.sleep(5)

def make_new_fish():
    random_key = random.choice(list(fish_info.keys()))
    fish = Fish(random_key)
    all_sprites.add(fish)
    fishes.add(fish)

all_sprites = pygame.sprite.Group()
fishes = pygame.sprite.Group()
harpoons = pygame.sprite.Group()

player = Person()
all_sprites.add(player)
fish = Fish("gray_snapper")
all_sprites.add(fish)
fishes.add(fish)

score = 0
def spearfish(score):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                RUNNING[0] = False #Needed so that the game does not break into the code that goes after
    #chatGPT wrote the following 6 lines of code:
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    player.shoot()  # Trigger the same action as a spacebar press
        all_sprites.update()
        time.sleep(0.0000001) #neccessary because the movement has to be an integer, and the integer 1 is too big if theres no break - as in the default smallest speed is too fast without this
        if random.randint(1, 150) == 1: #causing some lag
            if len(fishes) < 10:
                make_new_fish()
        screen.blit(background_img, (0, 0))
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score} ", True, (255, 0, 0))
        screen.blit(score_text, (10, 20))
        all_sprites.draw(screen)
        pygame.display.flip()

        hits = pygame.sprite.groupcollide(fishes, harpoons, True, True)
        for hit in hits:
            for fish in hits: 
                score+=fish_info[fish.get_type()][2]
                caught_fish.append(fish.get_type())
        if score>200:
            running = False
    return score
#Main control center 
#Where FSM will need to be
score = spearfish(score)
if not RUNNING[0]:
    pygame.quit()
    sys.exit()
screen.fill((255, 255, 255))
pygame.display.flip()
time.sleep(1)
tell_legal_status()
pygame.quit()
sys.exit()