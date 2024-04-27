
import pygame
from random import randint
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.math import Vector2

class Target(pygame.sprite.Sprite):
    def __init__(self, speed = 5) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.is_flying = True
        self.is_alive = True
        self.current_sprite = 0
        self.flying_animation_sprites = [frame for frame in [pygame.image.load(f"assets/graphics/duck/duck_horizon_{i}.png") for i in [1, 2, 3, 2]] for r in range(10)]
        self.got_shot_sprite = pygame.image.load("assets/graphics/duck/got_shot.png")
        self.image = self.flying_animation_sprites[int(self.current_sprite)]
        self.image = pygame.transform.scale_by(self.image, 4)
        
        

        point1 = (0,randint(20 ,SCREEN_HEIGHT-20))
        point2 = (SCREEN_WIDTH,randint(20 ,SCREEN_HEIGHT-20))
        self.direct = randint(1,2)
        points = [point1, point2]
        self.pos = Vector2(points[self.direct-1])    
        self.direction = Vector2(points[2 - self.direct]) - Vector2(self.pos) 
        self.flying_speed = speed
        if self.direct == 2:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(center = self.pos)
        self.flapping_sound = pygame.mixer.Sound("assets/audio/duck_flapping_sound.ogg")

    def update(self):
        if self.is_flying == True:
            self.current_sprite += 1

            if self.current_sprite >= len(self.flying_animation_sprites):
                self.current_sprite = 0

            self.image = self.flying_animation_sprites[int(self.current_sprite)]

            if self.current_sprite == 20 :
                self.flapping_sound.play() 

            if self.direct == 2:
                self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.scale_by(self.image, 4)
            self.rect = self.image.get_rect()

            self.pos += self.direction.normalize() * self.flying_speed    
            self.rect.center = (round(self.pos.x), round(self.pos.y))
            
            if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:  
                self.kill()
            if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
                self.kill()
            
        else:
            self.current_sprite += 2.5
            self.image = pygame.transform.scale_by(self.got_shot_sprite, 4)
            self.rect = self.image.get_rect()
            
            self.pos += self.direction.normalize() * 8    
            self.rect.center = (round(self.pos.x), round(self.pos.y))

    def got_shot(self):
        self.is_alive = False
        self.is_flying = False
        self.current_sprite = 0
        self.direction = Vector2(self.pos.x, SCREEN_HEIGHT) - Vector2(self.pos) 