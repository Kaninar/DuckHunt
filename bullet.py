import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, is_ready):
        super(Bullet, self).__init__()
        self.is_ready = True
        self.x = pos_x
        self.y = pos_y
        self.ready_sprite = pygame.image.load("assets/graphics/gun/ShotgunShell.png")
        self.blind_sprite = pygame.image.load("assets/graphics/gun/ShotgunShellBlind.png")
        if is_ready:
            self.image = self.ready_sprite
        else:
            self.image = self.blind_sprite
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, speed):
        if self.is_ready:
            self.image = self.ready_sprite
        else:
            self.image = self.blind_sprite
        
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

