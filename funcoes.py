import numpy as np

#posição dos blocos no map
def block_location(matrix, divisions, resolution):
    positions = []
    lines, columns = np.where(matrix == 1)
    for i in range(len(lines)):
        positions.append((columns[i]*(resolution[0]/divisions[0]), lines[i]*(resolution[0]/divisions[0])))

    return positions
                
def create_map(divisions):
    map_matrix = np.ones((divisions[0], divisions[1]))
    for line in range(1, len(map_matrix)-1):
        if line % 2 != 0:
            map_matrix[line][1:-1] = [0]*(divisions[0]-2)
        else:
            map_matrix[line][1:] = [0,1]*(divisions[0]//2)
            
    return map_matrix
            