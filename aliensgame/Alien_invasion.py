#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:34:08 2019 

@author: christynataliaj
"""
import sys

import pygame

from settings import Settings

from game_stats import GameStats

from scoreboard import Scoreboard 

from button import Button

from ship import Ship

import game_functions as gf

from pygame.sprite import Group





def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play") 
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    
    gf.create_fleet(ai_settings, screen,ship, aliens)
    
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb, ship, aliens,bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings,screen, stats, sb, ship,aliens, bullets, play_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
                
        pygame.display.flip()
run_game()