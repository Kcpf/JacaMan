import pygame 
import random
import variable
import numpy
import funcoes
import assets

pygame.init()

window = pygame.display.set_mode((variable.RESOLUTION))

pygame.display.set_caption('Super Jaca Man')
fixed_square = pygame.Surface(variable.SQUARE_DIMENSIONS)
fixed_square.fill(variable.SQUARE_COLOR)
assets = assets.load_assets()

game = True

#looooop principal 
while game:
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    
    pos = funcoes.block_location(variable.MAP,variable.DIVISIONS,variable.RESOLUTION)
    
    window.fill((155, 220, 72)) 

    for each in pos: 
        window.blit(fixed_square,each)

    window.blit(assets["player_img"], (300, 300))
    pygame.display.update()

pygame.quit()
