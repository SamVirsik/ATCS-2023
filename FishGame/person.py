import pygame

class Person(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, person_img):
        super().__init__()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.image = person_img
        self.rect = self.image.get_rect()
        self.rect.left = 50
        self.rect.centery = SCREEN_HEIGHT // 4
        self.health = 100

    def update(self):
        #Player can only move up and down, or it would be too easy to select the fish you want to shoot
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= 4
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += 4
        self.rect.y = max(0, min(self.rect.y, self.SCREEN_HEIGHT - self.rect.height))
