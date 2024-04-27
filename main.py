
import pygame, sys
from button import Button
from pygame.sprite import Group 
from pygame.sprite import Sprite
from logo import Logo
from config import *
from bullet import Bullet
from aim import Aim
from target import Target
from gun import Gun
from enum import Enum

class Scene(Enum):
    MAIN_MENU = 0
    GAME = 1
    PAUSE = 2
    RESULT = 3

class Game(Sprite):
    def __init__(self):
        pygame.init()  
        pygame.mixer.init() 
        pygame.display.set_caption("DuckHunt")
        pygame.display.set_icon(pygame.image.load("assets/UI/DuckHuntLogo.png"))
        self.SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.scene = Scene.MAIN_MENU
        self.SCORE = 0
        self.CLOCK = pygame.time.Clock()
        self.GUN = Gun(6)
        self.AIM = Aim()
        self.PLAYER_GROUP = Group()
        self.TARGETS = Group()
        self.SUMMON_DUCK = pygame.USEREVENT + 1
        self.TIMER_EVENT = pygame.USEREVENT + 2
        self.time_from_start = 0
        self.game_started_at = 0
        self.time_left = 60
        self.PLAYER_GROUP.add([self.AIM, self.GUN])
        self.INGAME_COUNTDOWN = 60
        self.FONT = pygame.font.Font("assets/Fonts/minecraft.ttf", 48)
        # MAIN MENU region
        self.GAME_BACKGROUND = pygame.image.load("assets/backgrounds/lake.jpeg")
        self.MAIN_MENU_BACKGROUND = pygame.transform.scale(pygame.image.load("assets/backgrounds/main_menu.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.BUTTON_IMAGE = pygame.transform.scale2x(pygame.image.load("assets/UI/Button.png"))
        self.LOGO = Logo()
        self.PLAY_BUTTON = Button(image=self.BUTTON_IMAGE, pos=(SCREEN_WIDTH//2, int(SCREEN_HEIGHT * 0.5)) , 
                                  text_input="ИГРАТЬ",
                                  font=self.FONT,
                                  base_color="White",
                                  hovering_color="Yellow")
        self.OPTIONS_BUTTON = Button(image=self.BUTTON_IMAGE, 
                                pos=(SCREEN_WIDTH//2 , int(SCREEN_HEIGHT * 0.7)) , 
                                    text_input="ОПЦИИ",
                                    font=self.FONT,
                                    base_color="White",
                                    hovering_color="Yellow")
        self.QUIT_BUTTON = Button(image = self.BUTTON_IMAGE, 
                            pos = (SCREEN_WIDTH//2, int(SCREEN_HEIGHT * 0.9)) , 
                            text_input="ВЫХОД",
                            font=self.FONT,
                            base_color="White",
                            hovering_color="Yellow")
        self.MAIN_MENU_BUTTONS = [self.PLAY_BUTTON, self.OPTIONS_BUTTON, self.QUIT_BUTTON]
        self.MAIN_MENU_GROUPE = [self.LOGO, self.PLAY_BUTTON, self.OPTIONS_BUTTON, self.QUIT_BUTTON]
        # MAIN MENU region
        # RESULT region
        RESULT_TO_MAIN_MENU_BUTTON = Button(image=self.BUTTON_IMAGE, pos=(SCREEN_WIDTH//2, int(SCREEN_HEIGHT * 0.6)) , 
                                    text_input="ГЛАВНАЯ",
                                    font=self.FONT,
                                    base_color="White",
                                    hovering_color="Yellow")
        RESULT_QUIT_BUTTON = Button(image=self.BUTTON_IMAGE, 
                                pos=(SCREEN_WIDTH//2, int(SCREEN_HEIGHT * 0.8)) , 
                                    text_input="ВЫХОД",
                                    font=self.FONT,
                                    base_color="White",
                                    hovering_color="Yellow")
        
        self.RESULT_BUTTONS = [RESULT_TO_MAIN_MENU_BUTTON, RESULT_QUIT_BUTTON]
        pygame.time.set_timer(self.SUMMON_DUCK,1500)
        # RESULT region

    def update(self) -> None:
        # main menu apdate
        if self.scene == Scene.MAIN_MENU:
            self.SCREEN.blit(self.MAIN_MENU_BACKGROUND, (0,0))        
            logo = Logo()
            logo.draw(self.SCREEN)

            for button in self.MAIN_MENU_BUTTONS:
                button.changeColor(self.MOUSE_POS)
                button.update(self.SCREEN)
        # game scene update
        if self.scene == Scene.GAME:
            self.SCREEN.blit(self.GAME_BACKGROUND, (0,0))
            score_image = self.FONT.render(f"Счёт: {self.SCORE}", True, (0, 0, 0))
            score_rect = score_image.get_rect()
            self.SCREEN.blit(score_image, (10,10),score_rect)
            time_image = self.FONT.render(f"{self.time_left:02d}", True, (0, 0, 0))
            time_rect = time_image.get_rect()
            self.SCREEN.blit(time_image, (SCREEN_WIDTH-80,30), time_rect) 
            self.PLAYER_GROUP.draw(self.SCREEN)
            self.AIM.handle_keys()
            self.AIM.update()
            self.GUN.update()
            self.GUN.ammo.update()
            self.draw_magazin()
            self.TARGETS.update()
            self.TARGETS.draw(self.SCREEN)


        if self.scene == Scene.RESULT:
            self.SCREEN.blit(self.MAIN_MENU_BACKGROUND, (0,0))
            result_image = self.FONT.render(f"Ваш результат: {self.SCORE}", True, (0, 0, 0))
            result_rect = result_image.get_rect()
            self.SCREEN.blit(result_image, (SCREEN_WIDTH//2, int(SCREEN_HEIGHT * 0.6)), result_rect)
            for button in self.RESULT_BUTTONS:
                button.changeColor(self.MOUSE_POS)
                button.update(self.SCREEN)

    def summon_duck(self):
        duck = Target()
        self.TARGETS.add(duck)

    def draw_magazin(self):
        for i in range(0, self.GUN.current_bullets_count):
            self.GUN.ammo_list[i].is_ready = True
        for i in range(self.GUN.current_bullets_count, self.GUN.mag_size):
            self.GUN.ammo_list[i].is_ready = False

        self.GUN.ammo.draw(self.SCREEN)

    def EventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.scene == Scene.MAIN_MENU:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.PLAY_BUTTON.checkForInput(self.MOUSE_POS):
                        self.scene = Scene.GAME
                    if self.OPTIONS_BUTTON.checkForInput(self.MOUSE_POS):
                        pass
                    if self.QUIT_BUTTON.checkForInput(self.MOUSE_POS):
                        pygame.quit()
                        sys.exit()
            if self.scene == Scene.GAME:
                if event.type == pygame.KEYDOWN:
                    if event.key in self.GUN.CONTROLS:
                        if event.key == pygame.K_SPACE:
                            if self.GUN.state == 0:
                                sprites = pygame.sprite.spritecollide(self.AIM, self.TARGETS, 0)
                                if len(sprites) == 0 and self.SCORE > 0:
                                    self.SCORE -= 50
                                elif self.GUN.current_bullets_count > 0:
                                    for duck in sprites:
                                        duck.got_shot()
                                        self.SCORE += 100
                                self.GUN.shoot()
                        if event.key == pygame.K_r:
                            if self.GUN.state == 0:
                                self.GUN.reload()  
                if event.type == self.SUMMON_DUCK:
                    self.summon_duck()
                if self.game_started_at == 0:
                    self.game_started_at = pygame.time.get_ticks()
                self.time_left = 60 - (pygame.time.get_ticks() - self.game_started_at) // 1000
                
            if self.scene == Scene.RESULT:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.RESULT_BUTTONS[0].checkForInput(self.MOUSE_POS):
                        self.scene = Scene.MAIN_MENU
                    if self.RESULT_BUTTONS[1].checkForInput(self.MOUSE_POS):
                        pygame.quit()
                        sys.exit()

    def run(self):
        while True:
            self.MOUSE_POS = pygame.mouse.get_pos()
            self.EventHandler()
            self.update()
            pygame.display.update()
            self.CLOCK.tick(60)

Game().run()