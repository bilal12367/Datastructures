str = "cccdaaaddllnneeemxxsdfhsdfkjhsdfjdkmppl"
strDict = {}
for i in str:
    if i in strDict:
        strDict[i] = strDict[i] + 1
    else:
        strDict[i] = 1
min = len(str)
for i in strDict:
    if strDict[i] < min:
        min = strDict[i]
j = 0
for i in strDict:
    if strDict[i] == min:
        j = i
        break

print(j)