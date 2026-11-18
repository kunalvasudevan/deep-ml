def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    a_row = len(a)
    a_col = len(a[0]) 
    # b_col = len(b[0])
    b_row = len(b)
    mul=0
    l=[]

    if a_col != b_row:
        return -1
    else:
        for i in range(a_col):
            for j in range(b_row):
              mul+=a[i][j] * b[j]
            l.append(mul)
            mul=0
        return l


    pass