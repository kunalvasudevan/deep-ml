def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    rows=len(matrix)
    col=len(matrix[0])
    # A_ in: list[list[float]]
    # for i in range(rows):
    #     for j in range(col):
    det= matrix[0][0]*matrix[1][1]- matrix[0][1]*matrix[1][0]
    A_in = [
        [0, 0],
        [0, 0]
    ]

    if det !=0:
        # A_in[]=(1/det)* [[matrix[1][1],-matrix[0][1]],-matrix[1][0],matrix[0][0]]
  
        A_in[0][0]= (1/det)* matrix[1][1]
        A_in[0][1]= -(1/det)* matrix[0][1]
        A_in[1][0]= -(1/det)* matrix[1][0]
        A_in[1][1]= (1/det)* matrix[0][0]
        return A_in
    else:
        return None


    pass