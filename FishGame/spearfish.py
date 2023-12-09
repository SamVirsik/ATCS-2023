import pygame
import time
import random
from fish import Fish
from person import Person
from harpoon import Harpoon

class Spearfish(pygame.sprite.Sprite):
    def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, score = 0):
        super().__init__()
        self.screen = screen
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.set_up_images()
        self.caught_fish = []

        #The fish_info dictionary contains all the information needed about the fish
        #The first entry is the image, the second is the speed, and the third is the point value
        self.fish_info = {"gray_snapper": (self.fish_images[0], 2, 50), "goliath_grouper": (self.fish_images[1], 1, 2500), "snook": (self.fish_images[2], 3, 150), "yellowfin_tuna": (self.fish_images[3], 4, 200), "tarpon": (self.fish_images[4], 2, 100), "bonefish": (self.fish_images[5], 3, 75), "mahi_mahi": (self.fish_images[6], 3, 150), "nausau_grouper": (self.fish_images[7], 1, 400), "sailfish": (self.fish_images[8], 10, 700), "swordfish": (self.fish_images[9], 8, 1200), "wahoo": (self.fish_images[10], 10, 1600)} 
        self.illegal_fish = ["goliath_grouper", "snook", "tarpon", "bonefish", "nausau_grouper"]
        
        self.score = score

        #These are the groups of sprite. Using the pygame function makes collision handling easier
        self.all_sprites = pygame.sprite.Group()
        self.fishes = pygame.sprite.Group()
        self.harpoons = pygame.sprite.Group()

    def set_up_images(self):
        #First importing all the images
        self.gray_snapper = pygame.image.load("Images/Gray snapper.png")
        self.goliath_grouper = pygame.image.load("Images/goliath_grouper_f.png")
        self.snook = pygame.image.load("Images/snook_f.png")
        self.yellowfin_tuna = pygame.image.load("Images/Yellowfin Tuna.png")
        self.tarpon = pygame.image.load("Images/tarpon_f.png")
        self.bonefish = pygame.image.load("Images/bonefish_f.png")
        self.mahi_mahi = pygame.image.load("Images/mahi mahi.png")
        self.nausau_grouper = pygame.image.load("Images/nausau_f.png")
        self.sailfish = pygame.image.load("Images/sailfish.png")
        self.swordfish = pygame.image.load("Images/swordfish.png")
        self.wahoo = pygame.image.load("Images/wahoo.png")

        #Next I am scaling the images to be somewhat realistic and playable with 
        self.gray_snapper = pygame.transform.scale(self.gray_snapper, (200, 100))
        self.goliath_grouper = pygame.transform.scale(self.goliath_grouper, (300, 150))
        self.snook = pygame.transform.scale(self.snook, (250, 75))
        self.yellowfin_tuna = pygame.transform.scale(self.yellowfin_tuna, (300, 150))
        self.tarpon = pygame.transform.scale(self.tarpon, (300, 125))
        self.bonefish = pygame.transform.scale(self.bonefish, (200, 75))
        self.mahi_mahi = pygame.transform.scale(self.mahi_mahi, (250, 100))
        self.nausau_grouper = pygame.transform.scale(self.nausau_grouper, (250, 125))
        self.sailfish = pygame.transform.scale(self.sailfish, (350, 150))
        self.swordfish = pygame.transform.scale(self.swordfish, (350, 150))
        self.wahoo = pygame.transform.scale(self.wahoo, (325, 175))

        self.fish_images = [self.gray_snapper, self.goliath_grouper, self.snook, self.yellowfin_tuna, self.tarpon, self.bonefish, self.mahi_mahi, self.nausau_grouper, self.sailfish, self.swordfish, self.wahoo]

        self.person_img = pygame.image.load("Images/character.png")
        self.harpoon_img = pygame.image.load("Images/harpoon.png")
        self.coast_guard_img = pygame.image.load("Images/Coast Guard.jpg")

        self.coast_guard_img = pygame.transform.scale(self.coast_guard_img, (500, 300))
        self.person_img = pygame.transform.scale(self.person_img, (250, 100))
        self.harpoon_img = pygame.transform.scale(self.harpoon_img, (int(self.harpoon_img.get_width() * 0.085), int(self.harpoon_img.get_height() * 0.085)))

        self.background_img = pygame.image.load("Images/GOPR1518.JPG")
        self.background_img = pygame.transform.scale(self.background_img, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def check_for_illegals(self):
        for i in self.illegal_fish:
            if i in self.caught_fish:
                return True
        return False

    def tell_legal_status(self):
        #This function simply tells the user whether or not some of the fish 
        #They speared are illegal. This information is then returned so that the 
        #FSM can be updated accordingly. 

        self.screen.fill((255, 255, 255))
        pygame.display.flip()
        time.sleep(1)

        if self.check_for_illegals():
            font = pygame.font.Font(None, 36)
            message = font.render("Uh oh", True, (0, 0, 0))
            self.screen.blit(message, (60, 80))
            pygame.display.flip()
            time.sleep(0.3)
            font = pygame.font.Font(None, 36)
            message = font.render("You speared illegal fish", True, (0, 0, 0))
            self.screen.blit(message, (70, 110))
            pygame.display.flip()
            time.sleep(0.3)
            font = pygame.font.Font(None, 80)
            message = font.render("The cops are chasing you", True, (255, 0, 0))
            self.screen.blit(message, (200, 200))
            pygame.display.flip()
            time.sleep(1)
            self.screen.blit(self.coast_guard_img, (400, 300))
            pygame.display.flip()
            time.sleep(2)
            return "are_illegals"
        else: 
            font = pygame.font.Font(None, 36)
            message = font.render("Yay you didn't catch any illegals!", True, (255, 0, 0))
            self.screen.blit(message, (10, 20))
            pygame.display.flip()
            time.sleep(2)
            return "no_illegals"

    def make_new_fish(self):
        fish = Fish(self.fish_images, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.all_sprites.add(fish)
        self.fishes.add(fish)

    def run_game(self):
        self.player = Person(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.person_img)
        self.all_sprites.add(self.player)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
                    running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.shoot()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        self.shoot()  # Trigger the same action as a spacebar press
            self.all_sprites.update()
            time.sleep(0.0000001) #neccessary because the movement has to be an integer, and the integer 1 is too big if theres no break - as in the default smallest speed is too fast without this
            if random.randint(1, 150) == 1: #This just randomizes the spawn timing of the fish - so they don't all come in waves
                if len(self.fishes) < 10:
                    self.make_new_fish()
            self.screen.blit(self.background_img, (0, 0))
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {self.score} ", True, (255, 0, 0))
            self.screen.blit(score_text, (10, 20))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

            hits = pygame.sprite.groupcollide(self.fishes, self.harpoons, True, True)

            for fish in hits: 
                self.score+=self.fish_info[fish.get_type()][2]
                self.caught_fish.append(fish.get_type())
            if len(self.caught_fish)>10: #only 10 fish killed per time - then either it repeats or they get chased
                running = False
        return self.score
        
    def shoot(self):
        harpoon = Harpoon(self.player.rect.right, self.player.rect.centery, self.harpoon_img, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.all_sprites.add(harpoon)
        self.harpoons.add(harpoon)