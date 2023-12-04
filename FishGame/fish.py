import pygame
import random

class Fish(pygame.sprite.Sprite):
    def __init__(self, fish_images, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        #For updating the fish and adding more, do this: 
            #Change the dictionary with new info
            #Put in new images
            #Ensure the images are uploaded to the main
            #Include the image files in fish_images
            #update this method slightly, and the illegal fish list
        self.fish_info = {"gray_snapper": (fish_images[0], 2, 15), "goliath_grouper": (fish_images[1], 1, 100), "snook": (fish_images[2], 3, 20), "yellowfin_tuna": (fish_images[3], 4, 50), "tarpon": (fish_images[4], 2, 75), "bonefish": (fish_images[5], 3, 200), "mahi_mahi": (fish_images[6], 3, 75), "nausau_grouper": (fish_images[7], 1, 250), "sailfish": (fish_images[8], 10, 400), "swordfish": (fish_images[9], 8, 300), "wahoo": (fish_images[10], 10, 500)} 

        self.type = random.choice(list(self.fish_info.keys()))

        self.image = self.fish_info[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 100)
        self.speed = self.fish_info[self.type][1]
        self.health = 50
        self.has_collided = False  # Flag to track collision

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

    def get_type(self):
        return self.type