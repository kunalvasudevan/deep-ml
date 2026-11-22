def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    rows=len(matrix)
    col=len(matrix[0])
    for i in range(rows):
        for j in range(col):
            matrix[i][j]=matrix[i][j]*scalar
    
    return matrix
    pass