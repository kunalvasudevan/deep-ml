def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    a=[]
    rows=len(matrix)
    col=len(matrix[0])
    if mode == "column":
        for c in range(col):
            total=0
            for r in range(rows):
                total+=matrix[r][c]
            a.append(total/rows)
        return a
    else:
        for r in range(rows):
            total=0
            for c in range(col):
                total+=matrix[r][c]
            a.append(total/col)
        return a
    # return means