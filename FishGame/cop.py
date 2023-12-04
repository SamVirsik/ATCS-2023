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
        #self.x_coord = self.SCREEN_WIDTH*(3/4)
        #self.y_coord = random.randint(1, self.SCREEN_HEIGHT)
        self.rect = self.image.get_rect()
        self.speed = 2
        #self.rect.left = random.randint(25, 100)
        #self.rect.centery = random.randint(0, 500)
        #self.rect.left = 50
        #self.rect.centery = 3*(SCREEN_HEIGHT // 4) #needs to be randomized
        #self.rect.y=random.randint(25, 100)
        #self.rect.x=random.randint(0, 500)
        self.rect.x=x
        self.rect.y=y
        self.move_to_x = random.randint(0, self.SCREEN_WIDTH)
        self.move_to_y = random.randint(0, self.SCREEN_HEIGHT)

    def update(self):
        pass
        #self.rect.x -= random.randint(-10, 10)
        #self.rect.y -= random.randint(-10, 10)
        #self.rect.y = max(0, min(self.rect.y, self.SCREEN_HEIGHT - self.rect.height))
        #self.rect.x = max(0, min(self.rect.x, self.SCREEN_WIDTH - self.rect.width))

    def move_direct(self, player_location):
        if player_location.x > self.rect.x:
            self.rect.x += self.speed
        elif player_location.x < self.rect.x:
            self.rect.x -= self.speed
        if player_location.y > self.rect.y:
            self.rect.y += self.speed
        elif player_location.y < self.rect.y:
            self.rect.y -= self.speed
    
    def random_smooth(self, player_location):
        if (self.rect.x+5 > self.move_to_x and self.rect.x-5 < self.move_to_x) and (self.rect.y+5 > self.move_to_y and self.rect.y-5 < self.move_to_y):
            self.move_to_x = random.randint(0, self.SCREEN_WIDTH)
            self.move_to_y = random.randint(0, self.SCREEN_HEIGHT)
        
        radius = 250
        if (self.rect.x-radius <player_location.x and self.rect.x+radius >player_location.x) and (self.rect.y-radius <player_location.y and self.rect.y+radius >player_location.y):
            self.move_direct(player_location)
            self.image = self.image_chasing
            return
        
        self.image = self.image_default
        if self.move_to_x > self.rect.x:
            self.rect.x += self.speed
        elif self.move_to_x < self.rect.x:
            self.rect.x -= self.speed
        if self.move_to_y > self.rect.y:
            self.rect.y += self.speed
        elif self.move_to_y < self.rect.y:
            self.rect.y -= self.speed
    
    def move_randomly(self, player_location):
        if random.randint(1,3) is not 1:
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