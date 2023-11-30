import pygame

class Fish(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.image = fish_info[type][0]
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 100)
        self.speed = fish_info[type][1]
        self.health = 50
        self.has_collided = False  # Flag to track collision

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

    def get_type(self):
        return self.type