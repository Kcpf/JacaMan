import pygame
import random
import variable
import numpy
import funcoes
import assets
from classes import *
from os import path
pygame.init()

#Define configurações de tela
window = pygame.display.set_mode((variable.RESOLUTION))
pygame.display.set_caption('Super Jaca Man')

#Carrega todos os assets
assets = assets.load_assets()
img_dir = path.join(path.dirname(__file__), 'img')
player_sheet = pygame.image.load(path.join(img_dir, 'bomberman_sprites.png')).convert_alpha()

#Inicializa classes
p1 = Character(player_sheet)
p2 = Character(player_sheet)

#Grupos de pepsi
all_sprites = pygame.sprite.Group()
all_jacas = pygame.sprite.Group()
fixed_wall_sprites = pygame.sprite.Group()
all_explosions = pygame.sprite.Group()
all_players = pygame.sprite.Group()
removable_wall_sprites = pygame.sprite.Group()
all_walls = pygame.sprite.Group()

all_sprites.add(p1)
all_sprites.add(p2)
all_players.add(p1)
all_players.add(p2)

#Cria as paredes fixas
pos = funcoes.block_location(variable.MAP, variable.DIVISIONS, variable.RESOLUTION)
for each in pos:
    wall = Fixed_wall(assets, each)
    all_sprites.add(wall)
    fixed_wall_sprites.add(wall)
    all_walls.add(wall)

# Cria as paredes removíveis
pos_tijolo = funcoes.tijolo_location(variable.MAP, variable.DIVISIONS, variable.RESOLUTION)
for each in pos_tijolo:
    wall = Removable_wall(assets, each)
    all_sprites.add(wall)
    removable_wall_sprites.add(wall)
    all_walls.add(wall)

game = True
clock = pygame.time.Clock()
FPS = 7

#Inicializa loop principal
while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        #Recebe e retorna ações do p
        if event.type == pygame.KEYDOWN:
            #eventos player 1
            if event.key == pygame.K_l:
                p1.drop_bomb(assets, all_sprites, all_jacas)
            if event.key == pygame.K_LEFT:
                p1.state = variable.LEFT
                p1.speedx -= variable.WIDTH_SQUARE
            if event.key == pygame.K_RIGHT:
                p1.state = variable.RIGHT
                p1.speedx += variable.WIDTH_SQUARE
            if event.key == pygame.K_UP:
                p1.state = variable.UP
                p1.speedy -= variable.WIDTH_SQUARE
            if event.key == pygame.K_DOWN:
                p1.state = variable.DOWN
                p1.speedy += variable.WIDTH_SQUARE

            #event player 2
            if event.key == pygame.K_e:
                p2.drop_bomb(assets, all_sprites, all_jacas)
            if event.key == pygame.K_a:
                p2.state = variable.LEFT
                p2.speedx -= variable.WIDTH_SQUARE
            if event.key == pygame.K_d:
                p2.state = variable.RIGHT
                p2.speedx += variable.WIDTH_SQUARE
            if event.key == pygame.K_w:
                p2.state = variable.UP
                p2.speedy -= variable.WIDTH_SQUARE
            if event.key == pygame.K_s:
                p2.state = variable.DOWN
                p2.speedy += variable.WIDTH_SQUARE
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p1.state = variable.STILL
                p1.speedx += variable.WIDTH_SQUARE

            if event.key == pygame.K_RIGHT:
                p1.state = variable.STILL
                p1.speedx -= variable.WIDTH_SQUARE

            if event.key == pygame.K_UP:
                p1.state = variable.STILL
                p1.speedy += variable.WIDTH_SQUARE

            if event.key == pygame.K_DOWN:
                p1.state = variable.STILL
                p1.speedy -= variable.WIDTH_SQUARE
                
            #event player 2    
            if event.key == pygame.K_a:
                p2.state = variable.STILL
                p2.speedx += variable.WIDTH_SQUARE

            if event.key == pygame.K_d:
                p2.state = variable.STILL
                p2.speedx -= variable.WIDTH_SQUARE

            if event.key == pygame.K_w:
                p2.state = variable.STILL
                p2.speedy += variable.WIDTH_SQUARE

            if event.key == pygame.K_s:
                p2.state = variable.STILL
                p2.speedy -= variable.WIDTH_SQUARE
    
    
    all_sprites.update()
    all_jacas.update()

    for wall in removable_wall_sprites:
        for jaca in pygame.sprite.spritecollide(wall, all_jacas, False , pygame.sprite.collide_mask):
            if jaca.image != jaca.jaca_types["aberta"] and jaca.image != jaca.jaca_types["fechada"]:
                wall.kill()
#detecta colisoes
    for player in all_players:
        for jaca in pygame.sprite.spritecollide(player, all_jacas, False , pygame.sprite.collide_mask):
            if jaca.image != jaca.jaca_types["aberta"] and jaca.image != jaca.jaca_types["fechada"]:
                player.kill()
            else:
                if funcoes.cant_pass(player, jaca):
                    player.rect.y -= player.speedy 
                    player.rect.x -= player.speedx
                
    #impede que o p entre na parede
    for player in all_players:
        for wall in all_walls:
            if funcoes.cant_pass(player, wall):
                player.rect.y -= player.speedy 
                player.rect.x -= player.speedx

    window.fill((155, 220, 72))
    all_jacas.draw(window)
    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()
