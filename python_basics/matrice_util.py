import random as ran

def generate_arr(m,n):
    arr = []
    for i in range(m):
        arr.append(ran.randint(0,n))
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

