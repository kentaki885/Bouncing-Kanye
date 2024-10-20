import math
from random import randint

import pygame
import random
from os.path import join
import json

#sprite
class Scores_class():
    def __init__(self):
        #main menu
        self.start_once = True
        self.reset_menu = False
        self.settings_menu = False
        self.mute_sfx = content['mute_sfx']
        self.mute_music = content['mute_music']

        self.screen_width_c = content["screen_width"]
        self.screen_height_c = content["screen_hight"]

        self.high_score = content['high_score']
        self.hikill_count = content['kill_count']
        self.death_count = content['death_count']

        self.money = content['money']
        self.money_multiplier = content['money_multiplier']

        self.boss_alive = False
        self.n = 1

        self.spawntext = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(60 * width_scale))
        self.spawntext_surf = self.spawntext.render(f"[START]", True, (240, 240, 240))
        self.spawntext_rect = self.spawntext_surf.get_frect(center=(screen_width/2, screen_height/2 + (235*hight_scale)))

        self.respawntext = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(60 * width_scale))
        self.respawntext_surf = self.respawntext.render(f"[RESTART]", True, (240, 240, 240))
        self.respawntext_rect = self.respawntext_surf.get_frect(center=(screen_width/2, screen_height/2 + (225*hight_scale)))

        self.quittext = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(40 * width_scale))
        self.quittext_surf = self.quittext.render(f"[QUIT GAME]", True, (160,60,225))
        self.quittext_rect = self.quittext_surf.get_frect(center=(screen_width/2 , screen_height/2 + (325*hight_scale)))

        self.mainmenutext = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(40 * width_scale))
        self.mainmenutext_surf = self.mainmenutext.render(f"[MAIN MENU]", True, (160,60,225))
        self.mainmenutext_rect = self.mainmenutext_surf.get_frect(center=(screen_width/2 , screen_height/2 + (325*hight_scale)))
