import sys

import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,
                                      ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船
    ship = Ship(ai_setting, screen)
    # 储存子弹的编组
    bullets = Group()

    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_setting, screen, ship, bullets)


run_game()
