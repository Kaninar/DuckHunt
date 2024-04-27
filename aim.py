import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Aim(pygame.sprite.Sprite):
    def __init__(self):
        super(Aim, self).__init__()
        self.image = pygame.image.load("assets/graphics/gun/Aim.png")
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        centerx, centery = self.rect.center

        if key[pygame.K_DOWN]: 
            if centery != SCREEN_HEIGHT:
                distToBottom = SCREEN_HEIGHT - centery
                self.rect.centery += distToBottom if distToBottom < dist else dist
        elif key[pygame.K_UP]:
           if centery != 0:
                self.rect.centery -= centery if centery < dist else dist

        if key[pygame.K_RIGHT]: 
            if centerx != SCREEN_WIDTH:
                distToRight = SCREEN_WIDTH - centerx
                self.rect.centerx += distToRight if distToRight < dist else dist
        elif key[pygame.K_LEFT]:
            if centerx != 0:
                self.rect.centerx -= centerx if centerx < dist else dist