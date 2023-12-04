import pygame 

class Harpoon(pygame.sprite.Sprite):
    def __init__(self, x, y, harpoon_img, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.image = harpoon_img
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 7

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > self.SCREEN_WIDTH:
            self.kill()