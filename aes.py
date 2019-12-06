def form_matrix(bits):
    matrix = [[0 for x in range(4)] for y in range(4)]
    for x in range(4):
        for y in range(4):
            matrix[x][y] = bits[x+8*y:(x+8*y)+2]
    print(matrix)

def shift_matrix(matrix):
    for x in range(4):
        for y in range(4):
            temp = 

# Main function
form_matrix("A329BC0FE755486D2181003EDA479059")



