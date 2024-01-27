

def combinations(digits):
    set1 = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
            6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
    l1 = list(map(int,list(str(digits))))
    n = len(l1)
    if n == 0:
        return []
    elif n == 1:
        return list(set1[l1[0]])
    elif n == 2:
        a = list(set1[l1[0]])
        b = list(set1[l1[1]])
        res = []
        for i in a:
            for j in b:
                res.append(str(i+j))
        return res
    elif n == 3:
        a = list(set1[l1[0]])
        b = list(set1[l1[1]])
        c = list(set1[l1[2]])
        res = []
        for i in a:
            for j in b:
                for k in c:
                    res.append(str(i+j+k))
        return res
    elif n == 4:
        a = list(set1[l1[0]])
        b = list(set1[l1[1]])
        c = list(set1[l1[2]])
        d = list(set1[l1[3]])
        res = []
        for i in a:
            for j in b:
                for k in c:
                    for l in d:
                        res.append(str(i+j+k+l))
        return res

        
    


print(combinations(2345))
