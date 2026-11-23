def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              A_row=len(a)
              A_col=len(a[0])
              B_row=len(b)
              B_col=len(b[0])
              if A_col==B_row:
                res=[[0]*B_col for _ in range(A_row)]
                for i in range(A_row):
                  for j in range(B_col):
                    for k in range(A_col):
                        res[i][j]+=a[i][k]*b[k][j]
                return res
              else:
                return -1