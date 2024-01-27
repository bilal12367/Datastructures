
# Print Pascal's Triangle
#        1
#       1  1
#      1  2  1
#     1  3  3  1
#    1  4  6  4  1
#   1  5  10 10  5  1

def pascalTriangle(numRows):
    res = []
    if numRows == 0:
        return res
    res.append([1])
    for i in range(1,numRows):
        list = []
        list.append(1)
        for j in range(1,len(res[i-1])):
            list.append(res[i-1][j - 1] + res[i-1][j])
        list.append(1)
        res.append(list)
    return res

print(pascalTriangle(8))