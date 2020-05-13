import pygame 
import random
import variable
import numpy
import funcoes
import assets
from classes import *


pygame.init()

window = pygame.display.set_mode((variable.RESOLUTION))

pygame.display.set_caption('Super Jaca Man')
assets = assets.load_assets()

player = Character(assets)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

pos = funcoes.block_location(variable.MAP,variable.DIVISIONS,variable.RESOLUTION)
for each in pos: 
    all_sprites.add(Fixed_wall(assets, each))

game = True

clock = pygame.time.Clock()
FPS = 10

#looooop principal 
while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    
        #player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedx -= variable.WIDTH_SQUARE/2
            if event.key == pygame.K_RIGHT:
                player.speedx += variable.WIDTH_SQUARE/2
            if event.key == pygame.K_UP:
                player.speedy -= variable.WIDTH_SQUARE/2
            if event.key == pygame.K_DOWN:
                player.speedy += variable.WIDTH_SQUARE/2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.speedx += variable.WIDTH_SQUARE/2
            if event.key == pygame.K_RIGHT:
                player.speedx -= variable.WIDTH_SQUARE/2
            if event.key == pygame.K_UP:
                player.speedy += variable.WIDTH_SQUARE/2
            if event.key == pygame.K_DOWN:
                player.speedy -= variable.WIDTH_SQUARE/2
    
    all_sprites.update()
    
    window.fill((155, 220, 72)) 
    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()
