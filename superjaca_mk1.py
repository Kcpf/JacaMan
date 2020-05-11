import pygame 
import random
import variable
import numpy
import funcoes

pygame.init()

window = pygame.display.set_mode((variable.RESOLUTION))

pygame.display.set_caption('Super Jaca Man')
fixed_square = pygame.Surface(variable.SQUARE_DIMENSIONS)
fixed_square.fill(variable.SQUARE_COLOR)
MAP = variable.MAP


game = True

#looooop principal 
while game:
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    
    pos = funcoes.block(MAP,variable.DIVISIONS,variable.RESOLUTION)

    

    window.fill((155, 220, 72)) 

    for each in pos: 
        window.blit(fixed_square,each)

    pygame.display.update()

pygame.quit()
