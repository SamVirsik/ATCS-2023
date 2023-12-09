import pygame

class PlayerBoat(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, person_img):
        super().__init__()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.image = person_img
        self.rect = self.image.get_rect()
        self.speed = 5
        self.rect.left = 50
        self.rect.centery = SCREEN_HEIGHT // 4
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -=self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x +=self.speed
        self.rect.y = max(0, min(self.rect.y, self.SCREEN_HEIGHT - self.rect.height))
        self.rect.x = max(0, min(self.rect.x, self.SCREEN_WIDTH - self.rect.width))