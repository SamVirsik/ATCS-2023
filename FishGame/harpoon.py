import pygame 

class Harpoon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = harpoon_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 7

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > SCREEN_WIDTH:
            self.kill()