


def zigZagByMatrix(str1, rows):
    arr = [['' for i in range(len(str1))] for j in range(rows)]

    i = 0
    j = 0
    flag = 0
    for s in str1:
        arr[i][j] = s
        print("============")
        print(s)
        print(i, ' ', j)
        print(flag)
        if flag == 0:
            i += 1
            if i == rows - 1:
                flag = 1
        else:
            i -= 1
            j += 1
            if i == 0 :
                flag = 0
    res = ''
    for i in arr:
        res += ''.join(i)
    return res

def zigZagByArr(str1, rows):
    if len(str1) <= 1:
        return str1
    arr = ['' for i in range(rows)]
    i = 0
    move = 1
    for s in str1:
        arr[i] += s
        i = i + move
        if i == rows - 1:
            move = -1
        elif i == 0:
            move  = 1
    
    return ''.join(arr)

str1 = "PAYPALISHIRING"
rows = 4
# zigZagByMatrix(str1, rows)

print(zigZagByArr(str1, rows))
