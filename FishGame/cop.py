import pygame
import random

class Cop(pygame.sprite.Sprite):
    def __init__(self, image, image_2, SCREEN_WIDTH, SCREEN_HEIGHT, x, y):
        super().__init__()
        self.image_default = image
        self.image_chasing = image_2 #the red colored boat for when its chasing them
        self.image = image
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.rect = self.image.get_rect()
        self.speed = 2
        self.rect.x=x
        self.rect.y=y
        self.move_to_x = random.randint(0, self.SCREEN_WIDTH)
        self.move_to_y = random.randint(0, self.SCREEN_HEIGHT)
        self.width = 100
        self.height = 60

    def move_direct(self, player_location):
        #The method for chasing down the player when they are close
        if player_location.x > self.rect.x:
            self.rect.x += self.speed
        elif player_location.x < self.rect.x:
            self.rect.x -= self.speed
        if player_location.y > self.rect.y:
            self.rect.y += self.speed
        elif player_location.y < self.rect.y:
            self.rect.y -= self.speed
    
    def random_smooth(self, player_location):
        #this method is a simple way to make good looking random movement
        #the cops choose a random spot on the board and then move there
        #they don't choose random movements for every move - that's very jittery

        #The reason for the following long if statement is the following:
            #The cop has a certain speed.
            #That speed corresponds to a number of 
            #pixels that the cop will travel when it 
            #moves. If it is close to the point it needs to be but not exact, 
            #the speed might not be able to get it there. 
            #Therefore, 5 - which is always more than the cops speed - helps approximate. 
        if (self.rect.x+5 > self.move_to_x and self.rect.x-5 < self.move_to_x) and (self.rect.y+5 > self.move_to_y and self.rect.y-5 < self.move_to_y):
            self.move_to_x = random.randint(0, self.SCREEN_WIDTH - self.width)
            self.move_to_y = random.randint(0, self.SCREEN_HEIGHT - self.height)
        
        radius = 250 #if the player is in this radius the cop switches modes to following them
        if (self.rect.x-radius <player_location.x and self.rect.x+radius >player_location.x) and (self.rect.y-radius <player_location.y and self.rect.y+radius >player_location.y):
            self.move_direct(player_location)
            self.image = self.image_chasing #we want the image to be the chasing image
            return
        
        self.image = self.image_default #resetting here for after one call of the overall method

        if not (self.rect.x+self.speed > self.move_to_x and self.rect.x-self.speed < self.move_to_x): #stops the cops from jittering around when the speed takes it back and forth above and below
            if self.move_to_x > self.rect.x:
                self.rect.x += self.speed
            elif self.move_to_x < self.rect.x:
                self.rect.x -= self.speed
        if not (self.rect.y+self.speed > self.move_to_y and self.rect.y-self.speed < self.move_to_y): #Same as above^^^
            if self.move_to_y > self.rect.y:
                self.rect.y += self.speed
            elif self.move_to_y < self.rect.y:
                self.rect.y -= self.speed
    
    def move_randomly(self, player_location):

        #This was my first attempt at a function for random movement. It does not work well and is 
        #not used anywhere in my code. I just left it around to show more of the path I took to come to my 
        #eventual decision on how to randomize

        if random.randint(1,3) != 1: #the (1,3) this is basically just saying that 2/3 of the time the cop will preference moving in the direction of the player. Not great logic here. Hence why its not used. 
            if player_location.x > self.rect.x:
                self.rect.x += self.speed
            elif player_location.x < self.rect.x:
                self.rect.x -= self.speed
            if player_location.y > self.rect.y:
                self.rect.y += self.speed
            elif player_location.y < self.rect.y:
                self.rect.y -= self.speed
        else:
            if player_location.x > self.rect.x:
                self.rect.y += self.speed
            elif player_location.x < self.rect.x:
                self.rect.y -= self.speed
            if player_location.y > self.rect.y:
                self.rect.x += self.speed
            elif player_location.y < self.rect.y:
                self.rect.x -= self.speed
        self.rect.y = max(0, min(self.rect.y, self.SCREEN_HEIGHT - self.rect.height))
        self.rect.x = max(0, min(self.rect.x, self.SCREEN_WIDTH - self.rect.width))