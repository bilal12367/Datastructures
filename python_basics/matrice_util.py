import random as ran

def generate_arr(m):
    arr = []
    for i in range(m):
        arr.append(ran.randint(1,1000))
    return arr


def generate_matrix(m,n):
    matrix = []
    for i in range(m):
        matrix.append(generate_arr(n))
    return matrix

def display_matrix(matrix):
    for i in matrix:
        print('[',end=" ")
        for j in i:
            print(j, end=" ,")
        print(']')

