import pygame
from bullet import Bullet
from pygame.sprite import Group
from config import SCREEN_WIDTH, SCREEN_HEIGHT

READY = 0
SHOOT = 1
PUMP = 2
RELOAD = 3


class Gun(pygame.sprite.Sprite):
    def __init__(self, mag_size) -> None:
        super(Gun, self).__init__()
        self.state = READY
        self.mag_size = mag_size
        self.current_bullets_count = mag_size
        self.CONTROLS = [pygame.K_SPACE, pygame.K_r]
        self.is_pumping = False

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
        self.pumping_animation = [frame for frame in self.pumping_animation for r in range(8)]
        #
        #   shot assets load
        #
        self.shot_sound = pygame.mixer.Sound("assets/audio/shot_sound.ogg")

        self.shooting_animation = []
        self.shooting_animation.append(pygame.image.load("assets/graphics/gun/shotgun_shoot/shoot1.png"))
        self.shooting_animation.append(pygame.image.load("assets/graphics/gun/shotgun_shoot/shoot2.png"))
        self.shooting_animation = [frame for frame in self.shooting_animation for r in range(11)]
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
        self.reloading_animation_sprites = [frame for frame in self.reloading_animation_sprites for r in range(6)]

        self.current_sprite = 0

        self.image = pygame.transform.scale_by(self.ready_sprite, 1.5)
        self.rect = self.image.get_rect()
        self.rect.midbottom = [SCREEN_WIDTH//2, SCREEN_HEIGHT]

        self.ammo = Group()
        self.ammo_list = [Bullet(SCREEN_WIDTH - ((i+1)*20 + (i+1)*25), SCREEN_HEIGHT - 80, True) for i in range(self.mag_size)]
        self.ammo.add(self.ammo_list)


    def shoot(self):
        if(self.current_bullets_count == 0):
            self.reload()
        else:
            self.current_bullets_count -= 1
            self.shot_sound.play()
            self.state = SHOOT
            
    def pump(self):
        self.pump_sound.play()
        self.state = PUMP

    def reload(self):
        if self.current_bullets_count == self.mag_size:
            return
        self.current_bullets_count += 1
        self.reload_sound.play()
        self.state = RELOAD

    def update(self):
        if self.state == PUMP:
            self.current_sprite += 1

            if self.current_sprite >= len(self.pumping_animation):
                self.current_sprite = 0
                self.state = READY
                self.image = self.ready_sprite
            else:    
                self.image = self.pumping_animation[int(self.current_sprite)]
            self.image = pygame.transform.scale_by(self.image, 1.5)

        if self.state == SHOOT:
            self.current_sprite += 1

            if self.current_sprite >= len(self.shooting_animation):
                self.current_sprite = 0
                self.state = READY
                self.pump()
            else:
                self.image = self.shooting_animation[int(self.current_sprite)]
            self.image = pygame.transform.scale_by(self.image, 1.5)

        if self.state == RELOAD:
            self.current_sprite += 1

            if self.current_sprite >= len(self.reloading_animation_sprites):
                self.current_sprite = 0
                self.state = READY
                self.image = self.ready_sprite
            else:
                self.image = self.reloading_animation_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale_by(self.image, 1.5)

        self.rect = self.image.get_rect()
        self.rect.midbottom = [SCREEN_WIDTH//2, SCREEN_HEIGHT]    

        self.ammo.update() 