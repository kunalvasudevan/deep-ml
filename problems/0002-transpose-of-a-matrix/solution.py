def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    a_row= len(a)
    a_col= len(a[0])
    b= [[0 for j in range(a_row)] for i in range(a_col)]
    bb=[]
    for i in range(a_row):
        for j in range(a_col):
            b[j][i]=a[i][j]
    
    return b


    pass