class Shop():
    def __init__(self):
        #speed
        self.level_speed = content['level_speed']
        self.price_speed = content['price_speed']
        self.speed = content['speed']
        self.dash = content['dash']
        self.unlock_dash = content['unlock_dash']

        self.upgradetext_speed = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(35 * width_scale))
        self.upgradetext_surf_speed = self.upgradetext_speed.render(f"SPEED", True, (255, 220, 220))
        self.upgradetext_rect_speed = self.upgradetext_surf_speed.get_frect(topleft=(0, screen_height / 2 - (250*hight_scale)))

        self.leveltext_speed = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        self.leveltext_surf_speed = self.leveltext_speed.render(f"Level: {self.level_speed}", True, (240, 240, 240))
        self.leveltext_rect_speed = self.leveltext_surf_speed.get_frect(topleft=(0, screen_height/2 - 200))

        self.buttontext_speed = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        self.buttontext_surf_speed = self.buttontext_speed.render(f"Price: {self.price_speed}", True, (240, 240, 240))
        self.buttontext_rect_speed = self.buttontext_surf_speed.get_frect(topleft=
                                                                          (100, screen_height/2 - 125))
        self.button_border_speed = pygame.draw.rect(screen, (255, 223, 0), self.buttontext_rect_speed.inflate(30, 25).move(0, -7),
                                         border_radius=15)

        #controls speed
        self.controlstext_speed = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        self.controlstext_surf_speed = self.controlstext_speed.render(f"L-SHIFT to dash!", True, (255, 255, 255))
        self.controlstext_rect_speed = self.controlstext_surf_speed.get_frect(topleft=((128*width_scale), screen_height / 2 - (235*hight_scale)))

        #laserspeed
        self.level_laser_speed = content['level_laser_speed']
        self.price_laser_speed = content['price_laser_speed']
        self.laser_speed = content['laser_speed']
        self.double_laser = content['double_laser']
        self.unlock_double_laser = content['unlock_double_laser']

        self.upgradetext_lasergun = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(35 * width_scale))
        self.upgradetext_surf_lasergun = self.upgradetext_lasergun.render(f"LASER SPEED", True, (200,220,255))
        self.upgradetext_rect_lasergun = self.upgradetext_surf_lasergun.get_frect(
            topleft=(0, screen_height / 2 - (100*hight_scale)))
        self.leveltext_lasergun = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        self.leveltext_surf_lasergun = self.leveltext_lasergun.render(f"Level: {self.level_laser_speed}", True,
                                                                      (240, 240, 240))
        self.leveltext_rect_lasergun = self.leveltext_surf_lasergun.get_frect(
            topleft=(screen_width / 2 - 225, screen_height / 2 - 200))

        self.buttontext_lasergun = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        self.buttontext_surf_lasergun = self.buttontext_lasergun.render(f"Price: {self.price_laser_speed}", True,
                                                                        (240, 240, 240))
        self.buttontext_rect_lasergun = self.buttontext_surf_lasergun.get_frect(
            topleft=(screen_width / 2 - 225, screen_height / 2 - 125))
        self.button_border_lasergun = pygame.draw.rect(screen, (255, 223, 0),
                                            self.buttontext_rect_lasergun.inflate(30, 25).move(0, -7),border_radius=15)
        #reload
        self.level_reload = content['level_reload']
        self.price_reload = content['price_reload']
        self.reload = content['reload']
        self.fullauto = content['fullauto']
        self.unlock_fullauto = content['unlock_fullauto']

        self.upgradetext_reload = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(35 * width_scale))
        self.upgradetext_surf_reload = self.upgradetext_reload.render(f"FIRERATE", True, (255,200,150))
        self.upgradetext_rect_reload = self.upgradetext_surf_reload.get_frect(
            topleft=(0, screen_height / 2 + (50*hight_scale)))

        self.leveltext_reload = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        self.leveltext_surf_reload = self.leveltext_reload.render(f"Level: {self.level_reload}", True,
                                                                      (240, 240, 240))
        self.leveltext_rect_reload = self.leveltext_surf_reload.get_frect(
            topleft=(screen_width / 2+50 , screen_height / 2 - 200))

        self.buttontext_reload = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        self.buttontext_surf_reload = self.buttontext_lasergun.render(f"Price: {self.price_reload}", True,
                                                                        (240, 240, 240))
        self.buttontext_rect_reload = self.buttontext_surf_reload.get_frect(topleft=
                                                                            (screen_width/2 , screen_height / 2+50 - 125))
        self.button_border_reload = pygame.draw.rect(screen, (255, 223, 0),
                                            self.buttontext_rect_reload.inflate(30, 25).move(0, -7),border_radius=15)

        #money multiplaier

        self.level_money = content['level_money']
        self.price_money = content['price_money']

        self.upgradetext_money = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(35 * width_scale))
        self.upgradetext_surf_money = self.upgradetext_money.render(f"MONEY MULTIPLIER", True, (200,255,200))
        self.upgradetext_rect_money = self.upgradetext_surf_money.get_frect(
            topleft=(0, screen_height / 2 + (200*hight_scale)))

        self.leveltext_money = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        self.leveltext_surf_money = self.leveltext_money.render(f"Level: {self.level_money}", True,
                                                                      (240, 240, 240))
        self.leveltext_rect_money = self.leveltext_surf_money.get_frect(
            topleft=(screen_width / 2 + 400 , screen_height / 2 - 200))

        self.buttontext_money = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        self.buttontext_surf_money= self.buttontext_money.render(f"Price: {self.price_money}", True,
                                                                        (240, 240, 240))
        self.buttontext_rect_money = self.buttontext_surf_money.get_frect(topleft=
                                                                          (screen_width/2 + 400 , screen_height / 2 - 125))
        self.button_border_money = pygame.draw.rect(screen, (255, 223, 0),
                                            self.buttontext_rect_money.inflate(30, 25).move(0, -7),border_radius=15)

        #skin1
        self.unlocked_1 = content['unlocked_1']
        self.price_skin1 = content['price_skin1']
        self.equipped_1 = content['equipped_1']
        self.upgradetext_skin1 = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(35 * width_scale))
        self.upgradetext_surf_skin1 = self.upgradetext_skin1.render(f"KANYE", True, (100,200,255))
        self.upgradetext_rect_skin1 = self.upgradetext_surf_skin1.get_frect(topright=(screen_width, screen_height / 2 - (250*hight_scale)))

        self.statue1_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        self.statue1_text_surf = self.statue1_text.render(f"LOCKED", True,
                                                                      (240, 240, 240))
        self.statue1_text_rect = self.statue1_text_surf.get_frect(
            topright=(screen_width - (7*width_scale), screen_height / 2 - (225*hight_scale)))

        self.buttontext_skin1 = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        self.buttontext_surf_skin1 = self.buttontext_skin1.render(f"{self.price_skin1}", True, (240, 240, 240))
        self.buttontext_rect_skin1 = self.buttontext_surf_skin1.get_frect(topright=
                                                                          (100, screen_height/2 - 125))
        self.button_border_skin1 = pygame.draw.rect(screen, (255, 223, 0), self.buttontext_rect_skin1.inflate(30, 25).move(0, -7),
                                         border_radius=15)

        #skin2
        self.unlocked_2 = content['unlocked_2']
        self.price_skin2 = content['price_skin2']
        self.equipped_2 = content['equipped_2']

        self.upgradetext_skin2 = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(35 * width_scale))
        self.upgradetext_surf_skin2 = self.upgradetext_skin2.render(f"SUIT YE", True, (255,165,0))
        self.upgradetext_rect_skin2 = self.upgradetext_surf_skin2.get_frect(topright=(screen_width, screen_height / 2 - (100*hight_scale)))

        self.statue2_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        self.statue2_text_surf = self.statue2_text.render(f"LOCKED", True,
                                                                      (240, 240, 240))
        self.statue2_text_rect = self.statue2_text_surf.get_frect(
            topright=(screen_width - 7, screen_height / 2 - 225))

        self.buttontext_skin2 = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        self.buttontext_surf_skin2 = self.buttontext_skin2.render(f"{self.price_skin2}", True, (240, 240, 240))
        self.buttontext_rect_skin2 = self.buttontext_surf_skin2.get_frect(topright=
                                                                          (100, screen_height/2 - 125))
        self.button_border_skin2 = pygame.draw.rect(screen, (255, 223, 0), self.buttontext_rect_skin2.inflate(30, 25).move(0, -7),
                                         border_radius=15)

        #skin3
        self.unlocked_3 = content['unlocked_3']
        self.price_skin3 = content['price_skin3']
        self.equipped_3 = content['equipped_3']

        self.upgradetext_skin3 = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(35 * width_scale))
        self.upgradetext_surf_skin3 = self.upgradetext_skin3.render(f"MILLIONAIR-YE", True, (140,255,150))
        self.upgradetext_rect_skin3 = self.upgradetext_surf_skin3.get_frect(topright=(screen_width, screen_height / 2 + int(50*hight_scale)))

        self.statue3_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        self.statue3_text_surf = self.statue3_text.render(f"LOCKED", True,
                                                                      (240, 240, 240))
        self.statue3_text_rect = self.statue3_text_surf.get_frect(
            topright=(screen_width - 7, screen_height / 2 - 225))

        self.buttontext_skin3 = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        self.buttontext_surf_skin3 = self.buttontext_skin3.render(f"{self.price_skin3}", True, (240, 240, 240))
        self.buttontext_rect_skin3 = self.buttontext_surf_skin3.get_frect(topright=
                                                                          (100, screen_height/2 - 125))
        self.button_border_skin3 = pygame.draw.rect(screen, (255, 223, 0), self.buttontext_rect_skin3.inflate(30, 25).move(0, -7),
                                         border_radius=15)

        #skin4
        self.unlocked_4 = content['unlocked_4']
        self.price_skin4 = content['price_skin4']
        self.equipped_4 = content['equipped_4']

        self.upgradetext_skin4 = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(35 * width_scale))
        self.upgradetext_surf_skin4 = self.upgradetext_skin4.render(f"?????", True, (255,245,120))
        self.upgradetext_rect_skin4 = self.upgradetext_surf_skin4.get_frect(topright=(screen_width, screen_height / 2 + (200*hight_scale)))

        self.statue4_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        self.statue4_text_surf = self.statue4_text.render(f"LOCKED", True,
                                                                      (240, 240, 240))
        self.statue4_text_rect = self.statue4_text_surf.get_frect(
            topright=(screen_width - 7, screen_height / 2 - 225))

        self.buttontext_skin4 = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        self.buttontext_surf_skin4 = self.buttontext_skin4.render(f"{self.price_skin4}", True, (240, 240, 240))
        self.buttontext_rect_skin4 = self.buttontext_surf_skin4.get_frect(topright=
                                                                          (100, screen_height/2 - 125))
        self.button_border_skin4 = pygame.draw.rect(screen, (255, 223, 0), self.buttontext_rect_skin4.inflate(30, 25).move(0, -7),
                                         border_radius=15)
    def update(self):
        ##speeed
        if ((self.button_border_speed.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0] and
                scores.money >= self.price_speed and player.alive == False and not scores.start_once) and
                ((self.level_speed < 5))):
            pygame.mixer.Sound.play(fweah_sound)
            scores.money -= self.price_speed
            self.level_speed += 1
            self.price_speed = self.price_speed * self.level_speed * 4
        elif ((self.button_border_speed.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
               and player.alive == False and not scores.start_once) and
                ((self.unlock_dash ) and (not self.dash))):
            pygame.mixer.Sound.play(fweah_sound)
            self.double_laser = False
            self.fullauto = False

            self.dash = True
        elif ((self.button_border_speed.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
                   and not player.alive and not scores.start_once) and ((((not self.dash) and (self.double_laser or self.fullauto))
                   or (((scores.money < self.price_speed) and (not self.unlock_dash)) or (self.dash))))):
            pygame.mixer.Sound.play(wrong_sound)

        #update text speed
        self.leveltext_surf_speed = self.leveltext_speed.render(f"Level: {self.level_speed}", True, (255, 255, 255))
        if self.level_speed < 5:
            self.buttontext_surf_speed = self.buttontext_speed.render(f"{self.price_speed}$", True, (51, 44, 0))
        elif ((self.unlock_dash) and (not self.dash)):
            self.buttontext_surf_speed = self.buttontext_speed.render(f"EQUIP", True, (51, 44, 0))
        elif((self.dash)):
            self.buttontext_surf_speed = self.buttontext_speed.render(f"EQUIPPED", True, (200,200,200))

        #cases speed
        match self.level_speed:
            case 0:
                self.speed = 500
            case 1:
                self.speed = 550
            case 2:
                self.speed = 575
            case 3:
                self.speed = 600
            case 4:
                self.speed = 625
            case 5:
                self.speed = 650
                self.unlock_dash = True

        ##lasergun
        if ((self.button_border_lasergun.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0] and
                scores.money >= self.price_laser_speed and not player.alive and not scores.start_once) and
                ((self.level_laser_speed < 5))):
            pygame.mixer.Sound.play(fweah_sound)
            scores.money -= self.price_laser_speed
            self.level_laser_speed += 1
            self.price_laser_speed = self.price_laser_speed * self.level_laser_speed * 4
        elif ((self.button_border_lasergun.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
               and not player.alive and not scores.start_once) and
                ((self.unlock_double_laser) and (not self.double_laser))):
            pygame.mixer.Sound.play(fweah_sound)
            self.dash = False
            self.fullauto = False

            self.double_laser = True
        elif ((self.button_border_lasergun.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
               and not player.alive and not scores.start_once) and ((((not self.double_laser) and (self.dash or self.fullauto))
              or (((scores.money < self.price_laser_speed) and (not self.unlock_dash)) or (self.double_laser))))):
            pygame.mixer.Sound.play(wrong_sound)

        #update text lasergun
        self.leveltext_surf_lasergun = self.leveltext_lasergun.render(f"Level: {self.level_laser_speed}", True, (255, 255, 255))
        if self.level_laser_speed < 5:
            self.buttontext_surf_lasergun = self.buttontext_lasergun.render(f"{self.price_laser_speed}$", True, (51, 44, 0))
        elif ((self.unlock_double_laser) and (not self.double_laser)):
            self.buttontext_surf_lasergun = self.buttontext_lasergun.render(f"EQUIP", True, (51, 44, 0))
        elif ((self.double_laser)):
            self.buttontext_surf_lasergun = self.buttontext_lasergun.render(f"EQUIPPED", True, (200,200,200))


        #cases lasergun
        match self.level_laser_speed:
            case 0:
                self.laser_speed = 400
            case 1:
                self.laser_speed = 450
            case 2:
                self.laser_speed = 500
            case 3:
                self.laser_speed = 600
            case 4:
                self.laser_speed = 650
            case 5:
                self.laser_speed = 700
                self.unlock_double_laser = True
        ##reloaddddd
        #level up/click
        if ((self.button_border_reload.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0] and
                scores.money >= self.price_reload  and not player.alive and not scores.start_once) and
                 ((self.level_reload < 5))):
            pygame.mixer.Sound.play(fweah_sound)
            scores.money -= self.price_reload
            self.level_reload += 1
            self.price_reload = self.price_reload * self.level_reload * 4
        elif ((self.button_border_reload.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
               and not player.alive and not scores.start_once) and
                 ((self.unlock_fullauto) and (not self.fullauto))):
            pygame.mixer.Sound.play(fweah_sound)
            self.double_laser = False
            self.dash = False

            self.fullauto = True
        elif ((self.button_border_reload.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
               and not player.alive and not scores.start_once) and ((((not self.fullauto) and (self.dash or self.double_laser))
              or (((scores.money < self.price_reload) and (not self.unlock_fullauto)) or (self.fullauto))))):
            pygame.mixer.Sound.play(wrong_sound)
        # update text reload
        self.leveltext_surf_reload = self.leveltext_reload.render(f"Level: {self.level_reload}", True,
                                                                      (255, 255, 255))
        if self.level_reload < 5:
            self.buttontext_surf_reload = self.buttontext_reload.render(f"{self.price_reload}$", True,
                                                                            (51, 44, 0))
        elif ((self.unlock_fullauto) and (not self.fullauto)):
            self.buttontext_surf_reload = self.buttontext_reload.render(f"EQUIP", True, (51, 44, 0))
        elif ((self.fullauto)):
            self.buttontext_surf_reload = self.buttontext_reload.render(f"EQUIPPED", True, (200, 200, 200))

        # cases reload
        match self.level_reload:
            case 0:
                self.reload = 500
            case 1:
                self.reload = 475
            case 2:
                self.reload = 450
            case 3:
                self.reload = 425
            case 4:
                self.reload = 400
            case 5:
                self.reload = 350
                self.unlock_fullauto = True

            ##moneyyyyy
            # level up/click
        if ((self.button_border_money.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0] and
             scores.money >= self.price_money and not player.alive and not scores.start_once) and
                ((self.level_money < 5))):
            pygame.mixer.Sound.play(fweah_sound)
            scores.money -= self.price_money
            self.level_money += 1
            self.price_money= int(self.price_money * self.level_money * 2.5)
        elif ((self.button_border_money.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
               and not player.alive and not scores.start_once) and
              ((scores.money < self.price_money) or (self.level_money == 5))):
            pygame.mixer.Sound.play(wrong_sound)
            # update text reload
        self.leveltext_surf_money = self.leveltext_money.render(f"Level: {self.level_money}", True,
                                                                  (255, 255, 255))
        if self.level_money < 5:
            self.buttontext_surf_money = self.buttontext_money.render(f"{self.price_money}$", True,
                                                                        (51, 44, 0))
        elif self.level_money == 5:
            self.buttontext_surf_money = self.buttontext_money.render(f"MAXED", True, (200, 200, 200))
            # cases money
        match self.level_money:
            case 0:
                scores.money_multiplier = 1
            case 1:
                scores.money_multiplier = 2
            case 2:
                scores.money_multiplier = 4
            case 3:
                scores.money_multiplier = 8
            case 4:
                scores.money_multiplier = 16
            case 5:
                scores.money_multiplier = 24


        ##skin1
        if ((self.button_border_skin1.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0] and
                scores.money >= self.price_skin1 and not player.alive and not scores.start_once) and
                ((not self.unlocked_1))):
            pygame.mixer.Sound.play(fweah_sound)
            scores.money -= self.price_skin1
            self.unlocked_1 = True
        elif ((self.button_border_skin1.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
               and not player.alive and not scores.start_once) and
                ((self.unlocked_1) and (not self.equipped_1))):
            pygame.mixer.Sound.play(fweah_sound)
            self.equipped_2 = False
            self.equipped_3 = False
            self.equipped_4 = False

            self.equipped_1 = True
        elif ((self.button_border_skin1.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
                   and not player.alive and not scores.start_once) and
                (((scores.money < self.price_skin1) and (not self.unlocked_1)) or (self.equipped_1))):
            pygame.mixer.Sound.play(wrong_sound)
        #LOCKED
        if not self.unlocked_1:
            self.statue1_text_surf = self.statue1_text.render(f"LOCKED", True,(240, 240, 240))
        if self.unlocked_1:
            self.statue1_text_surf = self.statue1_text.render(f"UNLOCKED", True,(240, 240, 240))

        if self.equipped_1 and not player.image == skin_kanye:
            player.image = skin_kanye
            player.rect = player.image.get_frect(center=(screen_width / 2, screen_height / 2))
        #update text skin1
        if not self.unlocked_1:
            self.buttontext_surf_skin1 = self.buttontext_skin1.render(f"{self.price_skin1}$", True, (51, 44, 0))
        elif self.unlocked_1 and not self.equipped_1:
            self.buttontext_surf_skin1 = self.buttontext_skin1.render(f"EQUIP", True, (51, 44, 0))
        elif self.unlocked_1 and self.equipped_1:
            self.buttontext_surf_skin1 = self.buttontext_skin1.render(f"EQUIPPED", True, (200,200,200))

        ##skin2
        if ((self.button_border_skin2.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0] and
                scores.money >= self.price_skin2 and not player.alive and not scores.start_once) and
                ((not self.unlocked_2))):
            pygame.mixer.Sound.play(fweah_sound)
            scores.money -= self.price_skin2
            self.unlocked_2 = True
        elif ((self.button_border_skin2.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
               and not player.alive and not scores.start_once) and
                ((self.unlocked_2) and (not self.equipped_2))):
            pygame.mixer.Sound.play(fweah_sound)
            self.equipped_1 = False
            self.equipped_3 = False
            self.equipped_4 = False

            self.equipped_2 = True
        elif ((self.button_border_skin2.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
                   and not player.alive and not scores.start_once) and
                (((scores.money < self.price_skin2) and (not self.unlocked_2)) or (self.equipped_2))):
            pygame.mixer.Sound.play(wrong_sound)

        #update text skin2
        if not self.unlocked_2:
            self.buttontext_surf_skin2 = self.buttontext_skin2.render(f"{self.price_skin2}$", True, (51, 44, 0))
        elif self.unlocked_2 and not self.equipped_2:
            self.buttontext_surf_skin2 = self.buttontext_skin2.render(f"EQUIP", True, (51, 44, 0))
        elif self.unlocked_2 and self.equipped_2:
            self.buttontext_surf_skin2 = self.buttontext_skin2.render(f"EQUIPPED", True, (200,200,200))

        #LOCKED
        if not self.unlocked_2:
            self.statue2_text_surf = self.statue2_text.render(f"LOCKED", True,(240, 240, 240))
        if self.unlocked_2:
            self.statue2_text_surf = self.statue2_text.render(f"UNLOCKED", True,(240, 240, 240))


        if self.equipped_2 and not player.image == player_surf:
            player.image = player_surf
            player.rect = player.image.get_frect(center=(screen_width / 2, screen_height / 2))

        ##skin3
        if ((self.button_border_skin3.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0] and
                scores.money >= self.price_skin3 and not player.alive and not scores.start_once) and
                ((not self.unlocked_3))):
            pygame.mixer.Sound.play(fweah_sound)
            scores.money -= self.price_skin3
            self.unlocked_3 = True
        elif ((self.button_border_skin3.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
               and not player.alive and not scores.start_once) and
                ((self.unlocked_3) and (not self.equipped_3))):
            pygame.mixer.Sound.play(fweah_sound)
            self.equipped_1 = False
            self.equipped_2 = False
            self.equipped_4 = False

            self.equipped_3 = True
        elif ((self.button_border_skin3.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
                   and not player.alive and not scores.start_once) and
                (((scores.money < self.price_skin3) and (not self.unlocked_3)) or (self.equipped_3))):
            pygame.mixer.Sound.play(wrong_sound)

        #update text skin3
        if not self.unlocked_3:
            self.buttontext_surf_skin3 = self.buttontext_skin3.render(f"{self.price_skin3}$", True, (51, 44, 0))
        elif self.unlocked_3 and not self.equipped_3:
            self.buttontext_surf_skin3 = self.buttontext_skin3.render(f"EQUIP", True, (51, 44, 0))
        elif self.unlocked_3 and self.equipped_3:
            self.buttontext_surf_skin3 = self.buttontext_skin3.render(f"EQUIPPED", True, (200,200,200))


        #LOCKED
        if not self.unlocked_3:
            self.statue3_text_surf = self.statue3_text.render(f"LOCKED", True,(240, 240, 240))
        if self.unlocked_3:
            self.statue3_text_surf = self.statue3_text.render(f"UNLOCKED", True,(240, 240, 240))


        if self.equipped_3 and not player.image == skin_cool_ye:
            player.image = skin_cool_ye
            player.rect = player.image.get_frect(center=(screen_width / 2, screen_height / 2))

        ##skin4
        if ((self.button_border_skin4.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0] and
             scores.money >= self.price_skin4 and not player.alive and not scores.start_once) and
                ((not self.unlocked_4))):
            pygame.mixer.Sound.play(fweah_sound)
            scores.money -= self.price_skin4
            self.unlocked_4 = True
        elif ((self.button_border_skin4.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
               and not player.alive and not scores.start_once) and
              ((self.unlocked_4) and (not self.equipped_4))):
            pygame.mixer.Sound.play(fweah_sound)
            self.equipped_1 = False
            self.equipped_2 = False
            self.equipped_3 = False

            self.equipped_4 = True
        elif ((self.button_border_skin4.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]
               and not player.alive and not scores.start_once) and
              (((scores.money < self.price_skin4) and (not self.unlocked_4)) or (self.equipped_4))):
            pygame.mixer.Sound.play(wrong_sound)

        # update text skin4
        if not self.unlocked_4:
            self.buttontext_surf_skin4 = self.buttontext_skin4.render(f"{self.price_skin4}$", True, (51, 44, 0))
        elif self.unlocked_4 and not self.equipped_4:
            self.buttontext_surf_skin4 = self.buttontext_skin4.render(f"EQUIP", True, (51, 44, 0))
        elif self.unlocked_4 and self.equipped_4:
            self.buttontext_surf_skin4 = self.buttontext_skin4.render(f"EQUIPPED", True, (200, 200, 200))

        #locked
        if not self.unlocked_4:
            self.statue4_text_surf = self.statue4_text.render(f"LOCKED", True,(240, 240, 240))
        if self.unlocked_4:
            self.statue4_text_surf = self.statue4_text.render(f"UNLOCKED", True,(240, 240, 240))


        if self.equipped_4 and not player.image == skin_lebron:
            player.image = skin_lebron
            player.rect = player.image.get_frect(center=(screen_width / 2, screen_height / 2))
    def draw(self):
        if not player.alive and not scores.start_once:

            ##speed
            #update rect pos before drawing
            self.leveltext_rect_speed = self.leveltext_surf_speed.get_frect(
                topleft=((7*width_scale), screen_height / 2 - (210*hight_scale)))
            self.buttontext_rect_speed = self.buttontext_surf_speed.get_frect(
                topleft=((140*width_scale), screen_height / 2 - (190*hight_scale)))
            #draw
            screen.blit(self.upgradetext_surf_speed, self.upgradetext_rect_speed)
            screen.blit(self.leveltext_surf_speed, self.leveltext_rect_speed)
            if not self.dash:
                self.button_border_speed = pygame.draw.rect(screen, (255,223,0), self.buttontext_rect_speed.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            if (self.dash):
                self.button_border_speed = pygame.draw.rect(screen, (44, 44, 44), self.buttontext_rect_speed.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
                screen.blit(self.controlstext_surf_speed, self.controlstext_rect_speed)
            screen.blit(self.buttontext_surf_speed, self.buttontext_rect_speed)
            #button hover
            if (self.button_border_speed.collidepoint((mouse_x,mouse_y))) and ((self.level_speed <5)):
                self.buttontext_surf_speed = self.buttontext_speed.render(f"{self.price_speed}$", True, (51, 44, 0))
                self.button_border_speed = pygame.draw.rect(screen, (255, 238, 128),
                                                 self.buttontext_rect_speed.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_speed, self.buttontext_rect_speed)
            if (self.button_border_speed.collidepoint((mouse_x,mouse_y))) and ((self.unlock_dash) and (not self.dash)):
                self.buttontext_surf_speed = self.buttontext_speed.render(f"EQUIP", True, (51, 44, 0))
                self.button_border_speed = pygame.draw.rect(screen, (255, 238, 128),
                                                 self.buttontext_rect_speed.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_speed, self.buttontext_rect_speed)


            ##lasergun
            #update rect pos before drawing
            self.leveltext_rect_lasergun = self.leveltext_surf_lasergun.get_frect(
                topleft=((7*width_scale), screen_height / 2 - (60*hight_scale)))
            self.buttontext_rect_lasergun = self.buttontext_surf_lasergun.get_frect(
                topleft=((140*width_scale), screen_height / 2 - (40*hight_scale)))
            #draw
            screen.blit(self.upgradetext_surf_lasergun, self.upgradetext_rect_lasergun)
            screen.blit(self.leveltext_surf_lasergun, self.leveltext_rect_lasergun)
            if not self.double_laser:
                self.button_border_lasergun = pygame.draw.rect(screen, (255,223,0), self.buttontext_rect_lasergun.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            if (self.double_laser):
                self.button_border_lasergun = pygame.draw.rect(screen, (44, 44, 44), self.buttontext_rect_lasergun.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            screen.blit(self.buttontext_surf_lasergun, self.buttontext_rect_lasergun)
            #button hover
            if (self.button_border_lasergun.collidepoint((mouse_x,mouse_y))) and ((self.level_laser_speed <5)):
                self.buttontext_surf_lasergun = self.buttontext_lasergun.render(f"{self.price_laser_speed}$", True, (51, 44, 0))
                self.button_border_lasergun = pygame.draw.rect(screen, (255, 238, 128),
                                                 self.buttontext_rect_lasergun.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_lasergun, self.buttontext_rect_lasergun)

            if (self.button_border_lasergun.collidepoint((mouse_x,mouse_y))) and ((self.unlock_double_laser) and (not self.double_laser)):
                self.buttontext_surf_lasergun = self.buttontext_lasergun.render(f"EQUIP", True, (51, 44, 0))
                self.button_border_lasergun = pygame.draw.rect(screen, (255, 238, 128),
                                                 self.buttontext_rect_lasergun.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_lasergun, self.buttontext_rect_lasergun)
            ##reloaddddddd
            #update rect pos before drawing
            self.leveltext_rect_reload = self.leveltext_surf_reload.get_frect(
                topleft=((7*width_scale), screen_height / 2 + (90*hight_scale)))
            self.buttontext_rect_reload = self.buttontext_surf_reload.get_frect(
                topleft=((140*width_scale), screen_height / 2 + (110*hight_scale)))
            #draw
            screen.blit(self.upgradetext_surf_reload, self.upgradetext_rect_reload)
            screen.blit(self.leveltext_surf_reload, self.leveltext_rect_reload)
            if not self.fullauto:
                self.button_border_reload = pygame.draw.rect(screen, (255,223,0), self.buttontext_rect_reload.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            if (self.fullauto):
                self.button_border_reload = pygame.draw.rect(screen, (44, 44, 44), self.buttontext_rect_reload.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            screen.blit(self.buttontext_surf_reload, self.buttontext_rect_reload)
            #button hover
            if (self.button_border_reload.collidepoint((mouse_x,mouse_y))) and ((self.level_reload <5)):
                self.buttontext_surf_reload = self.buttontext_reload.render(f"{self.price_reload}$", True, (51, 44, 0))
                self.button_border_reload = pygame.draw.rect(screen, (255, 238, 128),
                                                 self.buttontext_rect_reload.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
                screen.blit(self.buttontext_surf_reload, self.buttontext_rect_reload)
            if (self.button_border_reload.collidepoint((mouse_x,mouse_y))) and ((self.unlock_fullauto) and (not self.fullauto)):
                self.buttontext_surf_reload = self.buttontext_reload.render(f"EQUIP", True, (51, 44, 0))
                self.button_border_reload = pygame.draw.rect(screen, (255, 238, 128),
                                                 self.buttontext_rect_reload.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_reload, self.buttontext_rect_reload)


            ##moneyyyyy
            #update rect pos before drawing
            self.leveltext_rect_money = self.leveltext_surf_money.get_frect(
                topleft=((7*width_scale), screen_height / 2 + (240*hight_scale)))
            self.buttontext_rect_money = self.buttontext_surf_money.get_frect(
                topleft=((140*width_scale), screen_height / 2 + (260*hight_scale)))
            #draw
            screen.blit(self.upgradetext_surf_money, self.upgradetext_rect_money)
            screen.blit(self.leveltext_surf_money, self.leveltext_rect_money)
            if self.level_money <5:
                self.button_border_money = pygame.draw.rect(screen, (255,223,0), self.buttontext_rect_money.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            if (self.level_money == 5):
                self.button_border_money = pygame.draw.rect(screen, (44, 44, 44), self.buttontext_rect_money.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            screen.blit(self.buttontext_surf_money, self.buttontext_rect_money)
            #button hover
            if (self.button_border_money.collidepoint((mouse_x,mouse_y))) and (self.level_money <5):
                self.buttontext_surf_money = self.buttontext_money.render(f"{self.price_money}$", True, (51, 44, 0))
                self.button_border_money = pygame.draw.rect(screen, (255, 238, 128),
                                                 self.buttontext_rect_money.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_money, self.buttontext_rect_money)

            ##skin1
            # update rect pos before drawing
            self.buttontext_rect_skin1 = self.buttontext_surf_skin1.get_frect(
                topright=(screen_width - (140*width_scale), screen_height / 2 - (190*hight_scale)))
            # draw
            screen.blit(self.upgradetext_surf_skin1, self.upgradetext_rect_skin1)

            self.statue1_text_rect = self.statue1_text_surf.get_frect(topright=(screen_width - (7*width_scale), screen_height / 2 - (210*hight_scale)))
            screen.blit(self.statue1_text_surf, self.statue1_text_rect)
            if not self.unlocked_1:
                self.button_border_skin1 = pygame.draw.rect(screen, (255, 223, 0),
                                                            self.buttontext_rect_skin1.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            if (self.unlocked_1) and (self.equipped_1):
                self.button_border_skin1 = pygame.draw.rect(screen, (44, 44, 44),
                                                            self.buttontext_rect_skin1.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            if (self.unlocked_1) and (not self.equipped_1):
                self.button_border_skin1 = pygame.draw.rect(screen, (255, 223, 0),
                                                            self.buttontext_rect_skin1.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            screen.blit(self.buttontext_surf_skin1, self.buttontext_rect_skin1)
            # button hover
            if (self.button_border_skin1.collidepoint((mouse_x,mouse_y))) and ((not self.unlocked_1)):
                self.buttontext_surf_skin1 = self.buttontext_skin1.render(f"{self.price_skin1}$", True, (51, 44, 0))
                self.button_border_skin1 = pygame.draw.rect(screen, (255, 238, 128),
                                                            self.buttontext_rect_skin1.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_skin1, self.buttontext_rect_skin1)
            if (self.button_border_skin1.collidepoint((mouse_x,mouse_y))) and ((self.unlocked_1 and not self.equipped_1)):
                self.buttontext_surf_skin1 = self.buttontext_skin1.render(f"EQUIP", True, (51, 44, 0))
                self.button_border_skin1 = pygame.draw.rect(screen, (255, 238, 128),
                                                            self.buttontext_rect_skin1.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_skin1, self.buttontext_rect_skin1)

            ##skin2
            # update rect pos before drawing
            self.buttontext_rect_skin2 = self.buttontext_surf_skin2.get_frect(
                topright=(screen_width - (140*width_scale), screen_height / 2 - (40*hight_scale)))
            # draw
            screen.blit(self.upgradetext_surf_skin2, self.upgradetext_rect_skin2)

            self.statue2_text_rect = self.statue2_text_surf.get_frect(topright=(screen_width - (7*width_scale), screen_height / 2 - (60*hight_scale)))
            screen.blit(self.statue2_text_surf, self.statue2_text_rect)
            if not self.unlocked_2:
                self.button_border_skin2 = pygame.draw.rect(screen, (255, 223, 0),
                                                            self.buttontext_rect_skin2.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            if (self.unlocked_2) and (self.equipped_2):
                self.button_border_skin2 = pygame.draw.rect(screen, (44, 44, 44),
                                                            self.buttontext_rect_skin2.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            if (self.unlocked_2) and (not self.equipped_2):
                self.button_border_skin2 = pygame.draw.rect(screen, (255, 223, 0),
                                                            self.buttontext_rect_skin2.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            screen.blit(self.buttontext_surf_skin2, self.buttontext_rect_skin2)
            # button hover
            if (self.button_border_skin2.collidepoint((mouse_x,mouse_y))) and ((not self.unlocked_2)):
                self.buttontext_surf_skin2 = self.buttontext_skin2.render(f"{self.price_skin2}$", True, (51, 44, 0))
                self.button_border_skin2 = pygame.draw.rect(screen, (255, 238, 128),
                                                            self.buttontext_rect_skin2.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_skin2, self.buttontext_rect_skin2)
            if (self.button_border_skin2.collidepoint((mouse_x,mouse_y))) and ((self.unlocked_2 and not self.equipped_2)):
                self.buttontext_surf_skin2 = self.buttontext_skin2.render(f"EQUIP", True, (51, 44, 0))
                self.button_border_skin2 = pygame.draw.rect(screen, (255, 238, 128),
                                                            self.buttontext_rect_skin2.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_skin2, self.buttontext_rect_skin2)


            ##skin3
            # update rect pos before drawing
            self.buttontext_rect_skin3 = self.buttontext_surf_skin3.get_frect(
                topright=(screen_width - (140*width_scale), screen_height / 2 + (110*hight_scale)))
            # draw
            screen.blit(self.upgradetext_surf_skin3, self.upgradetext_rect_skin3)

            self.statue3_text_rect = self.statue3_text_surf.get_frect(topright=(screen_width - (7*width_scale), screen_height / 2 + (90*hight_scale)))
            screen.blit(self.statue3_text_surf, self.statue3_text_rect)
            if not self.unlocked_3:
                self.button_border_skin3 = pygame.draw.rect(screen, (255, 223, 0),
                                                            self.buttontext_rect_skin3.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            if (self.unlocked_3) and (self.equipped_3):
                self.button_border_skin3 = pygame.draw.rect(screen, (44, 44, 44),
                                                            self.buttontext_rect_skin3.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            if (self.unlocked_3) and (not self.equipped_3):
                self.button_border_skin3 = pygame.draw.rect(screen, (255, 223, 0),
                                                            self.buttontext_rect_skin3.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            screen.blit(self.buttontext_surf_skin3, self.buttontext_rect_skin3)
            # button hover
            if (self.button_border_skin3.collidepoint((mouse_x,mouse_y))) and ((not self.unlocked_3)):
                self.buttontext_surf_skin3 = self.buttontext_skin3.render(f"{self.price_skin3}$", True, (51, 44, 0))
                self.button_border_skin3 = pygame.draw.rect(screen, (255, 238, 128),
                                                            self.buttontext_rect_skin3.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_skin3, self.buttontext_rect_skin3)
            if (self.button_border_skin3.collidepoint((mouse_x,mouse_y))) and ((self.unlocked_3 and not self.equipped_3)):
                self.buttontext_surf_skin3 = self.buttontext_skin3.render(f"EQUIP", True, (51, 44, 0))
                self.button_border_skin3 = pygame.draw.rect(screen, (255, 238, 128),
                                                            self.buttontext_rect_skin3.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_skin3, self.buttontext_rect_skin3)


            ##skin4
            # update rect pos before drawing
            self.buttontext_rect_skin4 = self.buttontext_surf_skin4.get_frect(
                topright=(screen_width - (140*width_scale), screen_height / 2 + (260*hight_scale)))
            # draw
            screen.blit(self.upgradetext_surf_skin4, self.upgradetext_rect_skin4)

            self.statue4_text_rect = self.statue4_text_surf.get_frect(topright=(screen_width - (7*width_scale), screen_height / 2 + (240*hight_scale)))
            screen.blit(self.statue4_text_surf, self.statue4_text_rect)

            if not self.unlocked_4:
                self.button_border_skin4 = pygame.draw.rect(screen, (255, 223, 0),
                                                            self.buttontext_rect_skin4.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            if (self.unlocked_4) and (self.equipped_4):
                self.button_border_skin4 = pygame.draw.rect(screen, (44, 44, 44),
                                                            self.buttontext_rect_skin4.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            if (self.unlocked_4) and (not self.equipped_4):
                self.button_border_skin4 = pygame.draw.rect(screen, (255, 223, 0),
                                                            self.buttontext_rect_skin4.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(15*width_scale))
            screen.blit(self.buttontext_surf_skin4, self.buttontext_rect_skin4)
            # button hover
            if (self.button_border_skin4.collidepoint((mouse_x,mouse_y))) and ((not self.unlocked_4)):
                self.buttontext_surf_skin4 = self.buttontext_skin4.render(f"{self.price_skin4}$", True, (51, 44, 0))
                self.button_border_skin4 = pygame.draw.rect(screen, (255, 238, 128),
                                                            self.buttontext_rect_skin4.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
                screen.blit(self.buttontext_surf_skin4, self.buttontext_rect_skin4)
            if (self.button_border_skin4.collidepoint((mouse_x,mouse_y))) and ((self.unlocked_4 and not self.equipped_4)):
                self.buttontext_surf_skin4 = self.buttontext_skin4.render(f"EQUIP", True, (51, 44, 0))
                self.button_border_skin4 = pygame.draw.rect(screen, (255, 238, 128),
                                                            self.buttontext_rect_skin4.inflate((30*width_scale), (25*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10  *width_scale))
                screen.blit(self.buttontext_surf_skin4, self.buttontext_rect_skin4)
class Coins(pygame.sprite.Sprite):
    def __init__(self,groups, surf, pos, posy, value):
        super().__init__(groups)

        self.image = surf
        self.posy = posy
        self.rect = self.image.get_frect(center = pos)

        self.value = value
        self.direction = pygame.math.Vector2((random.choice([-0.3,0.3])),(-0.5))
        self.speed = (600*speed_scale)

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt

        #wall clipping
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0

        #movement
        if self.rect.top <= self.posy - (110*hight_scale) or self.rect.top == 0 :
            self.direction.y *= -1
            self.direction.x *= 1
            self.speed = 750 * speed_scale
        if self.rect.right >= screen_width:
            self.direction.x *= -1
        if self.rect.left <= 0:
            self.direction.x *= -1
        if self.rect.top >= screen_height:
            self.kill()
class Diamond(pygame.sprite.Sprite):
    def __init__(self,groups, surf, pos,posy, value):
        super().__init__(groups)

        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.posy = posy

        self.value = value

        self.direction = pygame.math.Vector2((random.choice([-0.3,0.3])),(-0.5))
        self.speed = (600*speed_scale)

        #timer
        self.last_time = pygame.time.get_ticks()
        self.cooldown_time = 12000
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        self.destroy_diamond()
        #wall clipping
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

        #movement
        if self.rect.top <= self.posy - (110*hight_scale) or self.rect.top == 0 :
            self.direction.y *= -1
            self.direction.x *= 1
            self.speed = 750 * speed_scale
        if self.rect.top >= self.posy + (50 * hight_scale) or self.rect.top == 0:
            self.direction.x = 0
            self.direction.y = 0

        if self.rect.right >= screen_width:
            self.direction.x *= -1
        if self.rect.left <= 0:
            self.direction.x *= -1
    #timeout
    def destroy_diamond(self):
        if pygame.time.get_ticks() - self.last_time >= self.cooldown_time:
            self.kill()
            self.last_time = pygame.time.get_ticks()
        if not player.alive:
            self.kill()
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = skin_kanye
        self.rect = self.image.get_frect(center=(screen_width/2 , screen_height/2))
        self.direction = pygame.math.Vector2(0, 0)
        #upgradable speed
        self.speed = shop.speed *speed_scale

        self.alive = True
        self.kill_count = 0
        self.kill_count_adder = 1
        self.kill_money_adder = 5
        self.can_shoot = False
        self.last_shot = 0
        #reload speed
        if not shop.fullauto:
            self.cooldown_time = shop.reload
        elif shop.fullauto:
            self.cooldown_time = 150
        #dash
        self.can_dash = False
        self.last_dash = 0
        self.cooldown_time_dash = 50

        self.current_score_og = 0
        self.current_score = self.current_score_og

        #mask
        self.mask = pygame.mask.from_surface(self.image)

    def laser_time(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot >= self.cooldown_time:
                self.can_shoot = True
    def dash_time(self):
        if not self.can_dash:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_dash >= self.cooldown_time_dash:
                self.can_dash = True

    def update(self, dt):
        #key pressed
        if player.alive:
            if scores.start_once:
                scores.start_once = False
            if not scores.boss_alive:
                self.current_score += 10 * dt
        if player.alive:
            keys_pressed = pygame.key.get_pressed()
            keys_justPressed = pygame.key.get_just_pressed()
            player.direction.x = int(keys_pressed[pygame.K_d]) or int(keys_pressed[pygame.K_RIGHT]) - int(keys_pressed[pygame.K_a]) or - int(keys_pressed[pygame.K_LEFT])
            player.direction.y = int(keys_pressed[pygame.K_s]) or int(keys_pressed[pygame.K_DOWN]) - int(keys_pressed[pygame.K_w]) or -int(keys_pressed[pygame.K_UP])
            if (keys_pressed[pygame.K_SPACE] and self.can_shoot and shop.fullauto) or (pygame.mouse.get_pressed()[0] == True and self.can_shoot and shop.fullauto):
                laser = Laser(laser_surf, player.rect.midtop, (all_sprites, laser_group))
                pygame.mixer.Sound.play(laser_sound)
                self.can_shoot = False
                self.last_shot = pygame.time.get_ticks()
            elif (keys_justPressed[pygame.K_SPACE] and self.can_shoot and not shop.fullauto) or (pygame.mouse.get_just_pressed()[0] == True and self.can_shoot and not shop.fullauto):
                if not shop.double_laser:
                    laser = Laser(laser_surf, player.rect.midtop, (all_sprites, laser_group))
                    pygame.mixer.Sound.play(laser_sound)
                if shop.double_laser:
                    laser = Laser(laser_surf, player.rect.midtop, (all_sprites, laser_group))
                    laser = Laser(laser_surf, (player.rect.centerx - (15*width_scale), player.rect.top), (all_sprites, laser_group))
                    laser = Laser(laser_surf, (player.rect.centerx + (15*width_scale), player.rect.top), (all_sprites, laser_group))
                    pygame.mixer.Sound.play(shotgun_sound)
                self.can_shoot = False
                self.last_shot = pygame.time.get_ticks()
            if keys_justPressed[pygame.K_LSHIFT] and self.can_dash and shop.dash:
                player.rect.center += player.direction * 4000 * dt * speed_scale
                self.can_dash = False
                self.last_dash = pygame.time.get_ticks()
        if player.direction:
            player.direction = player.direction.normalize()
        else:
            player.direction = player.direction
        # movement
        player.rect.center += player.direction * player.speed * dt
        #collisions
        #-wall passing
        if player.rect.right > screen_width:
            player.rect.right = screen_width
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.bottom > screen_height:
            player.rect.bottom = screen_height
        if player.rect.top < 0:
            player.rect.top = -5*hight_scale
        #=wall collisions
        if player.rect.right >= screen_width or player.rect.left <= 0:
            player.direction.x = 0
        if player.rect.bottom >= screen_height or player.rect.top <= 0:
            player.direction.y = 0
        self.laser_time()
        self.dash_time()
class Star(pygame.sprite.Sprite):
    def __init__(self, groups,pos,surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom= pos)
    def update(self, dt):
        if player.alive:
            x = min((25 + player.current_score/100), 200) * speed_scale
            self.rect.top += x *dt
        if self.rect.top > screen_height:
            self.kill()
            x = random.uniform(0.01, 0.04)
            star_surf = pygame.image.load(join('Data', 'white-star.png')).convert_alpha()
            star_surf = pygame.transform.scale(star_surf, (int(star_surf.get_width() * x * width_scale),
                                                           int(star_surf.get_height() * x * hight_scale)))
            Star(star_group, ((random.randint(0, screen_width)), (-20*hight_scale)), star_surf)
class Laser(pygame.sprite.Sprite):
    def __init__(self,surf,pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
        self.speed = (shop.laser_speed* speed_scale)

        if shop.double_laser:
            self.image = pygame.transform.invert(self.image)
    def update(self, dt):
        self.rect.centery -= self.speed * dt
        if self.rect.bottom <0:
            self.kill()
class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.kim_original = pygame.image.load(join('Data', 'crying-kim-kardashian-valentina-hramov-transparent-2.png')).convert_alpha()
        self.kim_original = pygame.transform.smoothscale(self.kim_original, (int(self.kim_original.get_width()*width_scale),
                                                               int(self.kim_original.get_height()*hight_scale)))
        #self.image = random.choice([self.swift_original, self.kim_original])
        self.image = self.kim_original
        self.rect = self.image.get_frect(center= ((random.randint(0, screen_width)), ((random.randint(-300, -200)*hight_scale))))

        self.speed = (random.randint(300,400)*speed_scale)
        self.direction = pygame.math.Vector2((random.uniform(-0.5, 0.5)),(1))
        self.last_time = pygame.time.get_ticks()
        self.cooldown_time = 5500

        self.size = randint(0,10)
        self.rotation_angle = 0
        self.rotation_speed = (random.choice([(randint(1,100)),(randint(1,100)),(randint(1,100)),
                                              (randint(1,100)),(randint(1,100)),(200)]))
        self.jumpy = randint(1,3)
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        self.destroy_meteor()

        # transform
        self.rotation_angle +=  self.rotation_speed * dt

        self.image = pygame.transform.rotozoom(self.kim_original, self.rotation_angle, 1)
        if self.size == 1:
            self.image = pygame.transform.scale2x(self.image)
        elif self.size == 2:
            self.image = pygame.transform.scale2x(self.kim_original)
        if self.jumpy != 1:
            self.rect = self.image.get_frect(center=self.rect.center)

    def destroy_meteor(self):
        if pygame.time.get_ticks() - self.last_time >= self.cooldown_time:
            self.kill()
            self.last_time = pygame.time.get_ticks()
class EvilYe(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('Data', 'evil_ye.png')).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (int(self.image.get_width()*0.85*width_scale),
                                                               int(self.image.get_height()*0.85*hight_scale)))
        self.rect = self.image.get_frect(center= ((random.choice([0, screen_width])), -(300*hight_scale)))
        self.direction = pygame.math.Vector2((random.choice([0.6, -0.6])), 1)
        if self.direction.x == (0.6):
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_frect(center= ((0), (random.randint(-300, -200)*hight_scale)))
        if self.direction.x == (-0.6):
            self.rect = self.image.get_frect(center=((screen_width), (random.randint(-300, -200)*hight_scale)))
        self.speed = (350*speed_scale)
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        self.destroy_ye()

    def destroy_ye(self):
        if self.rect.top > screen_height:
            self.kill()
            pygame.mixer.Sound.stop(ye_spawn)
class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('Data', 'taylor.png')).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (int(self.image.get_width()*width_scale),
                                                               int(self.image.get_height()*hight_scale)))
        self.rect = self.image.get_frect(center = ((screen_width/2), (-30*hight_scale)))

        self.direction = pygame.math.Vector2(0,1)
        self.speed = (random.randint(175, 200)*speed_scale)
        self.once = 0

        self.once_2 = 0
        self.can_shoot = False
        self.last_shot = 0
        self.cooldown_time = 1250

    def laser_time(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot >= self.cooldown_time:
                self.can_shoot = True
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        #vertical spawn
        if self.rect.bottom >= (150*hight_scale) and self.once != 1:
            self.speed = (random.randint(325, 350)*speed_scale)
            self.direction.x = random.choice([-1,1])
            self.direction.y = 0
            self.once = 1
        #collisions
        if self.rect.right > screen_width + (50*width_scale):
            self.rect.right = screen_width + (50*width_scale)
        if self.rect.left < (-50*width_scale):
            self.rect.left = (-50*width_scale)
        if self.rect.right >= screen_width + (50*width_scale):
            self.direction.x *= -1
        if self.rect.left <= (-50*width_scale):
            self.direction.x *= -1


        #attack
        if self.can_shoot:
            ship_laser = ShipLaser(self.rect.midbottom, (all_sprites,ship_laser_group))
            pygame.mixer.Sound.play(laser_sound)
            self.can_shoot = False
            self.last_shot = pygame.time.get_ticks()
        self.laser_time()
class ShipLaser(pygame.sprite.Sprite):
    def __init__(self,pos, groups):
        super().__init__(groups)
        self.image = laser_surf
        self.image = pygame.transform.flip(self.image, flip_x=False, flip_y=True)
        self.image = pygame.transform.invert(self.image)
        self.rect = self.image.get_frect(midtop = pos)

    def update(self, dt):
        self.rect.centery += (500*speed_scale) * dt
        if self.rect.top > screen_height:
            self.kill()
class Boss(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image_original = diddy1_surf
        self.image = self.image_original
        self.rect = self.image.get_frect(center = ((screen_width/2), (-400*hight_scale)))

        self.direction = pygame.math.Vector2(0,1)
        self.speed = (200*speed_scale)

        self.can_shoot = False
        self.last_shot = 0
        self.cooldown_time = 1000

        self.health = min(40 +(scores.n * 10), 100)
        self.max_health = min(40 +(scores.n * 10), 100)
        # min(40 +(scores.n * 10), 100)

        #spawn phase
        self.spawn = True

        #phase oil
        self.shoot_starter = False
        self.shoot_phase = False
        self.shoot_counter = 0

        #phase bouncing
        self.bouncing_starter = False
        self.bouncing_phase = False
        self.bouncing_counter = 0

        #phase laser beam
        self.laserbeam_starter = False
        self.laserbeam_phase = False
        self.laserbeam_return = False

    def laser_time(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot >= self.cooldown_time:
                self.can_shoot = True
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        #vertical spawn
        if self.rect.bottom >= (325*hight_scale) and self.spawn:
            self.rect.bottom = (325*hight_scale)
            self.direction.y = 0
            self.spawn = False
            # choose phase
            self.phase_chooser = random.choice([1,2,3])
            if self.phase_chooser == 1:
                self.shoot_starter = True
                self.shoot_phase = True
            elif self.phase_chooser == 2:
                self.bouncing_phase = True
                self.bouncing_starter = True
            elif self.phase_chooser == 3:
                self.laserbeam_phase = True
                self.laserbeam_starter = True

        #collisions
        #wall clipping
        if self.rect.right > screen_width +(75*width_scale):
            self.rect.right = screen_width +(75*width_scale)

        if self.rect.left < -(85*width_scale):
            self.rect.left = -(85*width_scale)

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        #bouncing
        if not self.spawn:
            if self.rect.top < (-85 *hight_scale):
                self.rect.top = (-85 *hight_scale)

        #walls collisions
        if self.rect.right >= screen_width +(75*width_scale) or self.rect.left <= -(85*width_scale):
            self.direction.x *= -1

        if self.rect.bottom >= screen_height:
            self.direction.y *= -1
        #bouncinggg
        if not self.spawn:
            if self.rect.top <= (-85 *hight_scale):
                self.direction.y *= -1
        ###bouncing counter
        if self.bouncing_phase and (not self.spawn):
            if self.rect.right >= screen_width + (75 * width_scale) or self.rect.left <= -(85 * width_scale) or self.rect.bottom >= screen_height or self.rect.top <= (-85 *hight_scale):
                pygame.mixer.Sound.play(boing_sound)
                self.bouncing_counter += 1

        #attack oil
        if (not self.spawn) and (self.shoot_phase):
            if self.shoot_starter:
                self.speed = (300 * speed_scale)
                self.direction.x = random.choice([-1, 1])
                self.direction.y = 0
                self.shoot_starter = False
            if self.can_shoot:
                boss_oil = Boss_oil(self.rect.midbottom, (all_sprites, ship_laser_group, oil_group))
                boss_oil = Boss_oil((self.rect.centerx + 100*width_scale, self.rect.bottom), (all_sprites, ship_laser_group, oil_group))
                boss_oil = Boss_oil((self.rect.centerx - 100*width_scale, self.rect.bottom), (all_sprites, ship_laser_group, oil_group))
                pygame.mixer.Sound.play(laser_sound)
                self.can_shoot = False
                self.last_shot = pygame.time.get_ticks()
                self.shoot_counter += 1
            if self.shoot_counter >= 15:
                if self.rect.centerx > (screen_width/2 + (5*width_scale)):
                    self.direction.x = -1
                    self.speed = (300*speed_scale)
                elif self.rect.centerx < (screen_width/2 - (5*width_scale)):
                    self.direction.x = 1
                    self.speed = (300*speed_scale)
                else:
                    self.rect.centerx = (screen_width/2)
                    self.direction.x = 0
                    self.direction.y = 0
                    self.shoot_counter = 0
                    self.phase_chooser = random.choice([2,3])
                    if self.phase_chooser == 2:
                        self.bouncing_phase = True
                        self.bouncing_starter = True
                    elif self.phase_chooser == 3:
                        self.laserbeam_phase = True
                        self.laserbeam_starter = True
                    self.shoot_phase = False
        self.laser_time()

        #bouncing attack
        if (not self.spawn) and (self.bouncing_phase):
            if self.bouncing_starter:
                self.direction.x = random.choice([-1,1])
                self.direction.y = 1
                self.speed = (350*speed_scale)
                self.bouncing_starter = False
                self.bouncing_phase = True
            if self.bouncing_counter == 15:
                self.speed = (250 * speed_scale)
                if self.rect.centerx > (screen_width/2 + (5*width_scale)):
                    self.direction.x = -1
                elif self.rect.centerx < (screen_width/2 - (5*width_scale)):
                    self.direction.x = 1
                else:
                    self.rect.centerx = (screen_width/2)
                    self.direction.x = 0
                if self.rect.bottom > (330*hight_scale):
                    self.direction.y = -1
                elif self.rect.bottom < (320*hight_scale):
                    self.direction.y = 1
                else:
                    self.rect.bottom = (325*hight_scale)
                    self.direction.y = 0

                if self.rect.bottom == (325*hight_scale) and self.rect.centerx == (screen_width/2):
                    self.bouncing_counter = 0
                    self.direction.x = 0
                    self.direction.y = 0
                    self.phase_chooser = random.choice([1,3])
                    if self.phase_chooser == 1:
                        self.shoot_starter = True
                        self.shoot_phase = True
                    elif self.phase_chooser == 3:
                        self.laserbeam_phase = True
                        self.laserbeam_starter = True
                    self.bouncing_phase = False
        #laserbeam phase
        if (not self.spawn) and (self.laserbeam_phase):
            if self.laserbeam_starter:
                if self.rect.centery < (screen_height/2 -(50*hight_scale)):
                    self.direction.y = 1
                    self.speed = (200 * speed_scale)
                if self.rect.centery >= (screen_height / 2 - (50 * hight_scale)):
                    self.direction.y = 0
                    self.rect.centery = (screen_height/2 - (50*hight_scale))
                    Boss_laserbeam((boss_laserbeam_group), 90)
                    #Boss_laserbeam((boss_laserbeam_group), 240)
                    Boss_laserbeam((boss_laserbeam_group), 360)

                    pygame.mixer.Sound.play(laserbeam_sound, -1)
                    self.laserbeam_starter = False
            if self.laserbeam_return and (not self.laserbeam_starter):
                pygame.mixer.Sound.stop(laserbeam_sound)
                if self.rect.bottom > (330 * hight_scale):
                    self.direction.y = -1
                elif self.rect.bottom < (320 * hight_scale):
                    self.direction.y = 1
                else:
                    self.rect.bottom = (325 * hight_scale)
                    self.direction.y = 0

                    self.phase_chooser = random.choice([1,2])
                    if self.phase_chooser == 1:
                        self.shoot_starter = True
                        self.shoot_phase = True
                    elif self.phase_chooser == 2:
                        self.bouncing_phase = True
                        self.bouncing_starter = True
                    self.laserbeam_return = False
                    self.laserbeam_phase = False

        #player death
        if not(player.alive):
            # spawn phase
            self.spawn = False

            # phase oil
            self.shoot_starter = False
            self.shoot_phase = False
            self.shoot_counter = 0

            # phase bouncing
            self.bouncing_starter = False
            self.bouncing_phase = False
            self.bouncing_counter = 0

            # phase laser beam
            self.laserbeam_starter = False
            self.laserbeam_phase = False
            self.laserbeam_return= False

            self.speed = (250 * speed_scale)
            if self.rect.centerx > (screen_width/2 + (5*width_scale)):
                self.direction.x = -1
            elif self.rect.centerx < (screen_width/2 - (5*width_scale)):
                self.direction.x = 1
            else:
                self.rect.centerx = (screen_width/2)
                self.direction.x = 0
            if self.rect.bottom > (330*hight_scale):
                self.direction.y = -1
            elif self.rect.bottom < (320*hight_scale):
                self.direction.y = 1
            else:
                self.rect.bottom = (325*hight_scale)
                self.direction.y = 0
            if self.rect.bottom == (325*hight_scale) and self.rect.centerx == (screen_width/2):
                self.direction.x = 0
                self.direction.y = 0
                self.speed = 0
class Boss_oil(pygame.sprite.Sprite):
    def __init__(self,pos, groups):
        super().__init__(groups)
        self.image = babyoil_surf
        self.rect = self.image.get_frect(midtop = pos)

    def update(self, dt):
        self.rect.centery += (500*speed_scale) * dt
        if self.rect.top > screen_height:
            self.kill()
class Boss_laserbeam(pygame.sprite.Sprite):
    def __init__(self, groups, angle):
        super().__init__(groups)
        self.original_image = laserbeam_surf
        self.image = self.original_image
        self.rect = self.image.get_frect(center = (disco_rect.centerx, disco_rect.centery))

        self.rotation_angle = angle

        #timer
        self.last_time = pygame.time.get_ticks()
        self.cooldown_time = 14000
    def update(self, dt):
        self.destroy_laserbeam()
      # transform
        self.image = pygame.transform.rotozoom(self.original_image, self.rotation_angle, 1)

        self.rect = self.image.get_frect(center=self.rect.center)
        self.rotation_angle += -60 * dt
    def destroy_laserbeam(self):
        if pygame.time.get_ticks() - self.last_time >= self.cooldown_time:
            self.kill()
            self.last_time = pygame.time.get_ticks()
            for boss in boss_group:
                boss.laserbeam_return = True
class Boss_death(pygame.sprite.Sprite):
    def __init__(self, groups, pos,posx):
        super().__init__(groups)
        self.image_original = diddy1_surf
        self.image = self.image_original
        self.rect = self.image.get_frect(center=pos)

        self.posx = posx

        self.directionx = 0
        if self.posx > (screen_width/2):
            self.directionx = 0.6
            self.rotation_angle_adder = -0.4
        elif self.posx < (screen_width/2):
            self.directionx = -0.6
            self.rotation_angle_adder = 0.4
        else:
            self.directionx = random.choice([-0.6,0.6])
            if self.directionx == 0.6:
                self.rotation_angle_adder = -0.4
            elif self.directionx == -0.6:
                self.rotation_angle_adder = 0.4

        self.direction = pygame.math.Vector2(self.directionx,1)
        self.speed = (350*speed_scale)
        self.rotation_angle = 0

    def update(self, dt):
        self.despawn()

        self.rect.center += self.direction * self.speed *dt
        self.image = pygame.transform.rotozoom(self.image_original, self.rotation_angle, 1)
        self.rect = self.image.get_frect(center=self.rect.center)
        self.rotation_angle += self.rotation_angle_adder

    def despawn(self):
        if self.rect.top > screen_height:
            self.kill()
            pygame.mixer.Sound.fadeout(minecraft_boom, 500)
            pygame.mixer.Sound.fadeout(minecraft_boom2, 500)
            pygame.mixer.Sound.fadeout(minecraft_boom3, 500)
def spawn_boss():
    if ((int(player.current_score) >= (1000 * scores.n)) and (player.alive) and (not scores.boss_alive)):
        for meteor in meteor_group:
            Explosion_animation(all_sprites, meteor.rect.center)
            meteor.kill()
        for kanye in evil_ye:
            Explosion_animation(all_sprites, kanye.rect.center)
            kanye.kill()
        for ship in ship_group:
            Explosion_animation(all_sprites, ship.rect.center)
            ship.kill()
            if difficulty.ship_spawn >= 0:
                difficulty.ship_spawn -= 1
        pygame.mixer.Sound.play(explosion_sound)
        pygame.mixer.Sound.stop(ye_spawn)
        pygame.mixer.Sound.play(diddy_spawn_sound)
        pygame.mixer.Sound.stop(game_music)
        pygame.mixer.Sound.play(ds3_music, -1)
        # disable spawn
        pygame.time.set_timer(meteor_event, 0)
        pygame.time.set_timer(ship_event, 0)
        pygame.time.set_timer(kanye_event, 0)
        diddy = Boss((all_sprites, boss_group))
        scores.boss_alive = True
        scores.n += 1
def health_bar():
    if scores.boss_alive:
        pygame.draw.line(screen, (0, 0, 0),
                             (screen_width / 2 - (501 * width_scale), (700 * hight_scale)),
                             (screen_width / 2 + (501 * width_scale),(700 * hight_scale)),
                             int(16 * width_scale))
        pygame.draw.line(screen, (128,128,128),
                             (screen_width / 2 - (500 * width_scale), (700 * hight_scale)),
                             (screen_width / 2 + (500 * width_scale), (700 * hight_scale)),
                             int(13 * width_scale))
        for boss in boss_group:
            pygame.draw.line(screen, (255, 71, 76),
                             (screen_width / 2 - (500 * width_scale), (700 * hight_scale)),
                             (screen_width / 2 + ((-500 + (boss.health/boss.max_health * 1000)) * width_scale), (700 * hight_scale)),
                             int(13 * width_scale))
        boss_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(30 * width_scale))
        bosstext_surf = boss_text.render(f"Diddy, The old Diddler", True, (240, 240, 240))
        bosstext_rect = bosstext_surf.get_frect(midleft=(screen_width / 2 - (500 * width_scale),
                                                          (675 * hight_scale)))
        screen.blit(bosstext_surf, bosstext_rect)
class Boss_explosion_animation(pygame.sprite.Sprite):
    def __init__(self, groups,pos,x,y):
        super().__init__(groups)
        self.frames = explosion_frames
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.image = pygame.transform.smoothscale(self.image, (int(self.image.get_width()*width_scale),
                                                               int(self.image.get_height()*hight_scale)))

        self.rect = self.image.get_frect(center=pos)
        self.x = x
        self.y = y
    def update(self, dt):
        self.frames_index += 40 * dt

        for boss_death in boss_death_group:
            self.rect = self.image.get_frect(center=((boss_death.rect.centerx + self.x), (boss_death.rect.centery + self.y)))

        if self.frames_index < len(self.frames):
            self.image = self.frames[int(self.frames_index)]
            #self.image = pygame.transform.scale2x(self.image)
        else:
            self.frames_index = 0
        if (self.rect.top - (200*hight_scale)) > (screen_width/2):
            self.kill()
class Explosion_animation(pygame.sprite.Sprite):
    def __init__(self, groups,pos):
        super().__init__(groups)
        self.frames = explosion_frames
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.image = pygame.transform.smoothscale(self.image, (int(self.image.get_width()*width_scale),
                                                               int(self.image.get_height()*hight_scale)))
        self.rect = self.image.get_frect(center=pos)
    def update(self, dt):
        self.frames_index += 50 * dt
        if self.frames_index < len(self.frames):
            self.image = self.frames[int(self.frames_index)]
        else:
            self.kill()
        if player.alive == False:
            self.image = pygame.transform.scale2x(self.image)
class DynamicDiffuclity():
    def __init__(self):
        self.ye = 13000
        self.ye_float = 0

        self.meteor = 500
        self.meteor_float = 0

        self.ship = 8000
        self.ship_float = 0

        #swift spawn amount cap to 3
        self.ship_spawn = 0
    def update_meteor(self):
        if self.meteor > 100 and player.alive:
            if self.meteor_float < 1:
                self.meteor_float += 0.3
            if self.meteor_float >= 1:
                self.meteor -= int(self.meteor_float)
                pygame.time.set_timer(meteor_event, difficulty.meteor)
                self.meteor_float = 0
    def update_ye(self):
        if self.ye > 5000 and player.alive:
            if self.ye_float < 1:
                self.ye_float += 35
            if self.ye_float >= 1:
                self.ye -= int(self.ye_float)
                pygame.time.set_timer(kanye_event, self.ye)
                self.ye_float = 0
    def update_ship(self):
        if self.ship > 2700 and player.alive:
            if self.ship_float < 1:
                self.ship_float += 20
            if self.ship_float >= 1:
                self.ship -= int(self.ship_float)
                pygame.time.set_timer(ship_event, self.ship)
                self.ship_float = 0
class Nuke(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)

        self.image = pygame.image.load(join('Data', 'nuke.png')).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (int(self.image.get_width()*width_scale),
                                                               int(self.image.get_height()*hight_scale)))
        self.rect = self.image.get_frect(center = pos)

        self.direction = pygame.math.Vector2(random.choice([-1,1]),random.choice([-1,1]))
        self.speed = (350*speed_scale)

        #timer
        self.last_time = pygame.time.get_ticks()
        self.cooldown_time = 8000
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        self.destroy_nuke()

        #wall clipping
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        if self.rect.top < 0:
            self.rect.top = 0
        #wall collisions
        if self.rect.right >= screen_width or self.rect.left <= 0:
            self.direction.x *= -1
        if self.rect.bottom >= screen_height or self.rect.top <= 0:
            self.direction.y *= -1

    #timeout
    def destroy_nuke(self):
        if pygame.time.get_ticks() - self.last_time >= self.cooldown_time:
            self.kill()
            self.last_time = pygame.time.get_ticks()
    #kaboom
    def kaboom(self):
            for meteor in meteor_group:
                Explosion_animation(all_sprites, meteor.rect.center)
                meteor.kill()
                player.kill_count += player.kill_count_adder
                scores.money += player.kill_money_adder * scores.money_multiplier
            for kanye in evil_ye:
                Explosion_animation(all_sprites, kanye.rect.center)
                kanye.kill()
                pygame.mixer.Sound.stop(ye_spawn)
                player.kill_count += player.kill_count_adder
                scores.money += (player.kill_money_adder * 100) * scores.money_multiplier
            for ship in ship_group:
                Explosion_animation(all_sprites, ship.rect.center)
                ship.kill()
                player.kill_count += player.kill_count_adder * player.kill_count_adder
                scores.money += (player.kill_money_adder * 10) * scores.money_multiplier
                if difficulty.ship_spawn > 0:
                    difficulty.ship_spawn -= 1
            for ship_laser in ship_laser_group:
                ship_laser.kill()
            for nuke in nuke_group:
                nuke.kill()
class TeddieDrop(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)

        self.image = pygame.image.load(join('Data', 'teddie_drop.png')).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (int(self.image.get_width()*width_scale),
                                                               int(self.image.get_height()*hight_scale)))
        self.rect = self.image.get_frect(center = pos)

        self.direction = pygame.math.Vector2(random.choice([-1,1]),random.choice([-1,1]))
        self.speed = (350*speed_scale)

        #timer
        self.last_time = pygame.time.get_ticks()
        self.cooldown_time = 8000
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        self.destroy_teddie_drop()

        #wall clipping
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        if self.rect.top < 0:
            self.rect.top = 0
        #wall collisions
        if self.rect.right >= screen_width or self.rect.left <= 0:
            self.direction.x *= -1
        if self.rect.bottom >= screen_height or self.rect.top <= 0:
            self.direction.y *= -1

    #timeout
    def destroy_teddie_drop(self):
        if pygame.time.get_ticks() - self.last_time >= self.cooldown_time:
            self.kill()
            self.last_time = pygame.time.get_ticks()
class Teddie(pygame.sprite.Sprite):
    def __init__(self, groups, angle):
        super().__init__(groups)
        self.image = pygame.image.load(join('Data', 'teddie.png')).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (int(self.image.get_width()*width_scale),
                                                               int(self.image.get_height()*hight_scale)))
        self.rect = self.image.get_frect(center = ((player.rect.x), (player.rect.y + (20*hight_scale))))

        self.speed = (300*speed_scale)

        self.angle = angle
        self.radius = (100*width_scale)

        #timer
        self.last_time = pygame.time.get_ticks()
        self.cooldown_time = 25000
    def update(self, dt):
        #self.rect.center += self.direction * self.speed * dt
        self.angle += self.speed *dt
        self.destroy_teddie()

        self.rect.centerx = player.rect.centerx + self.radius * math.cos(math.radians(self.angle))
        self.rect.centery = player.rect.centery + self.radius * math.sin(math.radians(self.angle))
    #timeout
    def destroy_teddie(self):
        if pygame.time.get_ticks() - self.last_time >= self.cooldown_time:
            self.kill()
            self.last_time = pygame.time.get_ticks()
class Doublex_drop(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)

        self.image = pygame.image.load(join('Data', 'doublekill_drop.png')).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (int(self.image.get_width()*width_scale),
                                                               int(self.image.get_height()*hight_scale)))
        self.rect = self.image.get_frect(center = pos)

        self.direction = pygame.math.Vector2(random.choice([-1,1]),random.choice([-1,1]))
        self.speed = (350*speed_scale)

        #timer
        self.last_time = pygame.time.get_ticks()
        self.cooldown_time = 8000
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        self.destroy_doublex_drop()

        #wall clipping
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        if self.rect.top < 0:
            self.rect.top = 0
        #wall collisions
        if self.rect.right >= screen_width or self.rect.left <= 0:
            self.direction.x *= -1
        if self.rect.bottom >= screen_height or self.rect.top <= 0:
            self.direction.y *= -1

    #timeout
    def destroy_doublex_drop(self):
        if pygame.time.get_ticks() - self.last_time >= self.cooldown_time:
            self.kill()
            self.last_time = pygame.time.get_ticks()
class Countdown(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.time = 20
        self.text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(50 * width_scale))

        self.image = self.text.render(f":{int(self.time)}", True, (255, 71, 76))
        self.rect = self.image.get_frect(midtop=(screen_width/2 , 0))
    def update(self, dt):
        if self.time > 0:
            self.time -= 1 *dt
            screen.blit(clock_surf, (self.rect.x - (35*width_scale), self.rect.y + (3*hight_scale)))
            self.image = self.text.render(f":{int(self.time)}", True, (255, 71, 76))
            player.kill_count_adder = 2
            player.kill_money_adder = 10
        if self.time <= 0:
            player.kill_count_adder = 1
            player.kill_money_adder = 5
            self.kill()
        if not player.alive:
            player.kill_count_adder = 1
            player.kill_money_adder = 5
            self.kill()
def collisions():
    collision_player1 = False
    collision_player2 = False
    collision_player3 = False
    collision_player4 = False
    collision_player5 = False
    collision_player6 = False
    collision_player7 = False
    for laser in laser_group:
        collision_sprite_LM = pygame.sprite.spritecollide(laser, meteor_group, True, pygame.sprite.collide_mask)
        collision_sprite_LS = pygame.sprite.spritecollide(laser, ship_group, True, pygame.sprite.collide_mask)
        if collision_sprite_LM or collision_sprite_LS:
            pygame.mixer.Sound.play(explosion_sound)
            laser.kill()
            player.kill_count += player.kill_count_adder
            Explosion_animation(all_sprites, laser.rect.midtop)
            #drop%
            nuke_drop = random.randint(1,50)
            teddie_drop = random.randint(1,50)
            doublex_drop = random.randint(1,50)
            gold_coin_drop = random.randint(1,100)
            bronze_coin_drop = random.randint(1,10)
            silver_coin_drop = random.randint(1,50)
        if collision_sprite_LM:
            scores.money += player.kill_money_adder * scores.money_multiplier
        if collision_sprite_LS:
            if difficulty.ship_spawn > 0:
                difficulty.ship_spawn -= 1
            scores.money += (player.kill_money_adder * 10) * scores.money_multiplier
        if (collision_sprite_LM or collision_sprite_LS) and (nuke_drop == 1):
            nuke = Nuke((all_sprites, nuke_group), laser.rect.midtop)
        if (collision_sprite_LM or collision_sprite_LS) and (teddie_drop == 1):
            TeddieDrop((all_sprites, teddiedrop_group), laser.rect.midtop)
        if (collision_sprite_LM or collision_sprite_LS) and (doublex_drop == 1):
            Doublex_drop((all_sprites, doublexdrop_group), laser.rect.midtop)
        if (collision_sprite_LM or collision_sprite_LS) and (gold_coin_drop == 1):
            Coins((all_sprites, coins_group), coinye_surf, laser.rect.midtop,laser.rect.y - 25 ,1000)
        if (collision_sprite_LM or collision_sprite_LS) and (silver_coin_drop == 1):
            Coins((all_sprites, coins_group), coinye_s_surf, laser.rect.midtop,laser.rect.y - 18,250)
        if (collision_sprite_LM or collision_sprite_LS) and (bronze_coin_drop == 1):
            Coins((all_sprites, coins_group), coinye_b_surf, laser.rect.midtop,laser.rect.y -5,50)
        collision_evilye = pygame.sprite.spritecollide(laser, evil_ye, True, pygame.sprite.collide_mask)
        if collision_evilye:
            pygame.mixer.Sound.stop(ye_spawn)
            pygame.mixer.Sound.play(explosion_sound)
            pygame.mixer.Sound.play(ye_death)
            # no annoying voice
            pygame.time.set_timer(kanye_event, 0)
            pygame.time.set_timer(ship_event, 0)

            for ship in ship_group:
                ship.kill()
                if difficulty.ship_spawn > 0:
                    difficulty.ship_spawn -= 1
            laser.kill()
            player.kill()
            player.alive = False
            scores.death_count += 1
            Explosion_animation(all_sprites, laser.rect.midtop)
            Explosion_animation(all_sprites, player.rect.center)
            pygame.mixer.Sound.stop(game_music)
        collision_boss = pygame.sprite.spritecollide(laser, boss_group, False, pygame.sprite.collide_mask)
        if collision_boss:
            pygame.mixer.Sound.play(explosion_sound)
            laser.kill()
            Explosion_animation(all_sprites, laser.rect.midtop)
            for boss in boss_group:
                boss.health -= 1
                if boss.health <= 0:
                    boss.kill()
                    player.kill_count += player.kill_count_adder
                    scores.money += (player.kill_money_adder * 1000) * scores.money_multiplier
                    scores.boss_alive = False
                    channel2.play(diamond_sound)
                    pygame.mixer.Sound.stop(laserbeam_sound)
                    pygame.mixer.Sound.stop(ds3_music)
                    pygame.mixer.Sound.play(game_music, -1)
                    Diamond((all_sprites, coins_group), diamond_surf, boss.rect.center,boss.rect.centery, 5000)
                    for laserbeam in boss_laserbeam_group:
                        laserbeam.kill()

                    #death effects
                    Boss_death((all_sprites, boss_death_group), boss.rect.center, boss.rect.centerx)
                    for boss_death in boss_death_group:
                        pygame.mixer.Sound.play(minecraft_boom, -1)
                        pygame.mixer.Sound.play(minecraft_boom2, -1)
                        pygame.mixer.Sound.play(minecraft_boom3, -1)

                        Boss_explosion_animation((all_sprites), (boss_death.rect.center), (45*width_scale), (-15*hight_scale))
                        Boss_explosion_animation((all_sprites), (boss_death.rect.center), (-50*width_scale), (100*hight_scale))
                        Boss_explosion_animation((all_sprites), (boss_death.rect.center), (60*width_scale), (120*hight_scale))

                    #reset spawn
                    pygame.time.set_timer(meteor_event, difficulty.meteor)
                    pygame.time.set_timer(ship_event, difficulty.ship)
                    pygame.time.set_timer(kanye_event, difficulty.ye)

    if player.alive:
        collision_player1 = pygame.sprite.spritecollide(player, meteor_group, True, pygame.sprite.collide_mask)
        collision_player2 = pygame.sprite.spritecollide(player, evil_ye, True, pygame.sprite.collide_mask)
        collision_player3 = pygame.sprite.spritecollide(player, ship_group, True, pygame.sprite.collide_mask)
        collision_player7 = pygame.sprite.spritecollide(player, oil_group, False, pygame.sprite.collide_mask)
        collision_player4 = pygame.sprite.spritecollide(player, ship_laser_group, True, pygame.sprite.collide_mask)
        collision_player5 = pygame.sprite.spritecollide(player, boss_group, False, pygame.sprite.collide_mask)
        collision_player6 = pygame.sprite.spritecollide(player, boss_laserbeam_group, False, pygame.sprite.collide_mask)
        for nuke in nuke_group:
            collision_sprite_NP = pygame.sprite.spritecollide(player, nuke_group, False, pygame.sprite.collide_mask)
            if collision_sprite_NP:
                nuke.kaboom()
                Explosion_animation(all_sprites, nuke.rect.center)
                pygame.mixer.Sound.play(nuke_sound)
        for doublex in doublexdrop_group:
            collision_sprite_DP = pygame.sprite.spritecollide(player, doublexdrop_group, False, pygame.sprite.collide_mask)
            if collision_sprite_DP:
                Explosion_animation(all_sprites, doublex.rect.center)
                pygame.mixer.Sound.play(doublex_sound)
                if countdown_group:
                    for countdown in countdown_group:
                        countdown.kill()
                Countdown(countdown_group)
                for doublex in doublexdrop_group:
                    doublex.kill()
        for teddie_drop in teddiedrop_group:
            collision_sprite_TP = pygame.sprite.spritecollide(player, teddiedrop_group, False, pygame.sprite.collide_mask)
            if collision_sprite_TP:
                pygame.mixer.Sound.play(teddie_drop_sound)
                Explosion_animation(all_sprites, teddie_drop.rect.center)
                teddie1 = Teddie((all_sprites, teddie_group), 0)
                teddie2 = Teddie((all_sprites, teddie_group), 120)
                teddie3 = Teddie((all_sprites, teddie_group), 240)
                for teddie_drop in teddiedrop_group:
                    teddie_drop.kill()
        for teddie in teddie_group:
            collision_sprite_TM = pygame.sprite.spritecollide(teddie, meteor_group, True, pygame.sprite.collide_mask)
            collision_sprite_TS = pygame.sprite.spritecollide(teddie, ship_group, True, pygame.sprite.collide_mask)
            collision_sprite_TK = pygame.sprite.spritecollide(teddie, evil_ye, True, pygame.sprite.collide_mask)
            collision_sprite_TL = pygame.sprite.spritecollide(teddie, ship_laser_group, True, pygame.sprite.collide_mask)
            collision_sprite_TB = pygame.sprite.spritecollide(teddie, boss_group, False, pygame.sprite.collide_mask)
            if collision_sprite_TM or collision_sprite_TS or collision_sprite_TK:
                player.kill_count += player.kill_count_adder
                scores.money += player.kill_money_adder * scores.money_multiplier
                Explosion_animation(all_sprites, teddie.rect.center)
                pygame.mixer.Sound.play(explosion_sound)
                teddie.kill()
            if collision_sprite_TK:
                scores.money += (player.kill_money_adder * 100) * scores.money_multiplier
                pygame.mixer.Sound.stop(ye_spawn)
            if collision_sprite_TS:
                if difficulty.ship_spawn > 0:
                    difficulty.ship_spawn -= 1
                scores.money += (player.kill_money_adder * 10) * scores.money_multiplier
            if collision_sprite_TL:
                Explosion_animation(all_sprites, teddie.rect.center)
                pygame.mixer.Sound.play(explosion_sound)
                teddie.kill()
            if collision_sprite_TB:
                pygame.mixer.Sound.play(explosion_sound)
                teddie.kill()
                Explosion_animation(all_sprites, teddie.rect.center)
                for boss in boss_group:
                    boss.health -= 1
                    if boss.health <= 0:
                        boss.kill()
                        player.kill_count += player.kill_count_adder
                        scores.money += (player.kill_money_adder * 1000) * scores.money_multiplier
                        scores.boss_alive = False
                        channel2.play(diamond_sound)
                        pygame.mixer.Sound.stop(laserbeam_sound)
                        pygame.mixer.Sound.stop(ds3_music)
                        pygame.mixer.Sound.play(game_music, -1)
                        Diamond((all_sprites, coins_group), diamond_surf, boss.rect.center,boss.rect.centery,5000)
                        for laserbeam in boss_laserbeam_group:
                            laserbeam.kill()

                        #death effects
                        for boss_death in boss_death_group:
                            pygame.mixer.Sound.play(minecraft_boom, -1)
                            pygame.mixer.Sound.play(minecraft_boom2, -1)
                            pygame.mixer.Sound.play(minecraft_boom3, -1)
                            Boss_explosion_animation((all_sprites), (boss_death.rect.center), (45 * width_scale),
                                                     (-15 * hight_scale))
                            Boss_explosion_animation((all_sprites), (boss_death.rect.center), (-50 * width_scale),
                                                     (100 * hight_scale))
                            Boss_explosion_animation((all_sprites), (boss_death.rect.center), (60 * width_scale),
                                                     (120 * hight_scale))
                        # reset spawn
                        pygame.time.set_timer(meteor_event, difficulty.meteor)
                        pygame.time.set_timer(ship_event, difficulty.ship)
                        pygame.time.set_timer(kanye_event, difficulty.ye)

        for coins in coins_group:
            collision_sprite_CP = pygame.sprite.spritecollide(player, coins_group, True, pygame.sprite.collide_mask)
            if collision_sprite_CP:
                pygame.mixer.Sound.play(coins_sound)
                scores.money += coins.value * player.kill_count_adder * scores.money_multiplier
    if not player.alive:
        for teddie in teddie_group:
            teddie.kill()
    if (collision_player1 or collision_player2 or collision_player3 or collision_player4 or collision_player5 or collision_player6) and (player.alive):
        pygame.mixer.Sound.play(explosion_sound)
        pygame.mixer.Sound.stop(ye_spawn)
        pygame.mixer.Sound.stop(laserbeam_sound)
        #no annoying voice
        pygame.time.set_timer(kanye_event, 0)
        pygame.time.set_timer(ship_event, 0)
        for ship in ship_group:
            ship.kill()
            if difficulty.ship_spawn > 0:
                difficulty.ship_spawn -= 1
        for laserbeam in boss_laserbeam_group:
            laserbeam.kill()
        player.kill()
        player.alive = False
        scores.death_count += 1
        Explosion_animation(all_sprites,player.rect.center)
        pygame.mixer.Sound.stop(game_music)
        pygame.mixer.Sound.stop(ds3_music)
    if collision_player2 and player.alive == False:
        pygame.mixer.Sound.play(ye_death)
    if (collision_player5 or collision_player6 or collision_player7) and (not player.alive):
        pygame.mixer.Sound.play(diddy_death_sound)
    if player.alive == False:
        pygame.mixer.Sound.stop(game_music)
        pygame.mixer.Sound.stop(ds3_music)
def display_ui():
    global running
    def score():
        score_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(50 * width_scale))
        score_surf = score_text.render(f"{int(player.current_score)}", True, (240, 240, 240))
        score_rect = score_surf.get_frect(center=(screen_width/2 ,screen_height-(80*hight_scale)))
        screen.blit(score_surf, score_rect)
        pygame.draw.rect(screen, (240,240,240), score_rect.inflate((20*width_scale),(20*hight_scale)).move(0,(-7*hight_scale)),
                         int(5*width_scale), int(10*width_scale))
    def killcount():
        killcount_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(40 * width_scale))
        killcount_surf = killcount_text.render(f"{player.kill_count}", True, (240, 240, 240))
        killcount_rect = killcount_surf.get_frect(topright=(screen_width,0))
        screen.blit(killcount_surf, killcount_rect)
        screen.blit(skull_surf, (killcount_rect.x - (35*width_scale), killcount_rect.y))
    def moneycount():
        moneycount_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(40 * width_scale))
        moneycount_surf = moneycount_text.render(f"{scores.money}", True, (255,223,0))
        moneycount_rect = moneycount_surf.get_frect(topleft=(0,0))
        screen.blit(moneycount_surf, moneycount_rect)
        screen.blit(coin_ui_surf, (moneycount_rect.right, moneycount_rect.left))
    def hikillcount():
        hikill_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(35 * width_scale))
        hikill_surf = hikill_text.render(f"Highest kills: {scores.hikill_count}", True, (255, 71, 76))
        hikill_rect = hikill_surf.get_frect(center=(screen_width/2 , screen_height/2 + (25*hight_scale)))
        screen.blit(hikill_surf, hikill_rect)
    def deathcount():
        deathcount_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(35 * width_scale))
        deathcount_surf = deathcount_text.render(f"Death count: {scores.death_count}", True, (255, 71, 76))
        deathcount_rect = deathcount_surf.get_frect(center=(screen_width/2 , screen_height/2 + (50*hight_scale)))
        #screen.blit(deathcount_surf, deathcount_rect)
    def hiscore():
        hiscore_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(35 * width_scale))
        hiscore_surf = hiscore_text.render(f"High score: {scores.high_score}", True, (255, 71, 76))
        hiscore_rect = hiscore_surf.get_frect(center=(screen_width/2 , screen_height/2 - (25*hight_scale)))
        screen.blit(hiscore_surf, hiscore_rect)
    def respawn_text():
        respawntext = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(60 * width_scale))
        respawntext_surf = respawntext.render(f"[RESTART]", True, (160,60,225))
        respawntext_rect = respawntext_surf.get_frect(center=(screen_width/2 , screen_height/2 + (225*hight_scale)))
        if not player.alive and respawntext_rect.collidepoint((mouse_x,mouse_y)):
            respawntext = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(65 * width_scale))
            respawntext_surf = respawntext.render(f"[RESTART]", True, (240, 240, 240))
            respawntext_rect = respawntext_surf.get_frect(center=(screen_width / 2, screen_height / 2 + (225*hight_scale)))
            screen.blit(respawntext_surf, respawntext_rect)
        else:
            screen.blit(respawntext_surf, respawntext_rect)
    def main_menu_text():
        mainmenutext = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(40 * width_scale))
        mainmenutext_surf = mainmenutext.render(f"[MAIN MENU]", True, (160,60,225))
        mainmenutext_rect = mainmenutext_surf.get_frect(center=(screen_width/2 , screen_height/2 + (325*hight_scale)))
        if not player.alive and mainmenutext_rect.collidepoint((mouse_x,mouse_y)):
            mainmenutext = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(45 * width_scale))
            mainmenutext_surf = mainmenutext.render(f"[MAIN MENU]", True, (240, 240, 240))
            mainmenutext_rect = mainmenutext_surf.get_frect(center=(screen_width / 2, screen_height / 2 + (325*hight_scale)))
            screen.blit(mainmenutext_surf, mainmenutext_rect)
        else:
            screen.blit(mainmenutext_surf, mainmenutext_rect)
    def spawn_text():
        spawntext = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(60 * width_scale))
        spawntext_surf = spawntext.render(f"[START]", True, (160,60,225))
        spawntext_rect = spawntext_surf.get_frect(center=(screen_width/2 , screen_height/2 + (235*hight_scale)))

        if not player.alive and spawntext_rect.collidepoint((mouse_x,mouse_y)):
            spawntext = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(65 * width_scale))
            spawntext_surf = spawntext.render(f"[START]", True, (240, 240, 240))
            spawntext_rect = spawntext_surf.get_frect(center=(screen_width / 2, screen_height / 2 + (235*hight_scale)))
            screen.blit(spawntext_surf, spawntext_rect)
        else:
            screen.blit(spawntext_surf, spawntext_rect)
    def quit_text():
        quittext = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(40 * width_scale))
        quittext_surf = quittext.render(f"[QUIT GAME]", True, (160,60,225))
        quittext_rect = quittext_surf.get_frect(center=(screen_width/2 , screen_height/2 + (325*hight_scale)))
        if not player.alive and quittext_rect.collidepoint((mouse_x,mouse_y)):
            quittext = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(45 * width_scale))
            quittext_surf = quittext.render(f"[QUIT GAME]", True, (240, 240, 240))
            quittext_rect = quittext_surf.get_frect(center=(screen_width / 2, screen_height / 2 + (325*hight_scale)))
            screen.blit(quittext_surf, quittext_rect)
        else:
            screen.blit(quittext_surf, quittext_rect)
    def reset_window():
        window_border = pygame.draw.rect(screen, (105,105,105),(screen_width/2 - (350*width_scale),screen_height/2 - (200*hight_scale),
                                                                (700*width_scale),(400*hight_scale)),border_radius=int(15*width_scale))
        title_window = pygame.draw.rect(screen, (128,128,128),(screen_width/2 - (350*width_scale),screen_height/2 - (200*hight_scale)
                                                               ,(700*width_scale),(50*hight_scale)),border_top_left_radius=int(15*width_scale), border_top_right_radius=int(15*width_scale))

        title_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(30 * width_scale))
        title_surf = title_text.render(f"Delete all saved data and quit?", True, (240, 240, 240))
        title_rect = title_surf.get_frect(center=(screen_width/2,screen_height/2 - (170*hight_scale)))
        screen.blit(title_surf, title_rect)

        ok_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(30 * width_scale))
        ok_surf = ok_text.render(f"OK", True, (255, 71, 76))
        ok_rect = ok_surf.get_frect(center=(screen_width / 2 - (265*width_scale), screen_height / 2 + (150*hight_scale)))

        cancel_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(30 * width_scale))
        cancel_surf = cancel_text.render(f"CANCEL", True, (0, 171, 102))
        cancel_rect = cancel_surf.get_frect(center=(screen_width / 2 + (250*width_scale), screen_height/2 + (150*hight_scale)))

        main_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(30 * width_scale))
        main_surf = main_text.render(f"This process will completely delete\nall your data.\n"
                                     f"This action is irreversible.", True, (240,240,240))
        main_rect = main_surf.get_frect(center=(screen_width / 2, screen_height/2))

        global button_cancel, button_ok
        button_cancel = pygame.draw.rect(screen, (220, 220, 220), cancel_rect.inflate((20*width_scale),
                                                                                      (20*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
        button_ok = pygame.draw.rect(screen, (220, 220, 220), ok_rect.inflate((20*width_scale),
                                                                              (20*hight_scale)).move(0, (-7*hight_scale)),border_radius=int(10*width_scale))

        if not player.alive and button_ok.collidepoint((mouse_x,mouse_y)):
            ok_surf = ok_text.render(f"OK", True, (228, 0, 6))
        if not player.alive and button_cancel.collidepoint((mouse_x,mouse_y)):
            cancel_surf = cancel_text.render(f"CANCEL", True, (0, 222, 132))
        screen.blit(main_surf, main_rect)
        screen.blit(ok_surf, ok_rect)
        screen.blit(cancel_surf, cancel_rect)
    def settings_window():
        window_border = pygame.draw.rect(screen, (105,105,105),(screen_width/2 - (350*width_scale),screen_height/2 - (200*hight_scale),
                                                                (700*width_scale),(400*hight_scale)),border_radius=int(15*width_scale))
        title_window = pygame.draw.rect(screen, (128,128,128),(screen_width/2 - (350*width_scale),screen_height/2 - (200*hight_scale)
                                                               ,(700*width_scale),(50*hight_scale)),border_top_left_radius=int(15*width_scale), border_top_right_radius=int(15*width_scale))

        title_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(30 * width_scale))
        title_surf = title_text.render(f"SETTINGS", True, (240, 240, 240))
        title_rect = title_surf.get_frect(center=(screen_width/2,screen_height/2 - (170*hight_scale)))
        screen.blit(title_surf, title_rect)

        ok_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(30 * width_scale))
        if (scores.screen_width_c, scores.screen_height_c) != (screen_width, screen_height_):
            ok_surf = ok_text.render(f"SAVE & EXIT", True, (0, 171, 102))
        if (scores.screen_width_c, scores.screen_height_c) == (screen_width, screen_height_):
            ok_surf = ok_text.render(f"SAVE", True, (0, 171, 102))

        ok_rect = ok_surf.get_frect(center=(screen_width / 2 - (225*width_scale), screen_height / 2 + (150*hight_scale)))

        cancel_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(30 * width_scale))
        cancel_surf = cancel_text.render(f"CANCEL", True, (255, 71, 76))
        cancel_rect = cancel_surf.get_frect(center=(screen_width / 2 + (250*width_scale), screen_height/2 + (150*hight_scale)))

        video1_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        video1_surf = video1_text.render(f"16:9 Resolutions", True, (240, 240, 240))
        video1_rect = video1_surf.get_frect(center=(screen_width/2,screen_height/2 - (125*hight_scale)))
        screen.blit(video1_surf, video1_rect)

        video2_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(25 * width_scale))
        video2_surf = video2_text.render(f"16:10 Resolutions", True, (240, 240, 240))
        video2_rect = video2_surf.get_frect(center=(screen_width/2,screen_height/2 - (50*hight_scale)))
        screen.blit(video2_surf, video2_rect)

        res1_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        res1_surf = res1_text.render(f"1280x720", True, (255, 71, 76))
        res1_rect = res1_surf.get_frect(center=(screen_width / 2 - (265*width_scale), screen_height / 2 - (90*hight_scale)))

        res2_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        res2_surf = res2_text.render(f"1360x765", True, (255, 71, 76))
        res2_rect = res2_surf.get_frect(center=(screen_width / 2 - (135*width_scale), screen_height / 2 - (90*hight_scale)))

        res3_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        res3_surf = res3_text.render(f"1920x1080", True, (255, 71, 76))
        res3_rect = res3_surf.get_frect(center=(screen_width / 2 , screen_height / 2 - (90*hight_scale)))

        res4_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        res4_surf = res4_text.render(f"2560x1440", True, (255, 71, 76))
        res4_rect = res4_surf.get_frect(center=(screen_width / 2 + (135*width_scale), screen_height / 2 - (90*hight_scale)))

        res5_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        res5_surf = res5_text.render(f"3840x2160", True, (255, 71, 76))
        res5_rect = res5_surf.get_frect(center=(screen_width / 2 + (270*width_scale), screen_height / 2 - (90*hight_scale)))

        res6_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        res6_surf = res6_text.render(f"1280x800", True, (255, 71, 76))
        res6_rect = res6_surf.get_frect(center=(screen_width / 2 - (265*width_scale), screen_height / 2 - (15*hight_scale)))

        res7_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        res7_surf = res7_text.render(f"1440x900", True, (255, 71, 76))
        res7_rect = res7_surf.get_frect(center=(screen_width / 2 - (135*width_scale), screen_height / 2 - (15*hight_scale)))

        res8_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        res8_surf = res8_text.render(f"1920x1200", True, (255, 71, 76))
        res8_rect = res8_surf.get_frect(center=(screen_width / 2 , screen_height / 2 - (15*hight_scale)))

        res9_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        res9_surf = res9_text.render(f"2560x1600", True, (255, 71, 76))
        res9_rect = res9_surf.get_frect(center=(screen_width / 2 + (135*width_scale), screen_height / 2 - (15*hight_scale)))

        res10_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(20 * width_scale))
        res10_surf = res10_text.render(f"3840x2400", True, (255, 71, 76))
        res10_rect = res10_surf.get_frect(center=(screen_width / 2 + (270*width_scale), screen_height / 2 - (15*hight_scale)))

        global button_cancel2, button_ok2,button_sfx,button_music,button_res1, button_res2, button_res3, button_res4, button_res5,button_res6, button_res7, button_res8, button_res9, button_res10
        button_cancel2 = pygame.draw.rect(screen, (220, 220, 220), cancel_rect.inflate((20*width_scale),
                                                                                      (20*hight_scale)).move(0, (-7*hight_scale)), border_radius=int(10*width_scale))
        button_ok2 = pygame.draw.rect(screen, (220, 220, 220), ok_rect.inflate((20*width_scale),
                                                                              (20*hight_scale)).move(0, (-7*hight_scale)),border_radius=int(10*width_scale))
        button_sfx = pygame.draw.rect(screen, (80,80,80), sfx_rect.inflate((15*width_scale),
                                                                              (15*hight_scale)).move(0, (-4*hight_scale)),border_radius=int(10*width_scale))
        button_music = pygame.draw.rect(screen, (80,80,80), music_rect.inflate((15*width_scale),
                                                                              (15*hight_scale)).move(0, (-4*hight_scale)),border_radius=int(10*width_scale))
        button_res1 = pygame.draw.rect(screen, (68, 68, 68), res1_rect.inflate((15*width_scale),
                                                                              (15*hight_scale)).move(0, (-4*hight_scale)),border_radius=int(10*width_scale))
        button_res2 = pygame.draw.rect(screen, (68, 68, 68), res2_rect.inflate((15*width_scale),
                                                                              (15*hight_scale)).move(0, (-4*hight_scale)),border_radius=int(10*width_scale))
        button_res3 = pygame.draw.rect(screen, (68, 68, 68), res3_rect.inflate((15*width_scale),
                                                                              (15*hight_scale)).move(0, (-4*hight_scale)),border_radius=int(10*width_scale))
        button_res4 = pygame.draw.rect(screen, (68, 68, 68), res4_rect.inflate((15*width_scale),
                                                                              (15*hight_scale)).move(0, (-4*hight_scale)),border_radius=int(10*width_scale))
        button_res5 = pygame.draw.rect(screen, (68, 68, 68), res5_rect.inflate((15*width_scale),
                                                                              (15*hight_scale)).move(0, (-4*hight_scale)),border_radius=int(10*width_scale))
        button_res6 = pygame.draw.rect(screen, (68, 68, 68), res6_rect.inflate((15*width_scale),
                                                                              (15*hight_scale)).move(0, (-4*hight_scale)),border_radius=int(10*width_scale))
        button_res7 = pygame.draw.rect(screen, (68, 68, 68), res7_rect.inflate((15*width_scale),
                                                                              (15*hight_scale)).move(0, (-4*hight_scale)),border_radius=int(10*width_scale))
        button_res8 = pygame.draw.rect(screen, (68, 68, 68), res8_rect.inflate((15*width_scale),
                                                                              (15*hight_scale)).move(0, (-4*hight_scale)),border_radius=int(10*width_scale))
        button_res9 = pygame.draw.rect(screen, (68, 68, 68), res9_rect.inflate((15*width_scale),
                                                                              (15*hight_scale)).move(0, (-4*hight_scale)),border_radius=int(10*width_scale))
        button_res10 = pygame.draw.rect(screen, (68, 68, 68), res10_rect.inflate((15*width_scale),
                                                                              (15*hight_scale)).move(0, (-4*hight_scale)),border_radius=int(10*width_scale))
        #hover
        if not player.alive and button_ok2.collidepoint((mouse_x,mouse_y)):
            if (scores.screen_width_c, scores.screen_height_c) != (screen_width, screen_height_):
                ok_surf = ok_text.render(f"SAVE & EXIT", True, (0, 222, 132))
            if (scores.screen_width_c, scores.screen_height_c) == (screen_width, screen_height_):
                ok_surf = ok_text.render(f"SAVE", True, (0, 222, 132))
        if not player.alive and button_cancel2.collidepoint((mouse_x,mouse_y)):
            cancel_surf = cancel_text.render(f"CANCEL", True, (228, 0, 6))
        if (not player.alive) and (button_res1.collidepoint((mouse_x,mouse_y)) and ((scores.screen_width_c,scores.screen_height_c) != (1280,720))):
            res1_surf = res1_text.render(f"1280x720", True, (228, 0, 6))
        if (not player.alive) and (button_res2.collidepoint((mouse_x,mouse_y)) and ((scores.screen_width_c,scores.screen_height_c) != (1360,765))):
            res2_surf = res2_text.render(f"1360x765", True, (228, 0, 6))
        if (not player.alive) and (button_res3.collidepoint((mouse_x,mouse_y)) and ((scores.screen_width_c,scores.screen_height_c) != (1920,1080))):
            res3_surf = res3_text.render(f"1920x1080", True, (228, 0, 6))
        if (not player.alive) and (button_res4.collidepoint((mouse_x,mouse_y)) and ((scores.screen_width_c,scores.screen_height_c) != (2560,1440))):
            res4_surf = res4_text.render(f"2560x1440", True, (228, 0, 6))
        if (not player.alive) and (button_res5.collidepoint((mouse_x,mouse_y)) and ((scores.screen_width_c,scores.screen_height_c) != (3840,2160))):
            res5_surf = res5_text.render(f"3840x2160", True, (228, 0, 6))
        if (not player.alive) and (button_res6.collidepoint((mouse_x,mouse_y)) and ((scores.screen_width_c,scores.screen_height_c) != (1280,800))):
            res6_surf = res6_text.render(f"1280x800", True, (228, 0, 6))
        if (not player.alive) and (button_res7.collidepoint((mouse_x,mouse_y)) and ((scores.screen_width_c,scores.screen_height_c) != (1440,900))):
            res7_surf = res7_text.render(f"1440x900", True, (228, 0, 6))
        if (not player.alive) and (button_res8.collidepoint((mouse_x,mouse_y)) and ((scores.screen_width_c,scores.screen_height_c) != (1920,1200))):
            res8_surf = res8_text.render(f"1920x1200", True, (228, 0, 6))
        if (not player.alive) and (button_res9.collidepoint((mouse_x,mouse_y)) and ((scores.screen_width_c,scores.screen_height_c) != (2560,1600))):
            res9_surf = res9_text.render(f"2560x1600", True, (228, 0, 6))
        if (not player.alive) and (button_res10.collidepoint((mouse_x,mouse_y)) and ((scores.screen_width_c,scores.screen_height_c) != (3840,2400))):
            res10_surf = res10_text.render(f"3840x2400", True, (228, 0, 6))
        if (not player.alive) and (info_rect.collidepoint((mouse_x,mouse_y))):
            infotext_text = pygame.font.Font(join('Data', 'Oxanium-Bold.ttf'), int(14 * width_scale))
            infotext_surf = infotext_text.render(f"Note: Don't use a higher game resolution than your monitor's,\n"
                                                      f"this could make the game unplayable.\n"
                                                      f"Press L-SHIFT and ESCAPE to quit & reset video settings.\n"
                                                      f"Have fun! game made by Ahmed Algailany :)", True, (255, 255, 255))
            #hmm.. if you are reading this then wow hello, dont steal the credits!
            infotext_rect = infotext_surf.get_frect(
                center=(screen_width / 2 , screen_height/2 + (250*hight_scale)))
            screen.blit(infotext_surf, infotext_rect)
            screen.blit(info_surf_hover, info_rect_hover)

        #clicked
        if (not player.alive) and (button_res1.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            res1_surf = res1_text.render(f"1280x720", True, (0, 222, 132))
            scores.screen_width_c,scores.screen_height_c = 1280,720
        if (not player.alive) and (button_res2.collidepoint((mouse_x,mouse_y))and pygame.mouse.get_just_pressed()[0]):
            res2_surf = res2_text.render(f"1360x765", True, (0, 222, 132))
            scores.screen_width_c,scores.screen_height_c = 1360,765
        if (not player.alive) and (button_res3.collidepoint((mouse_x,mouse_y))and pygame.mouse.get_just_pressed()[0]):
            res3_surf = res3_text.render(f"1920x1080", True, (0, 222, 132))
            scores.screen_width_c, scores.screen_height_c = 1920,1080
        if (not player.alive) and (button_res4.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            res4_surf = res4_text.render(f"2560x1440", True, (0, 222, 132))
            scores.screen_width_c, scores.screen_height_c = 2560,1440
        if (not player.alive) and (button_res5.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            res5_surf = res5_text.render(f"3840x2160", True, (0, 222, 132))
            scores.screen_width_c, scores.screen_height_c =3840,2160
        if (not player.alive) and (button_res6.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            res6_surf = res6_text.render(f"1280x800", True, (0, 222, 132))
            scores.screen_width_c, scores.screen_height_c = 1280,800
        if (not player.alive) and (button_res7.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            res7_surf = res7_text.render(f"1440x900", True, (0, 222, 132))
            scores.screen_width_c, scores.screen_height_c = 1440,900
        if (not player.alive) and (button_res8.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            res8_surf = res8_text.render(f"1920x1200", True, (0, 222, 132))
            scores.screen_width_c, scores.screen_height_c = 1920,1200
        if (not player.alive) and (button_res9.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            res9_surf = res9_text.render(f"2560x1600", True, (0, 222, 132))
            scores.screen_width_c, scores.screen_height_c = 2560,1600
        if (not player.alive) and (button_res10.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            res10_surf = res10_text.render(f"3840x2400", True, (0, 222, 132))
            scores.screen_width_c, scores.screen_height_c = 3840,2400
        #update
        match scores.screen_width_c,scores.screen_height_c:
            case 1280,720:
                res1_surf = res1_text.render(f"1280x720", True, (0, 222, 132))
            case 1360,765:
                res2_surf = res2_text.render(f"1360x765", True, (0, 222, 132))
            case 1920,1080:
                res3_surf = res3_text.render(f"1920x1080", True, (0, 222, 132))
            case 2560,1440:
                res4_surf = res4_text.render(f"2560x1440", True, (0, 222, 132))
            case 3840,2160:
                res5_surf = res5_text.render(f"3840x2160", True, (0, 222, 132))
            case 1280,800:
                res6_surf = res6_text.render(f"1280x800", True, (0, 222, 132))
            case 1440,900:
                res7_surf = res7_text.render(f"1440x900", True, (0, 222, 132))
            case 1920,1200:
                res8_surf = res8_text.render(f"1920x1200", True, (0, 222, 132))
            case 2560,1600:
                res9_surf = res9_text.render(f"2560x1600", True, (0, 222, 132))
            case 3840,2400:
                res10_surf = res10_text.render(f"3840x2400", True, (0, 222, 132))


        if not player.alive and button_sfx.collidepoint((mouse_x,mouse_y)):
            button_sfx = pygame.draw.rect(screen, (90, 90, 90), sfx_rect.inflate((15 * width_scale),
                                                                                 (15 * hight_scale)).move(0,
                                                (-4 * hight_scale)), border_radius=int(10 * width_scale))
            screen.blit(sfx_surf, sfx_rect)
            if scores.mute_sfx:
                pygame.draw.line(screen, (255, 71, 76),
                                 (screen_width / 2 - (95 * width_scale), screen_height / 2 + (100 * hight_scale)),
                                 (screen_width / 2 - (25 * width_scale), screen_height / 2 + (20 * hight_scale)),
                                 int(23 * width_scale))
        else:
            screen.blit(sfx_surf, sfx_rect)
        if not player.alive and button_music.collidepoint((mouse_x,mouse_y)):
            button_music = pygame.draw.rect(screen, (90, 90, 90), music_rect.inflate((15 * width_scale),
                                                                                 (15 * hight_scale)).move(0,
                                                (-4 * hight_scale)), border_radius=int(10 * width_scale))
            screen.blit(music_surf, music_rect)
            if scores.mute_music:
                pygame.draw.line(screen, (255, 71, 76),
                                 (screen_width / 2 + (15 * width_scale), screen_height / 2 + (100 * hight_scale)),
                                 (screen_width / 2 + (80* width_scale), screen_height / 2 + (20 * hight_scale)),
                                 int(23 * width_scale))
        else:
            screen.blit(music_surf, music_rect)
        screen.blit(ok_surf, ok_rect)
        screen.blit(cancel_surf, cancel_rect)
        screen.blit(res1_surf, res1_rect)
        screen.blit(res2_surf, res2_rect)
        screen.blit(res3_surf, res3_rect)
        screen.blit(res4_surf, res4_rect)
        screen.blit(res5_surf, res5_rect)
        screen.blit(res6_surf, res6_rect)
        screen.blit(res7_surf, res7_rect)
        screen.blit(res8_surf, res8_rect)
        screen.blit(res9_surf, res9_rect)
        screen.blit(res10_surf, res10_rect)
        if not ((not player.alive) and (info_rect.collidepoint((mouse_x,mouse_y)))):
            screen.blit(info_surf,info_rect)
    def game_title():
        nametext = pygame.font.Font(join('Data', 'SpacieOpera-xR965.otf'), int(100 * width_scale))
        nametext_surf = nametext.render(f"B   UNCING KANYE", True, (240,240,240))
        nametext_rect = nametext_surf.get_frect(center=(screen_width/2 , (150*hight_scale)))
        screen.blit(nametext_surf, nametext_rect)
        surf = pygame.image.load(join('Data', 'kanye o.png')).convert_alpha()
        surf = pygame.transform.smoothscale(surf, (int(surf.get_width()*0.13*width_scale),
                                                   int(surf.get_height()*0.13*hight_scale)))
        screen.blit(surf,((335*width_scale),(65*hight_scale)))
    def update():
        if player.kill_count >= scores.hikill_count:
            scores.hikill_count = player.kill_count
        if player.current_score >= scores.high_score:
            scores.high_score = int(player.current_score)
        player.kill_count = 0
        player.current_score = player.current_score_og
    def update_display():
        hikillcount()
        hiscore()
        deathcount()
    if player.alive:
        if not boss_group:
            score()
        killcount()
        moneycount()
    if not player.alive and not scores.start_once:
        update()
        update_display()
        respawn_text()
        moneycount()
        main_menu_text()
    if scores.start_once:
        if (not player.alive) and (pygame.key.get_just_pressed()[pygame.K_LSHIFT] and
                                   pygame.key.get_just_pressed()[pygame.K_ESCAPE]):
            file = open('Data/savedata.txt', 'w')
            contents_to_save = {
                'money': scores.money,
                'high_score': scores.high_score,
                'kill_count': scores.hikill_count,
                'death_count': scores.death_count,

                'level_speed': shop.level_speed,
                "unlock_dash": shop.unlock_dash,
                "dash": shop.dash,
                'price_speed': shop.price_speed,
                'speed': shop.speed,

                'level_laser_speed': shop.level_laser_speed,
                'unlock_double_laser': shop.unlock_double_laser,
                'double_laser': shop.double_laser,
                'price_laser_speed': shop.price_laser_speed,
                'laser_speed': shop.laser_speed,

                'level_reload': shop.level_reload,
                'unlock_fullauto': shop.unlock_fullauto,
                'fullauto': shop.fullauto,
                'price_reload': shop.price_reload,
                'reload': shop.reload,

                'level_money': shop.level_money,
                'price_money': shop.price_money,
                'money_multiplier': scores.money_multiplier,

                'unlocked_1': shop.unlocked_1,
                'price_skin1': shop.price_skin1,
                'equipped_1': shop.equipped_1,

                'unlocked_2': shop.unlocked_2,
                'price_skin2': shop.price_skin2,
                'equipped_2': shop.equipped_2,

                'unlocked_3': shop.unlocked_3,
                'price_skin3': shop.price_skin3,
                'equipped_3': shop.equipped_3,

                'unlocked_4': shop.unlocked_4,
                'price_skin4': shop.price_skin4,
                'equipped_4': shop.equipped_4,

                "mute_music": scores.mute_music,
                "mute_sfx": scores.mute_sfx,

                "screen_width": 1280,
                "screen_hight": 720
            }
            json.dump(contents_to_save, file, indent=4)
            running = False
            file.close()
        if not (scores.reset_menu or scores.settings_menu):
            spawn_text()
            game_title()
            quit_text()
        #hover
        if not player.alive and (reset_rect.collidepoint((mouse_x,mouse_y))):
            screen.blit(reset_surf_hover, reset_rect_hover)
        else:
            screen.blit(reset_surf, reset_rect)
        if not player.alive and (settings_rect.collidepoint((mouse_x,mouse_y))):
            screen.blit(settings_surf_hover, settings_rect_hover)
        else:
            screen.blit(settings_surf, settings_rect)
        #click
        if not player.alive and (reset_rect.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            scores.reset_menu = not scores.reset_menu
            scores.settings_menu = False
        if not player.alive and (settings_rect.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            scores.settings_menu = not scores.settings_menu
            scores.reset_menu = False
    if not scores.start_once:
        scores.reset_menu = False
        scores.settings_menu = False
    if scores.reset_menu and scores.start_once:
        reset_window()
        if not player.alive and (button_cancel.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            scores.reset_menu = False
        if not player.alive and (button_ok.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            file = open('Data/savedata.txt', 'w')
            json.dump(erase_contents, file, indent=4)
            running = False
            file.close()
    if scores.settings_menu and scores.start_once:
        settings_window()
        if not player.alive and (button_ok2.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            if (scores.screen_width_c,scores.screen_height_c) != (screen_width,screen_height_):
                file = open('Data/savedata.txt', 'w')
                contents_to_save = {
                    'money': scores.money,
                    'high_score': scores.high_score,
                    'kill_count': scores.hikill_count,
                    'death_count': scores.death_count,

                    'level_speed': shop.level_speed,
                    "unlock_dash": shop.unlock_dash,
                    "dash": shop.dash,
                    'price_speed': shop.price_speed,
                    'speed': shop.speed,

                    'level_laser_speed': shop.level_laser_speed,
                    'unlock_double_laser': shop.unlock_double_laser,
                    'double_laser': shop.double_laser,
                    'price_laser_speed': shop.price_laser_speed,
                    'laser_speed': shop.laser_speed,

                    'level_reload': shop.level_reload,
                    'unlock_fullauto':shop.unlock_fullauto,
                    'fullauto':shop.fullauto,
                    'price_reload':shop.price_reload,
                    'reload':shop.reload,

                    'level_money':shop.level_money,
                    'price_money':shop.price_money,
                    'money_multiplier':scores.money_multiplier,

                    'unlocked_1':shop.unlocked_1,
                    'price_skin1':shop.price_skin1,
                    'equipped_1':shop.equipped_1,

                    'unlocked_2': shop.unlocked_2,
                    'price_skin2': shop.price_skin2,
                    'equipped_2': shop.equipped_2,

                    'unlocked_3': shop.unlocked_3,
                    'price_skin3': shop.price_skin3,
                    'equipped_3': shop.equipped_3,

                    'unlocked_4': shop.unlocked_4,
                    'price_skin4': shop.price_skin4,
                    'equipped_4': shop.equipped_4,

                    "mute_music": scores.mute_music,
                    "mute_sfx": scores.mute_sfx,

                    "screen_width": scores.screen_width_c,
                    "screen_hight": scores.screen_height_c
                }
                json.dump(contents_to_save, file, indent = 4)
                running = False
                file.close()
            else:
                scores.settings_menu = False
        if not player.alive and (button_cancel2.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            scores.settings_menu = False
            scores.screen_width_c,scores.screen_height_c = screen_width,screen_height
        if not player.alive and (button_sfx.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            scores.mute_sfx = not scores.mute_sfx
        if not player.alive and (button_music.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]):
            scores.mute_music = not scores.mute_music

    if scores.mute_sfx:
        mute_sfx_()
        if scores.settings_menu:
            pygame.draw.line(screen, (255, 71, 76),
                             (screen_width / 2 - (95*width_scale), screen_height / 2 + (100*hight_scale)),
                             (screen_width / 2 - (25*width_scale), screen_height / 2 + (20*hight_scale)), int(18*width_scale))
    if not scores.mute_sfx:
        unmute_sfx()
    if scores.mute_music:
        mute_music_()
        if scores.settings_menu:
            pygame.draw.line(screen, (255, 71, 76),
                             (screen_width / 2 + (15*width_scale), screen_height / 2 + (100*hight_scale)),
                             (screen_width / 2 + (80*width_scale), screen_height / 2 + (20*hight_scale)), int(18*width_scale))
    if not scores.mute_music:
        unmute_music()
def kill_onscreen():
    for meteor in meteor_group:
        meteor.kill()
    for kanye in evil_ye:
        kanye.kill()
    for ship in ship_group:
        ship.kill()
        if difficulty.ship_spawn >= 0:
            difficulty.ship_spawn -= 1
    for nuke in nuke_group:
        nuke.kill()
    for doublex in doublexdrop_group:
        doublex.kill()
    for teddie_drop in teddiedrop_group:
        teddie_drop.kill()
    for laser in laser_group:
        laser.kill()
    for ship_laser in ship_laser_group:
        ship_laser.kill()
    for coins in coins_group:
        coins.kill()
    for boss in boss_group:
        boss.kill()
        scores.boss_alive = False
        scores.n = 1
    for laserbeam in boss_laserbeam_group:
        laserbeam.kill()
def play_again():
    pygame.mixer.Sound.stop(mainmenu_music)
    pygame.mixer.Sound.stop(ye_spawn)
    pygame.mixer.Sound.stop(diddy_death_sound)
    pygame.mixer.Sound.stop(game_music)
    pygame.mixer.Sound.stop(minecraft_boom)
    pygame.mixer.Sound.stop(minecraft_boom2)
    pygame.mixer.Sound.stop(minecraft_boom3)
    pygame.mixer.Sound.play(game_music, -1)
    global player
    player = Player(all_sprites)
    if shop.equipped_4:
        pygame.mixer.Sound.play(lebron_spawn_sound)
    pygame.time.set_timer(meteor_event, 500)
    pygame.time.set_timer(kanye_event, 10000)
    pygame.time.set_timer(ship_event, 25000)
    difficulty.ye = 13000
    difficulty.ship = 8000
    difficulty.meteor = 500

    difficulty.ship_spawn = 0

    scores.boss_alive = False
    scores.n = 1

    kill_onscreen()
def mute_sfx_():
    pygame.mixer.Sound.set_volume(explosion_sound, 0)
    pygame.mixer.Sound.set_volume(laser_sound, 0)
    pygame.mixer.Sound.set_volume(shotgun_sound, 0)
    pygame.mixer.Sound.set_volume(damage_sound, 0)
    pygame.mixer.Sound.set_volume(ye_spawn, 0)
    pygame.mixer.Sound.set_volume(ye_death, 0)
    pygame.mixer.Sound.set_volume(teddie_drop_sound, 0)
    pygame.mixer.Sound.set_volume(doublex_sound, 0)
    pygame.mixer.Sound.set_volume(coins_sound, 0)
    pygame.mixer.Sound.set_volume(fweah_sound, 0)
    pygame.mixer.Sound.set_volume(lebron_spawn_sound, 0)
    pygame.mixer.Sound.set_volume(nuke_sound, 0)
    pygame.mixer.Sound.set_volume(wrong_sound, 0)
    pygame.mixer.Sound.set_volume(diddy_spawn_sound, 0)
    pygame.mixer.Sound.set_volume(boing_sound, 0)
    pygame.mixer.Sound.set_volume(laserbeam_sound, 0)
    pygame.mixer.Sound.set_volume(diddy_death_sound, 0)
    pygame.mixer.Sound.set_volume(diamond_sound, 0)
    pygame.mixer.Sound.set_volume(minecraft_boom, 0)
    pygame.mixer.Sound.set_volume(minecraft_boom2, 0)
    pygame.mixer.Sound.set_volume(minecraft_boom3, 0)
def unmute_sfx():
    pygame.mixer.Sound.set_volume(explosion_sound, 0.3)
    pygame.mixer.Sound.set_volume(laser_sound, 0.3)
    pygame.mixer.Sound.set_volume(shotgun_sound, 0.75)
    pygame.mixer.Sound.set_volume(damage_sound, 2)
    pygame.mixer.Sound.set_volume(ye_spawn, 0.4)
    pygame.mixer.Sound.set_volume(ye_death, 0.5)
    pygame.mixer.Sound.set_volume(teddie_drop_sound, 0.2)
    pygame.mixer.Sound.set_volume(doublex_sound, 0.65)
    pygame.mixer.Sound.set_volume(coins_sound, 0.4)
    pygame.mixer.Sound.set_volume(fweah_sound, 0.4)
    pygame.mixer.Sound.set_volume(lebron_spawn_sound, 0.65)
    pygame.mixer.Sound.set_volume(nuke_sound, 1)
    pygame.mixer.Sound.set_volume(wrong_sound, 1)
    pygame.mixer.Sound.set_volume(diddy_spawn_sound, 0.85)
    pygame.mixer.Sound.set_volume(boing_sound, 0.6)
    pygame.mixer.Sound.set_volume(laserbeam_sound, 0.6)
    pygame.mixer.Sound.set_volume(diddy_death_sound, 1)
    pygame.mixer.Sound.set_volume(diamond_sound, 0.7)
    pygame.mixer.Sound.set_volume(minecraft_boom, 0.6)
    pygame.mixer.Sound.set_volume(minecraft_boom2, 0.6)
    pygame.mixer.Sound.set_volume(minecraft_boom3, 0.6)
def mute_music_():
    pygame.mixer.Sound.set_volume(game_music, 0)
    pygame.mixer.Sound.set_volume(mainmenu_music, 0)
    pygame.mixer.Sound.set_volume(ds3_music, 0)
def unmute_music():
    pygame.mixer.Sound.set_volume(game_music, 0.3)
    pygame.mixer.Sound.set_volume(mainmenu_music, 0.4)
    pygame.mixer.Sound.set_volume(ds3_music, 0.6)

#pygame setup
pygame.init()


#save file
file = open('Data/savedata.txt', 'r')
content = json.load(file)
erase_contents = {
    "money": 0,
    "high_score": 0,
    "kill_count": 0,
    "death_count": 0,
    "level_speed": 0,
    "unlock_dash": False,
    "dash": False,
    "price_speed": 100,
    "speed": 550,
    "level_laser_speed": 0,
    "unlock_double_laser": False,
    "double_laser": False,
    "price_laser_speed": 100,
    "laser_speed": 400,
    "level_reload": 0,
    "unlock_fullauto": False,
    "fullauto": False,
    "price_reload": 100,
    "reload": 500,
    "level_money": 0,
    "price_money": 1000,
    "money_multiplier": 1,
    "unlocked_1": True,
    "price_skin1": 0,
    "equipped_1": True,
    "unlocked_2": False,
    "price_skin2": 10000,
    "equipped_2": False,
    "unlocked_3": False,
    "price_skin3": 1000000,
    "equipped_3": False,
    "unlocked_4": False,
    "price_skin4": 10000000,
    "equipped_4": False,
    "mute_music": False,
    "mute_sfx": False,

    "screen_width": 1280,
    "screen_hight": 720
}

screen_info = pygame.display.Info()

screen_width_ = screen_info.current_w
screen_height_ = screen_info.current_h

screen_ratio = screen_width_/screen_height_

ratios = {
    "16:9": 16/9,
    "16:10": 16/10,
    "4:3": 4/3,
    "1:1": 1/1,
    "5:4": 5/4,
    "21:9": 21/9,
    "32:9": 32/9,
    "3:2": 3/2
}
ratio_error = 0.01

for ratio_name, standard_ratio in ratios.items():
    if abs(screen_ratio - standard_ratio) < ratio_error:
        if ratio_name == "16:9":
            rx,ry = 16,9
        elif ratio_name == "16:10":
            rx,ry = 16,10
        elif ratio_name == "4:3":
            rx,ry = 4,3
        elif ratio_name == "1:1":
            rx,ry = 1,1
        elif ratio_name == "5:4":
            rx,ry = 5,4
        elif ratio_name == "21:9":
            rx,ry = 21,9
        elif ratio_name == "32:9":
            rx, ry = 32,9
        elif ratio_name == "3:2":
            rx,ry = 3,2
        break
    else:
        rx,ry = None,None

print((screen_ratio, rx, ry))

screen_width = content["screen_width"]
screen_height = content["screen_hight"]

width_scale = screen_width/1280
hight_scale = screen_height/720

mouse_width = screen_width/screen_width_
mouse_hight = screen_height/screen_height_

speed_scale = ((width_scale+hight_scale)/2)

screen = pygame.display.set_mode((screen_width, screen_height), vsync=1, flags=pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Bouncing Kanye")
running = True

#imports
diddy1_surf = pygame.image.load(join("Data", 'diddy1.png')).convert_alpha()
diddy1_surf = pygame.transform.smoothscale(diddy1_surf, (int(diddy1_surf.get_width()*0.8*width_scale),
                                                         int(diddy1_surf.get_height()*0.8*hight_scale)))
disco_surf = pygame.image.load(join("Data", "discoball.png")).convert_alpha()
disco_surf = pygame.transform.smoothscale(disco_surf, (int(disco_surf.get_width()*0.06*width_scale),
                                                         int(disco_surf.get_height()*0.06*hight_scale)))
disco_rect = disco_surf.get_frect(center=(525 * width_scale, 225 * hight_scale))
babyoil_surf = pygame.image.load(join("Data", "babyoil.webp")).convert_alpha()
babyoil_surf = pygame.transform.smoothscale(babyoil_surf, (int(babyoil_surf.get_width()*0.2*width_scale),
                                                         int(babyoil_surf.get_height()*0.2*hight_scale)))
laserbeam_surf = pygame.image.load(join("Data", "laser.png")).convert_alpha()
laserbeam_surf = pygame.transform.smoothscale(laserbeam_surf, (int(laserbeam_surf.get_width()*200*width_scale),
                                                         int(laserbeam_surf.get_height()*0.1*hight_scale)))
laserbeam_surf = pygame.transform.invert(laserbeam_surf)
info_surf = pygame.image.load(join('Data', 'info.png')).convert_alpha()
info_surf = pygame.transform.smoothscale(info_surf,(int(info_surf.get_width() * 0.05 * width_scale),
                                                       int(info_surf.get_height() * 0.05 * hight_scale)))
info_rect = info_surf.get_frect(center=(screen_width / 2 , screen_height/2 + (150*hight_scale)))
info_surf = pygame.transform.invert(info_surf)
info_surf_hover = pygame.transform.smoothscale(info_surf, (int(info_surf.get_width() * 1.2 * width_scale),
                                                       int(info_surf.get_height() * 1.2 * hight_scale)))
info_rect_hover = info_surf_hover.get_frect(center=(screen_width / 2 , screen_height/2 + (150*hight_scale)))

sfx_surf = pygame.image.load(join('Data', 'sfx.png')).convert_alpha()
sfx_surf = pygame.transform.smoothscale(sfx_surf,(int(sfx_surf.get_width() * 0.05 * width_scale),
                                                       int(sfx_surf.get_height() * 0.05 * hight_scale)))
sfx_rect = sfx_surf.get_frect(center=(screen_width / 2 - (60*width_scale), screen_height / 2 + (65*hight_scale)))
sfx_surf = pygame.transform.invert(sfx_surf)
sfx_surf_hover = pygame.transform.smoothscale(sfx_surf, (int(sfx_surf.get_width() * 1.1 * width_scale),
                                                       int(sfx_surf.get_height() * 1.1 * hight_scale)))
sfx_rect_hover = sfx_surf_hover.get_frect(center=(screen_width / 2 - (90*width_scale), screen_height / 2 + (65*hight_scale)))

music_surf = pygame.image.load(join('Data', 'music.png')).convert_alpha()
music_surf = pygame.transform.smoothscale(music_surf,(int(music_surf.get_width() * 0.05 * width_scale),
                                                       int(music_surf.get_height() * 0.05 * hight_scale)) )
music_rect = music_surf.get_frect(center=(screen_width / 2 + (50*width_scale), screen_height / 2 + (65*hight_scale)))
music_surf = pygame.transform.invert(music_surf)
settings_surf = pygame.image.load(join('Data', 'settings.png')).convert_alpha()
settings_surf = pygame.transform.smoothscale(settings_surf,(int(settings_surf.get_width() * 0.5 * width_scale),
                                                       int(settings_surf.get_height() * 0.5 * hight_scale)) )
settings_rect = settings_surf.get_frect(center=((100*width_scale), (650*hight_scale)))
settings_surf = pygame.transform.invert(settings_surf)
settings_surf_hover = pygame.transform.smoothscale(settings_surf, (int(settings_surf.get_width() * 1.1 * width_scale),
                                                       int(settings_surf.get_height() * 1.1 * hight_scale)))
settings_rect_hover = settings_surf_hover.get_frect(center=((100*width_scale), (650*hight_scale)))

reset_surf = pygame.image.load(join('Data', 'reset.png')).convert_alpha()
reset_surf = pygame.transform.smoothscale(reset_surf, (int(reset_surf.get_width() * 0.5 * width_scale),
                                                       int(reset_surf.get_height() * 0.5 * hight_scale)))
reset_rect = reset_surf.get_frect(center=((1180 * width_scale), (650 * hight_scale)))
reset_surf = pygame.transform.invert(reset_surf)
reset_surf_hover = pygame.transform.smoothscale(reset_surf, (int(reset_surf.get_width() * 1.1 * width_scale),
                                                             int(reset_surf.get_height() * 1.1 * hight_scale)))
reset_rect_hover = reset_surf_hover.get_frect(center=((1180 * width_scale), (650 * hight_scale)))

star_surf = pygame.image.load(join('Data', 'yellow star.webp')).convert_alpha()
star_surf = pygame.transform.scale(star_surf, (int(star_surf.get_width() * random.uniform(0.01, 0.05)*width_scale),
                                               int(star_surf.get_height() * random.uniform(0.01, 0.05)*hight_scale)))
laser_surf = pygame.image.load(join('Data', 'laser.png')).convert_alpha()
laser_surf = pygame.transform.smoothscale(laser_surf, (int(laser_surf.get_width()*width_scale),
                                                       int(laser_surf.get_height()*hight_scale)))
player_surf = pygame.image.load(join('Data', 'suit ye.png')).convert_alpha()
player_surf = pygame.transform.smoothscale(player_surf, (int(player_surf.get_width()*0.11 * width_scale),
                                                         int(player_surf.get_height() *0.11* hight_scale)))
window_image = pygame.image.load(join('Data', 'imageedit_2_2521105736.png')).convert_alpha()

skin_lebron = pygame.image.load(join("Data", "lebron.WEBP")).convert_alpha()
skin_lebron = pygame.transform.smoothscale(skin_lebron, (int(skin_lebron.get_width() * 0.131 * width_scale),
                                                         int(skin_lebron.get_height() * 0.133 * hight_scale)))
skin_cool_ye = pygame.image.load(join('Data', 'cool_ye.PNG')).convert_alpha()
skin_cool_ye = pygame.transform.smoothscale(skin_cool_ye, (int(skin_cool_ye.get_width() * 0.128 * width_scale),
                                                           int(skin_cool_ye.get_height() * 0.128 * hight_scale)))
skin_kanye = pygame.image.load(join('Data', 'KANYE.PNG')).convert_alpha()
skin_kanye = pygame.transform.smoothscale(skin_kanye, (int(skin_kanye.get_width() * 0.1485 * width_scale),
                                                       int(skin_kanye.get_height() * 0.15 * hight_scale)))
skin_angry_ye = pygame.image.load(join('Data', 'angry_ye.PNG')).convert_alpha()
skin_angry_ye = pygame.transform.smoothscale(skin_angry_ye, (int(skin_angry_ye.get_width() * 0.133),
                                                             int(skin_angry_ye.get_height() * 0.14)))
skull_surf = pygame.image.load(join('Data', 'skull_1.png')).convert_alpha()
skull_surf = pygame.transform.smoothscale(skull_surf, (int(skull_surf.get_width() * 0.07 * width_scale),
                                                       int(skull_surf.get_height() * 0.07 * hight_scale)))
skull_surf = pygame.transform.invert(skull_surf)
clock_surf = pygame.image.load(join('Data', 'clock_.png')).convert_alpha()
clock_surf = pygame.transform.smoothscale(clock_surf, (int(clock_surf.get_width() * 0.085 *width_scale),
                                                       int(clock_surf.get_height() * 0.08*hight_scale)))
coinye_surf = pygame.image.load(join('Data', 'coinye_1.png')).convert_alpha()
coinye_surf = pygame.transform.smoothscale(coinye_surf, (int(coinye_surf.get_width() * 0.13*width_scale),
                                                         int(coinye_surf.get_height() * 0.13*hight_scale)))
coinye_b_surf = pygame.image.load(join('Data', 'coinye_b.png')).convert_alpha()
coinye_b_surf = pygame.transform.smoothscale(coinye_b_surf, (int(coinye_b_surf.get_width() * 0.175*width_scale),
                                                             int(coinye_b_surf.get_height() * 0.175*hight_scale)))
coinye_s_surf = pygame.image.load(join('Data', 'coinye_s.png')).convert_alpha()
coinye_s_surf = pygame.transform.smoothscale(coinye_s_surf, (int(coinye_s_surf.get_width() * 0.07*width_scale),
                                                             int(coinye_s_surf.get_height() * 0.07*hight_scale)))
coin_ui_surf = pygame.image.load(join('Data', 'coin_ui.png')).convert_alpha()
coin_ui_surf = pygame.transform.smoothscale(coin_ui_surf, (int(coin_ui_surf.get_width() * 0.07 * width_scale),
                                                           int(coin_ui_surf.get_height() * 0.07 * hight_scale)))
diamond_surf = pygame.image.load(join('Data', 'diamond.png')).convert_alpha()
diamond_surf = pygame.transform.smoothscale(diamond_surf, (int(diamond_surf.get_width() * 0.15 * width_scale),
                                                           int(diamond_surf.get_height() * 0.15* hight_scale)))
explosion_frames = [pygame.image.load(join('Data', 'explosion', f'{i}.png')).convert_alpha() for i in range(21)]
laser_sound = pygame.mixer.Sound(join('Data', 'audio', 'laser.wav'))
explosion_sound = pygame.mixer.Sound(join('Data', 'audio', 'explosion.wav'))
game_music = pygame.mixer.Sound(join('Data', 'audio', 'game_music.wav'))
mainmenu_music = pygame.mixer.Sound(join('Data', 'audio', 'geometry-dash-menu.mp3'))
damage_sound = pygame.mixer.Sound(join('Data', 'audio', 'damage.mp3'))
ye_spawn = pygame.mixer.Sound(join('Data', 'audio', 'kanye-west-jetpack-joyride.mp3'))
ye_death = pygame.mixer.Sound(join('Data', 'audio', 'he-he-he-ha-clash-royale-deep-fried.mp3'))
nuke_sound = pygame.mixer.Sound(join('Data', 'audio', 'kaboom.mp3'))
teddie_drop_sound = pygame.mixer.Sound(join('Data', 'audio', 'iwonder-3.mp3'))
doublex_sound = pygame.mixer.Sound(join('Data', 'audio', 'double-kill.mp3'))
coins_sound = pygame.mixer.Sound(join('Data', 'audio', 'cash-point.mp3'))
fweah_sound = pygame.mixer.Sound(join('Data', 'audio', 'carti what-[AudioTrimmer.com].mp3'))
wrong_sound = pygame.mixer.Sound(join('Data', 'audio', 'wronganswer-37702.mp3'))
shotgun_sound = pygame.mixer.Sound(join('Data', 'audio', 'shotgun.mp3'))
lebron_spawn_sound = pygame.mixer.Sound(join("Data", 'audio', 'lebron-james.mp3'))
diddy_spawn_sound = pygame.mixer.Sound(join('Data', 'audio', 'bossspawn.mp3'))
boing_sound = pygame.mixer.Sound(join("Data", "audio", "boing.mp3"))
laserbeam_sound = pygame.mixer.Sound(join("Data", "audio", "laserbeam.mp3"))
diddy_death_sound = pygame.mixer.Sound(join("Data", "audio", 'diddy_death.mp3'))
ds3_music = pygame.mixer.Sound(join("Data", "audio", 'ds3.mp3'))
diamond_sound = pygame.mixer.Sound(join("Data", "audio", "diamond.mp3"))
minecraft_boom = pygame.mixer.Sound(join("Data", "audio", "minecraft-explosion-green-screen-[AudioTrimmer.com].mp3"))
minecraft_boom2 = pygame.mixer.Sound(join("Data", "audio", "boom2.mp3"))
minecraft_boom3 = pygame.mixer.Sound(join("Data", "audio", "boom3.mp3"))

#audio
pygame.mixer.Sound.set_volume(explosion_sound, 0.3)
pygame.mixer.Sound.set_volume(laser_sound, 0.3)
pygame.mixer.Sound.set_volume(shotgun_sound, 0.75)
pygame.mixer.Sound.set_volume(damage_sound, 2)
pygame.mixer.Sound.set_volume(ye_spawn, 0.4)
pygame.mixer.Sound.set_volume(ye_death, 0.5)
pygame.mixer.Sound.set_volume(teddie_drop_sound, 0.2)
pygame.mixer.Sound.set_volume(doublex_sound, 0.65)
pygame.mixer.Sound.set_volume(coins_sound, 0.4)
pygame.mixer.Sound.set_volume(fweah_sound, 0.4)
pygame.mixer.Sound.set_volume(lebron_spawn_sound, 0.65)
pygame.mixer.Sound.set_volume(nuke_sound, 1)
pygame.mixer.Sound.set_volume(wrong_sound, 1)
pygame.mixer.Sound.set_volume(diddy_spawn_sound, 0.85)
pygame.mixer.Sound.set_volume(boing_sound, 0.6)
pygame.mixer.Sound.set_volume(laserbeam_sound, 0.6)
pygame.mixer.Sound.set_volume(diddy_death_sound, 1)
pygame.mixer.Sound.set_volume(diamond_sound, 0.7)
pygame.mixer.Sound.set_volume(minecraft_boom, 0.6)
pygame.mixer.Sound.set_volume(minecraft_boom2, 0.6)
pygame.mixer.Sound.set_volume(minecraft_boom3, 0.6)
#game music
pygame.mixer.Sound.set_volume(game_music,0.3)
pygame.mixer.Sound.set_volume(mainmenu_music, 0.4)
pygame.mixer.Sound.set_volume(ds3_music, 0.6)
pygame.mixer.Sound.play(mainmenu_music, -1)
#channel
pygame.mixer.set_num_channels(16)
channel2 = pygame.mixer.find_channel()
#group sprite and instance
all_sprites = pygame.sprite.Group()
star_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()
ship_group = pygame.sprite.Group()
evil_ye = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
ship_laser_group = pygame.sprite.Group()
nuke_group = pygame.sprite.Group()
teddiedrop_group = pygame.sprite.Group()
teddie_group = pygame.sprite.Group()
doublexdrop_group = pygame.sprite.Group()
countdown_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
boss_laserbeam_group = pygame.sprite.Group()
oil_group = pygame.sprite.Group()
boss_death_group = pygame.sprite.Group()
for i in range(45):
    x = random.uniform(0.01, 0.04)
    star_surf = pygame.image.load(join('Data', 'white-star.png')).convert_alpha()
    star_surf = pygame.transform.scale(star_surf, (int(star_surf.get_width() * x),
                                                   int(star_surf.get_height() * x)))
    star = Star(star_group, ((random.randint(0, screen_width)), (random.randint(0, screen_height))), star_surf)
shop = Shop()
player = Player(all_sprites)
player.alive = False
player.kill()
scores = Scores_class()
difficulty = DynamicDiffuclity()

pygame.display.set_icon(window_image)
#custom event
meteor_event = pygame.event.custom_type()
kanye_event = pygame.event.custom_type()
ship_event = pygame.event.custom_type()
save_event = pygame.event.custom_type()

pygame.time.set_timer(meteor_event, 500)
pygame.time.set_timer(save_event, 600000)
#pygame.time.set_timer(kanye_event, 10000)
#pygame.time.set_timer(ship_event, 25000)

#gameloop
while running:
    dt = clock.tick(60) / 1000  # limits FPS to 60

    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]

    screen_info = pygame.display.Info()

    screen_width_ = screen_info.current_w
    screen_height_ = screen_info.current_h
    #event loop
    screen.fill((33,44,73))
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (scores.start_once and not (scores.settings_menu or scores.reset_menu)
                                           and (scores.quittext_rect.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0])):
            #save
            file = open('Data/savedata.txt', 'w')
            contents_to_save = {
                'money': scores.money,
                'high_score': scores.high_score,
                'kill_count': scores.hikill_count,
                'death_count': scores.death_count,

                'level_speed': shop.level_speed,
                "unlock_dash": shop.unlock_dash,
                "dash": shop.dash,
                'price_speed': shop.price_speed,
                'speed': shop.speed,

                'level_laser_speed': shop.level_laser_speed,
                'unlock_double_laser': shop.unlock_double_laser,
                'double_laser': shop.double_laser,
                'price_laser_speed': shop.price_laser_speed,
                'laser_speed': shop.laser_speed,

                'level_reload': shop.level_reload,
                'unlock_fullauto':shop.unlock_fullauto,
                'fullauto':shop.fullauto,
                'price_reload':shop.price_reload,
                'reload':shop.reload,

                'level_money':shop.level_money,
                'price_money':shop.price_money,
                'money_multiplier':scores.money_multiplier,

                'unlocked_1':shop.unlocked_1,
                'price_skin1':shop.price_skin1,
                'equipped_1':shop.equipped_1,

                'unlocked_2': shop.unlocked_2,
                'price_skin2': shop.price_skin2,
                'equipped_2': shop.equipped_2,

                'unlocked_3': shop.unlocked_3,
                'price_skin3': shop.price_skin3,
                'equipped_3': shop.equipped_3,

                'unlocked_4': shop.unlocked_4,
                'price_skin4': shop.price_skin4,
                'equipped_4': shop.equipped_4,

                "mute_music": scores.mute_music,
                "mute_sfx": scores.mute_sfx,

                "screen_width": screen_width,
                "screen_hight": screen_height
            }
            json.dump(contents_to_save, file, indent = 4)
            #close
            running = False
            file.close()
        if event.type == save_event:
            file = open('Data/savedata.txt', 'w')
            contents_to_save = {
                'money': scores.money,
                'high_score': scores.high_score,
                'kill_count': scores.hikill_count,
                'death_count': scores.death_count,

                'level_speed': shop.level_speed,
                "unlock_dash": shop.unlock_dash,
                "dash": shop.dash,
                'price_speed': shop.price_speed,
                'speed': shop.speed,

                'level_laser_speed': shop.level_laser_speed,
                'unlock_double_laser': shop.unlock_double_laser,
                'double_laser': shop.double_laser,
                'price_laser_speed': shop.price_laser_speed,
                'laser_speed': shop.laser_speed,

                'level_reload': shop.level_reload,
                'unlock_fullauto':shop.unlock_fullauto,
                'fullauto':shop.fullauto,
                'price_reload':shop.price_reload,
                'reload':shop.reload,

                'level_money':shop.level_money,
                'price_money':shop.price_money,
                'money_multiplier':scores.money_multiplier,

                'unlocked_1':shop.unlocked_1,
                'price_skin1':shop.price_skin1,
                'equipped_1':shop.equipped_1,

                'unlocked_2': shop.unlocked_2,
                'price_skin2': shop.price_skin2,
                'equipped_2': shop.equipped_2,

                'unlocked_3': shop.unlocked_3,
                'price_skin3': shop.price_skin3,
                'equipped_3': shop.equipped_3,

                'unlocked_4': shop.unlocked_4,
                'price_skin4': shop.price_skin4,
                'equipped_4': shop.equipped_4,

                "mute_music": scores.mute_music,
                "mute_sfx": scores.mute_sfx,

                "screen_width": screen_width,
                "screen_hight": screen_height
            }
            json.dump(contents_to_save, file, indent = 4)
            file = open('Data/savedata.txt', 'r')
        #spawn enemy
        if event.type == meteor_event:
            meteor = Meteor((all_sprites, meteor_group))
            difficulty.update_meteor()
        if event.type == kanye_event:
            kanye = EvilYe((all_sprites, evil_ye))
            pygame.mixer.Sound.play(ye_spawn)
            difficulty.update_ye()
        if event.type == ship_event:
            if difficulty.ship_spawn < 3:
                swift = Ship((all_sprites, ship_group))
                difficulty.ship_spawn += 1
            difficulty.update_ship()
        #start/restart
        if (not player.alive and (scores.start_once and not (scores.settings_menu or scores.reset_menu) and
                                  ((pygame.key.get_just_pressed()[pygame.K_SPACE] or
                                                        (scores.spawntext_rect.collidepoint((mouse_x,mouse_y)) and
                                                         pygame.mouse.get_just_pressed()[0]))) or
                (not scores.start_once and (pygame.key.get_just_pressed()[pygame.K_r] or
                                            (scores.respawntext_rect.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]))))):
            play_again()
        if not player.alive and (not scores.start_once and( pygame.key.get_just_pressed()[pygame.K_TAB] or (scores.mainmenutext_rect.collidepoint((mouse_x,mouse_y)) and pygame.mouse.get_just_pressed()[0]))):
            scores.start_once = True
            pygame.mixer.Sound.stop(ye_death)
            pygame.mixer.Sound.stop(diddy_death_sound)
            pygame.mixer.Sound.stop(minecraft_boom)
            pygame.mixer.Sound.stop(minecraft_boom2)
            pygame.mixer.Sound.stop(minecraft_boom3)
            pygame.mixer.Sound.play(mainmenu_music, -1)
            pygame.time.set_timer(meteor_event, 500)
            for boss in boss_group:
                boss.kill()
                scores.boss_alive = False
                scores.n = 1
    #update
    star_group.update(dt)
    all_sprites.update(dt)
    for boss in boss_group:
        boss_laserbeam_group.update(dt)
    collisions()
    shop.update()
    #draw
    star_group.draw(screen)
    all_sprites.draw(screen)
    for boss in boss_group:
        boss_laserbeam_group.draw(screen)
        if (not boss.spawn) and (boss.laserbeam_phase) and (not boss.laserbeam_starter):
            if not (boss.laserbeam_return):
                screen.blit(disco_surf, disco_rect)
    countdown_group.draw(screen)
    shop.draw()
    #clock level
    countdown_group.update(dt)
    display_ui()

    #diddy
    spawn_boss()
    for boss in boss_group:
        if not boss.spawn and (player.alive):
            health_bar()
            #print(boss.max_health)

    #print(difficulty.meteor)
    #print(difficulty.ye)
    #print(difficulty.ship)
    #print(difficulty.ship_spawn)

    screen.fill((0,0,0), (screen_width,0,screen_width_,screen_height_))
    screen.fill((0,0,0), (0,screen_height,screen_width_,screen_height_))

    #update display
    pygame.display.update()

pygame.quit()

