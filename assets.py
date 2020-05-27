import pygame
import variable
from os import path

PLAYER_IMG = 'player_img'
SQUARE_IMG = 'square_img'
JACA_ABERTA_IMG = "jaca_aberta_img"
JACA_FECHADA_IMG = "jaca_fechada_img"
EXPLOSAO = 'explojaca'
img_dir = path.join(path.dirname(__file__), 'img')

def load_assets():
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load('img/personagem.png').convert_alpha()
    assets[PLAYER_IMG] = pygame.transform.scale(assets['player_img'], (variable.PLAYER_WIDTH, variable.PLAYER_HEIGHT))

    assets[SQUARE_IMG] = pygame.image.load('img/bloco.png').convert_alpha()
    assets[SQUARE_IMG] = pygame.transform.scale(assets['square_img'], variable.SQUARE_DIMENSIONS)

    assets[JACA_ABERTA_IMG] = pygame.image.load('img/jaca_aberta.png').convert_alpha()
    assets[JACA_ABERTA_IMG] = pygame.transform.scale(assets['jaca_aberta_img'], variable.SQUARE_DIMENSIONS)

    assets[JACA_FECHADA_IMG] = pygame.image.load('img/JACA_FECHADA.png').convert_alpha()
    assets[JACA_FECHADA_IMG] = pygame.transform.scale(assets['jaca_fechada_img'], variable.SQUARE_DIMENSIONS)

    assets[EXPLOSAO] = pygame.image.load('img/explojaca.png').convert_alpha()
    assets[EXPLOSAO] = pygame.transform.scale(assets['explojaca'], variable.EXPLO_DIMENSIONS)

    return assets


