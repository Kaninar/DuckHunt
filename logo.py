import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Logo(pygame.sprite.Sprite):
    def __init__(self):
        super(Logo, self).__init__()
        self.image = pygame.image.load("assets/UI/DuckHuntLogo.png")
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (SCREEN_WIDTH//2 - self.rect.width//2, int(SCREEN_HEIGHT * 0.05))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
