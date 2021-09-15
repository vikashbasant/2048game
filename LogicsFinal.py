import random

# Start Game
def start_game():
    mat= []
    for i in range(4):
        # 0 represent the empty matrix
        mat.append([0]*4) 
    return mat


# Adding new 2 in the matrix
def add_new_2(mat):
    # We need to append 2 where matrix is empty..at random position

    row = random.randint(0,3)
    col = random.randint(0,3)
    while(mat[row][col] != 0):
        row = random.randint(0,3)
        col = random.randint(0,3)
    mat[row][col] = 2


    
# Implementing Reverse Matrix
def reverse(mat):
    new_mat = []
    for i in range(4): # For Row
        new_mat.append([])
        for j in range(4): # For Col
            new_mat[i].append(mat[i][4-j-1])
            
    return new_mat
            
                
# Implementing Transpose Matrix
def transpose(mat):
    new_mat = []
    for i in range(4): # For Row
        new_mat.append([])
        for j in range(4): # For Col
            new_mat[i].append(mat[j][i])
    
    return new_mat
    
    
    
    
# Implementing Merge Function
def merge(mat):
    # So in merge we need to return weather their is any changed in Matrix after merging or not.
    # So that we need to mentain changed bydefault to be False
    changed = False
    for i in range(4): # For Each Row
        for j in range(3): # For Each Column & except last col
            if mat[i][j] == mat[i][j+1] and mat[i][j] !=0:
                mat[i][j] = mat[i][j]*2
                # Now mat[i][j+1] becomes 0
                mat[i][j+1] = 0
                changed = True
    return mat,changed
    
    
    
# Implementing Comress function    
def compress(mat):
    changed = False
    # First of all we are make a new Matrix Now. And Each Row we will add New Number and initiallly each row will have 0.
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)

    for i in range(4):
        
        pos = 0 # At each row pos initailly will be 0
        for j in range(4):
            
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                # If any of the row, the position of the perivous element is not same the position of the at new position. 
                if j != pos:
                    changed = True
                pos+=1
    
    return new_mat,changed

# Grid means 2D Matrix...

# Implementing Move-up
def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid,changed1 = compress(transposed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid,changed


# Impementing Move-Down
def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid,changed

# Impelementing Move-Right
def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid,changed

# Impelemenring Move-Left
def move_left(grid):
    # Moving all Number towards left and Movinf all 0 Number towrds right.
    # Changed1 or Changed2 are boolean that tells us changed is happen in the Matrix or not.
    new_grid,changed1 = compress(grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    return new_grid,changed


# Current State Of game
def get_current_state(mat):
    
    # Anywhere 2048 is present
    for i in range(4): # Row
        for j in range(4): # Col
            
            # Case1: Game Won, When Any Of the index 2048 is present in thee Matrix that means Won.
            if (mat[i][j] == 2048):
                return "WON"
            
            
    # Anywhere 0 is present
    for i in range(4):
        for j in range(4):
            # Case2: Gaame Not Over, When Any of index 0 is present in the matrix that means Game Is Not Till Over...
            if (mat[i][j] == 0):
                return "GAME NOT OVER"

    # Other Considition For which Game Will Not Over.
    # Here we can check for 2nd last row and col of matrix
    # Every Row and col except last row and last col.
    if i in range(3):
        for j in range(3):
            # If any where in the matrix Consicutive Number Are Same.
            if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return "GAME NOT OVER"


    # Here we need check for last row and last col 
    # Our i(row) is fixed but j(col) will move[change].
    
    # For Last row
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return "GAME NOT OVER"
    
    # Our j(col) is fixed but i(row) will move[change].
    # For Last Col
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return "GAME NOT OVER"
            
    # Case3: Game is Over, When We can't make any Movement means(that whole array/matrix should be filled) in the Matrix.
    # If niether of these 2 case are staisfy, then taht means Game Over.
    return "LOST"
