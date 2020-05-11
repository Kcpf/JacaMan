import pygame
import variable

PLAYER_IMG = 'player_img'

def load_assets():
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load('assets/img/personagem.png').convert_alpha()
    assets[PLAYER_IMG] = pygame.transform.scale(assets['player_img'], (variable.PLAYER_WIDTH, variable.PLAYER_HEIGHT))
    return assets
    