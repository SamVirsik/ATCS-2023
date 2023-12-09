import pygame
import time
import random

from playerboat import PlayerBoat
from cop import Cop

class Chase(pygame.sprite.Sprite):
    def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.screen = screen
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.set_up_images()
        self.caught = False
        self.all_sprites = pygame.sprite.Group()
        self.cops = pygame.sprite.Group()
        self.players = pygame.sprite.Group() #helpful for easy checking of collisions (even though there will only ever be one player)

        self.escape_time =15 #The amount of time the player has to avoid cops before it ends
    
    def set_up_images(self):
        self.cop_boat = pygame.image.load("Images/cop boat.png")
        self.red_cop_boat = pygame.image.load("Images/cop boat with red.png")#This is the form of the boat when they are close to the player and are chasing them down
        self.boat = pygame.image.load("Images/boat.png")
        self.background = pygame.image.load("Images/ocean_backround.jpg")

        self.cop_boat = pygame.transform.scale(self.cop_boat, (100, 60))
        self.red_cop_boat = pygame.transform.scale(self.red_cop_boat, (100, 60))
        self.boat = pygame.transform.scale(self.boat, (50, 34))
        self.background = pygame.transform.scale(self.background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def make_cops(self, num):
        for i in range(num):
            x=random.randint(0, self.SCREEN_WIDTH)
            y=self.SCREEN_HEIGHT*3/4
            new_cop = Cop(self.cop_boat, self.red_cop_boat, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, x, y)
            self.all_sprites.add(new_cop)
            self.cops.add(new_cop)

    def run_game(self, num = 4):
        self.player = PlayerBoat(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.boat)
        self.all_sprites.add(self.player)
        self.players.add(self.player)
        self.make_cops(num)

        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        font = pygame.font.Font(None, 50)
        message = font.render("Escape in: " + str(self.escape_time), True, (255, 0, 0))
        self.screen.blit(message, (10, 10))
        pygame.display.flip()
        time.sleep(0.5)

        self.start_time = time.time()

        self.caught == False #needed for returning whether they were caught. The 'running' part of the loop won't have this info for me

        running = True
        while running and time.time() - self.start_time < self.escape_time:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
                    running = False
                    pygame.quit()
            self.all_sprites.update()
            for cop in self.cops:
                cop.random_smooth(self.player.rect) #the random_smooth function is just my nicest function for random movement of the cops
            time.sleep(0.01) 

            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)

            font = pygame.font.Font(None, 50)
            time_elapsed = time.time() - self.start_time
            message = font.render("Escape in: " + str(1+ int(self.escape_time - time_elapsed)), True, (255, 0, 0))
            self.screen.blit(message, (10, 10))
            pygame.display.flip()

            hits = pygame.sprite.groupcollide(self.players, self.cops, True, True)
            if len(hits) >0:
                running = False
                self.caught = True
        return self.caught