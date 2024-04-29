import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Logo(pygame.sprite.Sprite):
    def __init__(self):
        super(Logo, self).__init__()
        self.animation = [frame for frame in [pygame.image.load(f"assets/UI/DuckHuntLogo({i}).png") for i in range(1, 6)] for r in range(14) ]
        self.image = pygame.transform.scale2x(self.animation[0])
        self.current_sprite = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (SCREEN_WIDTH//2 - self.rect.width//2, int(SCREEN_HEIGHT * 0.05))

    def draw(self, screen):
        self.rect = self.image.get_rect()
        self.rect.topleft = (SCREEN_WIDTH//2 - self.rect.width//2, int(SCREEN_HEIGHT * 0.05))
        screen.blit(self.image, self.rect)

    def update(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.animation):
            self.current_sprite = 0
        self.image = pygame.transform.scale2x(self.animation[self.current_sprite])