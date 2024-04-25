
import pygame, sys
from button import Button
from logo import Logo
from config import *
from bullet import Bullet
from aim import Aim
from target import Target
from score_label import Score
from gun import Gun

from pygame.sprite import Group
from pygame import Surface
from pygame import display as pgdisplay


    

ColorBlack = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)


pygame.init()

screen = pgdisplay.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

clock = pygame.time.Clock()
targets = Group()
all_sprites = Group()
gun = Gun(6)

# def create_ammo():
#     i = 0
#     for i in range (0, gun.current_bullets_count):
#         ammo.add(Bullet(SCREEN_WIDTH - (i*20 + i*25), SCREEN_HEIGHT - 80),True)
#     while i != gun.mag_size:
#         ammo.add(Bullet(SCREEN_WIDTH - (i*20 + i*25), SCREEN_HEIGHT - 80),False)
def play():  

    aim = Aim()
    speed = 5
    target = Target(5)
    score_label = Score()
    targets.add(target)
    running = True
    score = 0
    all_sprites.add(aim)
    all_sprites.add(score_label)
    all_sprites.add(gun)
    all_sprites.add(gun.ammo)
    background = pygame.image.load("assets/backgrounds/lake.jpeg")
    pygame.time.get_ticks() #starter tick
    seconds = 60
    time_font = pygame.font.Font("assets/Fonts/minecraft.ttf", 32)
     # if more than 10 seconds close the game
    while running:

        screen.blit(pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
        seconds = int(60 - pygame.time.get_ticks()/1000)
        time_text = f"{seconds:02d}"
        time_image = time_font.render(time_text, True, (0, 0, 0))
        time_rect = time_image.get_rect()
        screen.blit(time_image, (SCREEN_WIDTH-70, 20), time_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
                if event.key == pygame.K_SPACE:
                    if True not in [gun.is_pumping, gun.is_reloading, gun.is_shooting]:
                        for target in targets: 
                            if pygame.sprite.collide_rect(aim, target) == True:
                                score += 100
                                score_label.score = score
                                score_label.draw(screen)
                                target.got_shot()
                        gun.shoot()
                if event.key == pygame.K_r:
                    if True not in [gun.is_pumping, gun.is_reloading, gun.is_shooting]:
                        gun.reload()    
                    
        

        aim.handle_keys()
        
        speed = 5 + (score/200)*2
        if targets.__len__() == 0:
            targets.add(Target(speed))
        if seconds == 0:
            result(score)
            break
        targets.draw(screen)
        targets.update(0.15)
        all_sprites.draw(screen)
        all_sprites.update(0.15)

        clock.tick(FRAMERATE)
        
        pygame.display.flip()        


def main_menu():
    main_menu_bg = pygame.image.load("assets/backgrounds/main_menu.png")
    main_menu_bg = pygame.transform.scale(main_menu_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    button_image = image=pygame.image.load("assets/UI/Button.png")
    button_image = pygame.transform.scale2x(button_image)

    button_font=pygame.font.Font("assets/Fonts/minecraft.ttf", 46)

    PLAY_BUTTON = Button(image=button_image, pos=(SCREEN_WIDTH//2, int(SCREEN_HEIGHT * 0.5)) , 
                                  text_input="ИГРАТЬ",
                                  font=button_font,
                                  base_color="White",
                                  hovering_color="Yellow")
    OPTIONS_BUTTON = Button(image=button_image, 
                             pos=(SCREEN_WIDTH//2 , int(SCREEN_HEIGHT * 0.7)) , 
                                  text_input="ОПЦИИ",
                                  font=button_font,
                                  base_color="White",
                                  hovering_color="Yellow")
    QUIT_BUTTON = Button(image=button_image, 
                             pos=(SCREEN_WIDTH//2, int(SCREEN_HEIGHT * 0.9)) , 
                                  text_input="ВЫХОД",
                                  font=button_font,
                                  base_color="White",
                                  hovering_color="Yellow")
    
    main_menu_buttons = []
    main_menu_buttons.append(PLAY_BUTTON)
    main_menu_buttons.append(OPTIONS_BUTTON)
    main_menu_buttons.append(QUIT_BUTTON)

    logo = Logo()

    while True:
        screen.blit(main_menu_bg, (0,0))
        
        logo.draw(screen)

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for button in main_menu_buttons:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()

def options():
    pass

def result(score):
    main_menu_bg = pygame.image.load("assets/backgrounds/main_menu.png")
    main_menu_bg = pygame.transform.scale(main_menu_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    button_image = pygame.image.load("assets/UI/Button.png")
    button_image = pygame.transform.scale2x(button_image)

    button_font=pygame.font.Font("assets/Fonts/minecraft.ttf", 46)
    result_font=pygame.font.Font("assets/Fonts/minecraft.ttf", 60)

    TO_MAIN_MENU_BUTTON = Button(image=button_image, pos=(SCREEN_WIDTH//2, int(SCREEN_HEIGHT * 0.6)) , 
                                  text_input="ГЛАВНАЯ",
                                  font=button_font,
                                  base_color="White",
                                  hovering_color="Yellow")
    QUIT_BUTTON = Button(image=button_image, 
                             pos=(SCREEN_WIDTH//2, int(SCREEN_HEIGHT * 0.8)) , 
                                  text_input="ВЫХОД",
                                  font=button_font,
                                  base_color="White",
                                  hovering_color="Yellow")
    
    result_menu_buttons = []
    result_menu_buttons.append(TO_MAIN_MENU_BUTTON)
    result_menu_buttons.append(QUIT_BUTTON)


    while True:
        screen.blit(main_menu_bg, (0,0))

        
        result_text = f"Ваш результат: {score}"
        result_image = result_font.render(result_text, True, (0, 0, 0))
        result_rect = result_image.get_rect()
        screen.blit(result_image, (SCREEN_WIDTH//2 - result_rect.width//2, int(SCREEN_HEIGHT * 0.05)), result_rect)

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for button in result_menu_buttons:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TO_MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()

main_menu()