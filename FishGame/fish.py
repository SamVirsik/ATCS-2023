import pygame
import random

class Fish(pygame.sprite.Sprite):
    def __init__(self, fish_images, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        #Copy of the fish_info dictionary. Not all the info is needed here, but this is the easiest way to get the info I do need. 
        self.fish_info = {"gray_snapper": (fish_images[0], 2, 50), "goliath_grouper": (fish_images[1], 1, 2500), "snook": (fish_images[2], 3, 150), "yellowfin_tuna": (fish_images[3], 4, 200), "tarpon": (fish_images[4], 2, 100), "bonefish": (fish_images[5], 3, 75), "mahi_mahi": (fish_images[6], 3, 150), "nausau_grouper": (fish_images[7], 1, 400), "sailfish": (fish_images[8], 10, 700), "swordfish": (fish_images[9], 8, 1200), "wahoo": (fish_images[10], 10, 1600)} 

        self.type = random.choice(list(self.fish_info.keys()))

        self.image = self.fish_info[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 100)
        self.speed = self.fish_info[self.type][1]
        self.health = 50
        self.has_collided = False 

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

    def get_type(self):
        return self.type