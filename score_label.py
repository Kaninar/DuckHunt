import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Score, self).__init__()
        self.font = pygame.font.Font("assets/Fonts/minecraft.ttf", 32)
        self.score = 0
        self.text = f"Score: {self.score}"
        self.image = self.font.render(self.text, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        

    def draw(self, surface):
        self.text = f"Score: {self.score}"
        self.render()
        surface.blit(self.image, self.rect)

    def render(self):
        self.image = self.font.render(self.text, True, (0, 0, 0))
        self.rect = self.image.get_rect()

        