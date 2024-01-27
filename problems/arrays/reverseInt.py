

def reverseInt(x: int) -> int:
    flag = 0
    if x < 0:
        flag = 1
        x = x * -1
    l1 = list(str(x))
    l1.reverse()
    return int(''.join(l1)) * (-1 if flag == 1 else 1)


# print(reverseInt(123))

print(reverseInt(-458))