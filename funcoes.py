import numpy as np
import variable
import pygame
import random


#Define a localização dos blocos na matrix
def block_location(matrix, divisions, resolution):
    positions = []
    lines, columns = np.where(matrix == 1)
    for i in range(len(lines)):
        positions.append(
            (columns[i]*(resolution[0]/divisions[0]), lines[i]*(resolution[0]/divisions[0])))

    return positions

#Define a localização dos tijolos na matrix
def tijolo_location(matrix, divisions, resolution):
    positions = []
    lines, columns = np.where(matrix == 2)
    for i in range(len(lines)):
        positions.append(
            (columns[i]*(resolution[0]/divisions[0]), lines[i]*(resolution[0]/divisions[0])))

    return positions


# Cria uma matriz para ser usada como mapa
def create_map(divisions):
    map_matrix = np.ones((divisions[0], divisions[1]))
    for line in range(1, len(map_matrix)-1):
        if line % 2 != 0:
            map_matrix[line][1:-1] = [0]*(divisions[0]-2)
        else:
            map_matrix[line][1:] = [0, 1]*(divisions[0]//2)

    return map_matrix

# Modifica a matriz para adicionar os tijolos
def modify_map(matrix, number_per_line):
    for line in range(1, len(matrix)-1):
        if line == 1 or line == len(matrix) - 2:
            randomlist = random.sample(range(3, len(matrix[0])-3), number_per_line)
        elif line == 2 or line == len(matrix) - 3:
            randomlist = random.sample(range(2, len(matrix[0])-2), number_per_line)
        else:
            randomlist = random.sample(range(1, len(matrix[0])), number_per_line)
        
        for each in randomlist:
            if matrix[line][each] != 1:
                matrix[line][each] = 2 

    return matrix

#impede o movimento atraves de bloco
def cant_pass(player, wall):
    distance = ((player.rect.centerx - wall.rect.centerx)**2 + (player.rect.centery - wall.rect.centery)**2)**0.5
    return distance - variable.HEIGHT_SQUARE < 0

#carrega todos os sprides recebidos
def load_spritesheet(img_sprite, rows, columns):
    # Calcula a largura e altura de cada sprite.
    width = img_sprite.get_width() // columns
    height = img_sprite.get_height() // rows
    
    # Percorre todos os sprites adicionando em uma lista.
    sprites = []
    for r in range(rows):
        for c in range(columns):
            # Calcula posição do sprite atual
            x = c * width
            y = r * height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, width, height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((width, height), pygame.SRCALPHA)
            image = image.convert_alpha()

            
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(img_sprite, (0, 0), dest_rect)

            sprites.append(image)
    return sprites