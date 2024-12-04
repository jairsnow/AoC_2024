amount = 0
char_array = {}

def check_nerby(x,y):
    
    # I can do a one big IF statement, but I prefer to check the boundaries first
    if x-1 in char_array and y-1 in char_array[x-1] and x+1 in char_array and y+1 in char_array[x+1]:

        # And then check if the is a crossed word
        if sorted([char_array[x-1][y-1], char_array[x+1][y+1]]) == ["M", "S"] and \
            sorted([char_array[x-1][y+1], char_array[x+1][y-1]]) == ["M", "S"]:
            return 1
    return 0


with open('raw_input.txt', 'r') as file:
    for i, row in enumerate(file):
        row = row.strip()

        char_array[i]  = {}

        for j, char in enumerate(row):
            char_array[i][j] = char


for i, row in char_array.items():
    for j, char in row.items():

        if char == "A":
            amount += check_nerby(i,j)

print(amount)
