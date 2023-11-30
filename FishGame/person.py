import pygame

class Person(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = person_img
        self.rect = self.image.get_rect()
        self.rect.left = 50
        self.rect.centery = SCREEN_HEIGHT // 4
        self.health = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= 3
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += 3
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

    def shoot(self):
        harpoon = Harpoon(self.rect.right, self.rect.centery)
        all_sprites.add(harpoon)
        harpoons.add(harpoon)