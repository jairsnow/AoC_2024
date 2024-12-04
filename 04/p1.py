# S  S  S   # S[-3,3]  S[0,3]  S[3,3]
#  A A A    #  A[2,-2] A[0,2] A[2,2] 
#   MMM     #   M[-1,1]M[0,1]M[1,1]  
# SAMXMAS   # S[-3,0]A[-2,0]M[-1,0]X[0,0]M[1,0]A[2,0]S[3,0]
#   MMM     #   M[-1,-1]M[0,-1]M[1,-1]  
#  A A A    #  A[-2,-2] A[0,-2] A[2,-2] 
# S  S  S   # S[-3,-3]  S[0,-3]  S[3,-3]

amount = 0
char_array = {}

def check_nerby(x,y):

    XMAS_found = 0
    # Simple ones
    if x+3 in char_array and char_array[x+1][y] == "M" and char_array[x+2][y] == "A" and char_array[x+3][y] == "S":
        XMAS_found += 1
    if x-3 in char_array and char_array[x-1][y] == "M" and char_array[x-2][y] == "A" and char_array[x-3][y] == "S":
        XMAS_found += 1
    if y+3 in char_array[x] and char_array[x][y+1] == "M" and char_array[x][y+2] == "A" and char_array[x][y+3] == "S":
        XMAS_found += 1
    if y-3 in char_array[x] and char_array[x][y-1] == "M" and char_array[x][y-2] == "A" and char_array[x][y-3] == "S":
        XMAS_found += 1
    
    # Diagonal
    if x+3 in char_array and y+3 in char_array[x+3] and char_array[x+1][y+1] == "M" and char_array[x+2][y+2] == "A" and char_array[x+3][y+3] == "S":
        XMAS_found += 1
    if x-3 in char_array and y+3 in char_array[x-3] and char_array[x-1][y+1] == "M" and char_array[x-2][y+2] == "A" and char_array[x-3][y+3] == "S":
        XMAS_found += 1
    if x+3 in char_array and y-3 in char_array[x+3] and char_array[x+1][y-1] == "M" and char_array[x+2][y-2] == "A" and char_array[x+3][y-3] == "S":
        XMAS_found += 1
    if x-3 in char_array and y-3 in char_array[x-3] and char_array[x-1][y-1] == "M" and char_array[x-2][y-2] == "A" and char_array[x-3][y-3] == "S":
        XMAS_found += 1
    
    char_array[x][y] = str(XMAS_found)
    return XMAS_found


with open('raw_input.txt', 'r') as file:
    for i, row in enumerate(file):
        row = row.strip()

        char_array[i]  = {}

        for j, char in enumerate(row):
            char_array[i][j] = char


for i, row in char_array.items():
    for j, char in row.items():

        if char == "X":
            amount += check_nerby(i,j)

print(amount)
