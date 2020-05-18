import pygame
import random
import variable
import numpy
import funcoes
import assets
from classes import *
from os import path

pygame.init()

window = pygame.display.set_mode((variable.RESOLUTION))
pygame.display.set_caption('Super Jaca Man')

assets = assets.load_assets()

img_dir = path.join(path.dirname(__file__), 'img')

player_sheet = pygame.image.load(path.join(img_dir, 'bomberman_sprites.png')).convert_alpha()
player = Character(player_sheet)


all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_jacas = pygame.sprite.Group()

fixed_wall_sprites = pygame.sprite.Group()

pos = funcoes.block_location(variable.MAP, variable.DIVISIONS, variable.RESOLUTION)
for each in pos:
    wall = Fixed_wall(assets, each)
    all_sprites.add(wall)
    fixed_wall_sprites.add(wall)

game = True

clock = pygame.time.Clock()
FPS = 10
# looooop principal
while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        # player movement
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:   
                #EXPLODE TUDO E CAGA GERAL DE JACA 
                player.drop_bomb(assets, all_sprites, all_jacas)
            
            if event.key == pygame.K_LEFT:
                player.state = variable.LEFT
                player.speedx -= variable.WIDTH_SQUARE/2
                
            if event.key == pygame.K_RIGHT:
                player.state = variable.RIGHT
                player.speedx += variable.WIDTH_SQUARE/2

            if event.key == pygame.K_UP:
                player.state = variable.UP
                player.speedy -= variable.WIDTH_SQUARE/2
            
            if event.key == pygame.K_DOWN:
                player.state = variable.DOWN
                player.speedy += variable.WIDTH_SQUARE/2
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.state = variable.STILL
                player.speedx += variable.WIDTH_SQUARE/2

            if event.key == pygame.K_RIGHT:
                player.state = variable.STILL
                player.speedx -= variable.WIDTH_SQUARE/2

            if event.key == pygame.K_UP:
                player.state = variable.STILL
                player.speedy += variable.WIDTH_SQUARE/2

            if event.key == pygame.K_DOWN:
                player.state = variable.STILL
                player.speedy -= variable.WIDTH_SQUARE/2

    all_sprites.update()

    for wall in fixed_wall_sprites:
        if funcoes.cant_pass(player, wall):
            player.rect.y -= player.speedy 
            player.rect.x -= player.speedx

    window.fill((155, 220, 72))
    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()
