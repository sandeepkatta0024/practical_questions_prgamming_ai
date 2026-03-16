def matrix_border_sum(m, n, matrix):
    sum=0
    for i in range(0,m):
        for j in range(0,n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                sum+=matrix[i][j]
                print(f"sum = {sum}")

matrix_border_sum(3,4,[[1,2,3,4],[5,6,7,8],[9,0,1,2]])