import numpy as np
#posição dos blocos no map
def block(matrix, divisions, resolution):
    positions = []
    lines, columns = np.where(matrix == 1)
    for i in range(len(lines)):
        positions.append((columns[i]*(resolution[0]/divisions[0]), lines[i]*(resolution[0]/divisions[0])))

    return positions
                

            