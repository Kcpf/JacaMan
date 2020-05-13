import numpy as np
import funcoes


RESOLUTION = (600, 600)
#resolução só pode ser quadrada 
#divisão tem que ser numero inteiro 
DIVISIONS = (15, 15) # Even numbers
WIDTH_SQUARE = RESOLUTION[0] // DIVISIONS[0]
HEIGHT_SQUARE = RESOLUTION[1] // DIVISIONS[1]
SQUARE_DIMENSIONS = (WIDTH_SQUARE, HEIGHT_SQUARE)
SQUARE_COLOR = (140,140,140)

MAP = funcoes.create_map(DIVISIONS)

PLAYER_WIDTH = WIDTH_SQUARE
PLAYER_HEIGHT = HEIGHT_SQUARE


