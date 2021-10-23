def transpose(mat):
    result = [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
    return result

x = [[10,8],[2,4], [1,7]]
print(transpose(x))

