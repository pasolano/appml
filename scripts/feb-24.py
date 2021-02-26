import numpy as np

def convolve(matrix, filter, weight=1):
    matrix_copy = np.copy(matrix)
    size_x = matrix.shape[0]
    size_y = matrix.shape[1]
    for x in range(1,size_x-1):
        for y in range(1,size_y-1):
            convolution = 0.0
            convolution += (matrix[x - 1, y-1] * filter[0][0])
            convolution += (matrix[x, y-1] * filter[0][1])
            convolution += (matrix[x + 1, y-1] * filter[0][2])
            convolution += (matrix[x-1, y] * filter[1][0])
            convolution += (matrix[x, y] * filter[1][1])
            convolution += (matrix[x+1, y] * filter[1][2])
            convolution += (matrix[x-1, y+1] * filter[2][0])
            convolution += (matrix[x, y+1] * filter[2][1])
            convolution += (matrix[x+1, y+1] * filter[2][2])
            convolution *= weight
            if(convolution<0):
                convolution=0
            if(convolution>255):
                convolution=255
            matrix_copy[x, y] = convolution

    # remove unfiltered border
    matrix_copy = matrix_copy[1:len(matrix_copy)-1]
    rows = []
    for row in matrix_copy:
        rows.append(row[1:len(row)-1])
    matrix_copy = np.array(rows)

    return matrix_copy

matrix1 = np.array([[1,1,1],[0,1,0],[1,1,0]])
matrix2 = np.array([[0,0,1],[0,1,1],[1,1,1]])
matrix3 = np.array([[0,1,1,2,0,0,1,0,-1],[1,-1,-1,-1,0,-2,-1,1,0],[-1,1,1,2,-1,-1,0,0,0],[-1,0,1,-1,1,0,-1,-1,1],[0,-1,1,2,0,0,1,1,1],[0,-1,-1,0,2,-2,-1,1,1],[-1,1,0,-1,-1,0,-1,-1,-1],[0,-1,-1,2,-1,-1,-1,0,-1],[-1,1,-1,1,-2,2,0,0,1]])

filtered1 = convolve(matrix3, matrix1)
filtered2 = convolve(matrix3, matrix2)

print("First convolution:\n" + str(filtered1) + '\n')
print("Second convolution:\n" + str(filtered2) + '\n')