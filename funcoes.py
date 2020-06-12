import pygame
import variable
import random
import numpy as np
from classes import *


def block_location(matrix, divisions, resolution):
    """ Creates a list with the blocks spawn locations.

    Keyword arguments:
    matrix -- Map matrix
    divisions -- Blocks per line
    resolution -- Screen resolution
    """
    positions = []
    lines, columns = np.where(matrix == 1)
    for i in range(len(lines)):
        positions.append(
            (columns[i]*(resolution[0]/divisions[0]), lines[i]*(resolution[0]/divisions[0])))

    return positions

def tijolo_location(matrix, divisions, resolution):
    """Define brick locations on matrix

    Keyword arguments:
    matrix -- Map
    divisions -- blocks per line
    resolution -- resolution of screen
    """
    
    positions = []
    lines, columns = np.where(matrix == 2)
    for i in range(len(lines)):
        positions.append(
            (columns[i]*(resolution[0]/divisions[0]), lines[i]*(resolution[0]/divisions[0])))

    return positions


def create_map(divisions):
    """Build Matrix

    Keyword arguments:
    divisions -- (lines, rows) of matrix
    """
    
    map_matrix = np.ones((divisions[0], divisions[1]))
    for line in range(1, len(map_matrix)-1):
        if line % 2 != 0:
            map_matrix[line][1:-1] = [0]*(divisions[0]-2)
        else:
            map_matrix[line][1:] = [0, 1]*(divisions[0]//2)

    return map_matrix


def modify_map(matrix, number_per_line):
    """Modify the matrix to add bricks to it

    Keyword arguments:
    matrix -- Map
    number_per_line -- number of bricks per line
    """
    
    for line in range(1, len(matrix)-1):
        if line == 1 or line == len(matrix) - 2:
            randomlist = random.sample(
                range(3, len(matrix[0])-3), number_per_line)
        elif line == 2 or line == len(matrix) - 3:
            randomlist = random.sample(
                range(2, len(matrix[0])-2), number_per_line)
        else:
            randomlist = random.sample(
                range(1, len(matrix[0])), number_per_line)

        for each in randomlist:
            if matrix[line][each] != 1:
                matrix[line][each] = 2

    return matrix


def cant_pass(player, wall):
    """Check is movement is possible

    Keyword arguments:
    player -- player sprite
    wall -- wall sprite
    """
    distance = ((player.rect.centerx - wall.rect.centerx)**2 +
                (player.rect.centery - wall.rect.centery)**2)**0.5
    return distance - variable.HEIGHT_SQUARE < 0


def load_spritesheet(img_sprite, rows, columns):
    """Load all sprites that have spritesheet

    Keyword arguments:
    img_sprite -- image dictionary
    rows -- Number of sprite rows
    columns -- Number of sprite columns
    """

    width = img_sprite.get_width() // columns
    height = img_sprite.get_height() // rows

    # Iterate all sprites and put then on a list
    sprites = []
    for r in range(rows):
        for c in range(columns):
            # calculates actual sprite position
            x = c * width
            y = r * height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, width, height)

            # Create a blank image on screen
            image = pygame.Surface((width, height), pygame.SRCALPHA)
            image = image.convert_alpha()

            # Copy the actual sprite to the image
            image.blit(img_sprite, (0, 0), dest_rect)

            sprites.append(image)
    return sprites


def build_walls(assets, all_sprites, fixed_wall_sprites, all_walls, removable_wall_sprites):
    """Create walls inside sprite groups

    Keyword arguments:
    assets -- image dictionary
    all_sprites -- All Sprites group
    fixed_wall_sprites -- Fixed wall Sprites group
    all_walls -- Wall Sprites group
    removable_wall_sprites -- Removable wall Sprites group
    """

    # Create fixed walls
    pos = block_location(variable.MAP, variable.DIVISIONS, variable.RESOLUTION)
    for each in pos:
        wall = Fixed_wall(assets, each)
        all_sprites.add(wall)
        fixed_wall_sprites.add(wall)
        all_walls.add(wall)

    # Create removable walls
    pos_tijolo = tijolo_location(
        variable.MAP, variable.DIVISIONS, variable.RESOLUTION)
    for each in pos_tijolo:
        wall = Removable_wall(assets, each)
        all_sprites.add(wall)
        removable_wall_sprites.add(wall)
        all_walls.add(wall)

    return all_sprites, fixed_wall_sprites, all_walls, removable_wall_sprites

def displayTextMainMenu(text, COLOR, screen, position):
        # Renders the text by the font chosen before
        font_50 = pygame.font.SysFont("American Captain", 50)
        text = font_50.render(text, True, COLOR)

        # Sets the text position:
        textPosition = (position)

        # Sticks the text to the screen:
        screen.blit(text, textPosition)

def buttonClick(x, y, width, height):
    # Gets mouse position:
    mousePosition = pygame.mouse.get_pos()

    # Checks if mouse is within button area:
    if mousePosition[0] >= x and mousePosition[0] <= x + width:
        if mousePosition[1] >= y and mousePosition[1] <= y + height:

            return True
