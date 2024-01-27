

def convertToRoman(num: int) -> str:
    set1 = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    l1 = list(map(int, list(str(num))))
    l1.reverse()
    j = 1
    res = ''
    for i in l1:
        if i <= 3:
            res = ''.join([set1[1*j] for _ in range(i)]) + res
        elif i >= 6 and i <= 8:
            res = set1[5*j] + ''.join([set1[1*j] for _ in range(i-5)]) + res
        else:
            res = set1[i*j] + res

        j = j * 10

    return res


convertToRoman(1289)
