import pygame
from bullet import Bullet
from pygame.sprite import Group
from config import SCREEN_WIDTH, SCREEN_HEIGHT


class Gun(pygame.sprite.Sprite):
    def __init__(self, mag_size) -> None:
        super(Gun, self).__init__()

        self.mag_size = mag_size
        self.current_bullets_count = mag_size

        self.is_pumping = False
        self.is_shooting = False
        self.is_reloading = False

        self.ready_sprite = pygame.image.load("assets/graphics/gun/shotgun_ready.png")
        #
        #   pump assets load
        #
        self.pump_sound = pygame.mixer.Sound("assets/audio/pump_sound2.ogg")

        self.pumping_animation = []
        self.pumping_animation.append(pygame.image.load("assets/graphics/gun/shotgun_pump/pump1.png"))
        self.pumping_animation.append(pygame.image.load("assets/graphics/gun/shotgun_pump/pump2.png"))
        self.pumping_animation.append(pygame.image.load("assets/graphics/gun/shotgun_pump/pump3.png"))
        self.pumping_animation.append(pygame.image.load("assets/graphics/gun/shotgun_pump/pump4.png"))
        self.pumping_animation.append(pygame.image.load("assets/graphics/gun/shotgun_pump/pump5.png"))
        self.pumping_animation.append(pygame.image.load("assets/graphics/gun/shotgun_pump/pump6.png"))
        #
        #   shot assets load
        #
        self.shot_sound = pygame.mixer.Sound("assets/audio/shot_sound.ogg")

        self.shooting_animation = []
        self.shooting_animation.append(pygame.image.load("assets/graphics/gun/shotgun_shoot/shoot1.png"))
        self.shooting_animation.append(pygame.image.load("assets/graphics/gun/shotgun_shoot/shoot2.png"))
        #
        #   reload assets load
        #
        self.reload_sound = pygame.mixer.Sound("assets/audio/reload_sound.ogg")

        self.reloading_animation_sprites = []
        self.reloading_animation_sprites.append(pygame.image.load("assets/graphics/gun/shotgun_reload/shotgun_reload_1.png"))
        self.reloading_animation_sprites.append(pygame.image.load("assets/graphics/gun/shotgun_reload/shotgun_reload_2.png"))
        self.reloading_animation_sprites.append(pygame.image.load("assets/graphics/gun/shotgun_reload/shotgun_reload_3.png"))
        self.reloading_animation_sprites.append(pygame.image.load("assets/graphics/gun/shotgun_reload/shotgun_reload_4.png"))
        self.reloading_animation_sprites.append(pygame.image.load("assets/graphics/gun/shotgun_reload/shotgun_reload_5.png"))
        self.reloading_animation_sprites.append(pygame.image.load("assets/graphics/gun/shotgun_reload/shotgun_reload_6.png"))
        self.reloading_animation_sprites.append(pygame.image.load("assets/graphics/gun/shotgun_reload/shotgun_reload_7.png"))
        self.reloading_animation_sprites.append(pygame.image.load("assets/graphics/gun/shotgun_reload/shotgun_reload_8.png"))
        self.reloading_animation_sprites.append(pygame.image.load("assets/graphics/gun/shotgun_reload/shotgun_reload_9.png"))

        self.current_sprite = 0

        self.image = pygame.transform.scale_by(self.ready_sprite, 1.5)
        self.rect = self.image.get_rect()
        self.rect.midbottom = [SCREEN_WIDTH//2, SCREEN_HEIGHT]

        self.ammo_list = []
        self.ammo = Group()
        for i in range (0, self.mag_size+1):
            self.ammo_list.append(Bullet(SCREEN_WIDTH - (i*20 + i*25), SCREEN_HEIGHT - 80, True))
        self.ammo.add(self.ammo_list)


    def shoot(self):
        if(self.current_bullets_count == 0):
            self.reload()
        else:
            self.current_bullets_count -= 1
            self.shot_sound.play()
            self.is_shooting = True
            
    def pump(self):
        self.pump_sound.play()
        self.is_pumping = True

    def reload(self):
        if self.current_bullets_count == self.mag_size:
            return
        self.current_bullets_count += 1
        self.reload_sound.play()
        self.is_reloading = True

    def update(self, speed):
        if self.is_pumping == True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.pumping_animation):
                self.current_sprite = 0
                self.is_pumping = False
                self.image = self.ready_sprite
            else:    
                self.image = self.pumping_animation[int(self.current_sprite)]
            self.image = pygame.transform.scale_by(self.image, 1.5)

        if self.is_shooting == True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.shooting_animation):
                self.current_sprite = 0
                self.is_shooting = False
                self.pump()
            else:
                self.image = self.shooting_animation[int(self.current_sprite)]
            self.image = pygame.transform.scale_by(self.image, 1.5)

        if self.is_reloading == True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.reloading_animation_sprites):
                self.current_sprite = 0
                self.is_reloading = False
                self.image = self.ready_sprite
            else:
                self.image = self.reloading_animation_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale_by(self.image, 1.5)

        self.rect = self.image.get_rect()
        self.rect.midbottom = [SCREEN_WIDTH//2, SCREEN_HEIGHT]

        for i in range(0, self.current_bullets_count):
            self.ammo_list[self.current_bullets_count].is_ready = True
        for i in range(self.current_bullets_count, self.mag_size):
            self.ammo_list[self.current_bullets_count+1].is_ready = False
        
        # for b in self.ammo_list:
        #     b.update(0)
            
    

