import pygame
import random
from variable import *
import numpy
import funcoes
import assets
from classes import *
from os import path
import math

pygame.init()

# Define configurações de tela
window = pygame.display.set_mode((RESOLUTION))
pygame.display.set_caption('Super Jaca Man')

# Carrega todos os assets
assets = assets.load_assets()
char_pos = [[RESOLUTION[0]/DIVISIONS[0], RESOLUTION[1] - 40],
            [RESOLUTION[0] - 40, 80]]

# Inicializa classes
p1 = Character(assets["player1_img"], char_pos[0][0], char_pos[0][1])
p2 = Character(assets["player2_img"], char_pos[1][0], char_pos[1][1])
    
# Grupos de sprit
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


# Cria as paredes
all_sprites, fixed_wall_sprites, all_walls, removable_wall_sprites = funcoes.build_walls(
    assets,
    all_sprites,
    fixed_wall_sprites,
    all_walls,
    removable_wall_sprites
)

game = True
clock = pygame.time.Clock()
FPS = 7
pygame.mixer.music.play(loops=-1)

# Inicializa loop principal
# if SCREEN == 0:
while SCREEN == 0:
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            pygame.quit()  
        if event.type == pygame.KEYUP:
            SCREEN = 1
        
    inicial = pygame.image.load(path.join('img/PeNaJaca.png')).convert()
    inicial_rect = inicial.get_rect()

    window.blit(assets['pejacks'], (0,0))
    pygame.display.update()
            
    

while SCREEN == 1:
    clock.tick(FPS) 

    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            pygame.quit() 

        # Recebe e retorna ações do p1
        if event.type == pygame.KEYDOWN:
            # eventos player 1
            if event.key == pygame.K_l:
                p1.drop_bomb(assets, all_sprites, all_jacas)
                
            if event.key == pygame.K_LEFT:
                p1.state = LEFT
                p1.speedx -= WIDTH_SQUARE
                
            if event.key == pygame.K_RIGHT:
                p1.state = RIGHT
                p1.speedx += WIDTH_SQUARE
                
            if event.key == pygame.K_UP:
                p1.state = UP
                p1.speedy -= WIDTH_SQUARE
                
            if event.key == pygame.K_DOWN:
                p1.state = DOWN
                p1.speedy += WIDTH_SQUARE
                

            # event player 2
            if event.key == pygame.K_e:
                p2.drop_bomb(assets, all_sprites, all_jacas)
            if event.key == pygame.K_a:
                p2.state = LEFT
                p2.speedx -= WIDTH_SQUARE
                
            if event.key == pygame.K_d:
                p2.state = RIGHT
                p2.speedx += WIDTH_SQUARE
                
            if event.key == pygame.K_w:
                p2.state = UP
                p2.speedy -= WIDTH_SQUARE
                
            if event.key == pygame.K_s:
                p2.state = DOWN
                p2.speedy += WIDTH_SQUARE
                    

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p1.state = STILL
                p1.speedx += WIDTH_SQUARE

            if event.key == pygame.K_RIGHT:
                p1.state = STILL
                p1.speedx -= WIDTH_SQUARE

            if event.key == pygame.K_UP:
                p1.state = STILL
                p1.speedy += WIDTH_SQUARE

            if event.key == pygame.K_DOWN:
                p1.state = STILL
                p1.speedy -= WIDTH_SQUARE

            # event player 2
            if event.key == pygame.K_a:
                p2.state = STILL
                p2.speedx += WIDTH_SQUARE
                
            if event.key == pygame.K_d:
                p2.state = STILL
                p2.speedx -= WIDTH_SQUARE
                
            if event.key == pygame.K_w:
                p2.state = STILL
                p2.speedy += WIDTH_SQUARE
                    
            if event.key == pygame.K_s:
                p2.state = STILL
                p2.speedy -= WIDTH_SQUARE
                

    all_sprites.update()
    all_jacas.update()

    for player in all_players:
        for wall in all_walls:
            if funcoes.cant_pass(player, wall):
                player.rect.y -= player.speedy
                player.rect.x -= player.speedx
                break
    # detecta colisoes
    for player in all_players:
        
        for jaca in pygame.sprite.spritecollide(player, all_jacas, False, pygame.sprite.collide_mask):
            if jaca.image != jaca.jaca_types["aberta1"] and jaca.image != jaca.jaca_types["fechada"] and jaca.image != jaca.jaca_types["aberta2"] and jaca.image != jaca.jaca_types["aberta3"]:
                if player == p1:
                    SCREEN = 2
                if player == p2:
                    SCREEN = 3
                
                player.kill()
                break
            else:
                # mover o cant_passs para dentro da classe player
                if funcoes.cant_pass(player, jaca):
                    player.rect.y -= player.speedy
                    player.rect.x -= player.speedx

    # impede que o p entre na parede
    for wall in removable_wall_sprites:
        for jaca in pygame.sprite.spritecollide(wall, all_jacas, False, pygame.sprite.collide_mask):
            if jaca.image != jaca.jaca_types["aberta1"] and jaca.image != jaca.jaca_types["fechada"] and jaca.image != jaca.jaca_types["aberta2"] and jaca.image != jaca.jaca_types["aberta3"]:
                wall.kill()
                
    window.fill((155, 220, 72))
    all_jacas.draw(window)
    all_sprites.draw(window)

    pygame.display.update() 

if SCREEN == 2:
    while True:
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                pygame.quit()
        window.blit(assets['pe_na_jaca2'], (0,0))  
        pygame.display.update()
        
if SCREEN == 3:
    while True:
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                pygame.quit()
        window.blit(assets['pe_na_jaca1'], (0,0))
        pygame.display.update()
       
pygame.quit()
