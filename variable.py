import numpy as np
import funcoes


RESOLUTION = (600, 600)
#resolução só pode ser quadrada 
#divisão tem que ser numero inteiro 
DIVISIONS = (15, 15) # Even numbers
WIDTH_SQUARE = (RESOLUTION[0] // DIVISIONS[0])
HEIGHT_SQUARE = (RESOLUTION[1] // DIVISIONS[1])
SQUARE_DIMENSIONS = (WIDTH_SQUARE, HEIGHT_SQUARE)
EXPLO_DIMENSIONS = (WIDTH_SQUARE*3, HEIGHT_SQUARE*3)
SQUARE_COLOR = (140,140,140)

MAP = funcoes.create_map(DIVISIONS)
MAP = funcoes.modify_map(MAP, 3)
PLAYER_WIDTH = WIDTH_SQUARE
PLAYER_HEIGHT = HEIGHT_SQUARE

# Define estados possíveis do jogador
STILL = 0
RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4



