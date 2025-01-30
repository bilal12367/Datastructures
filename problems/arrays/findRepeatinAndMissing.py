arr = [3, 1, 2, 5, 3]
freqArr = []
duplicate = -1
missing = -1
for idx, i in enumerate(arr):
    if i + 1 not in arr:
        missing = i + 1
    
    if i in freqArr:
        duplicate = i
    freqArr.append(i)

print("Duplicate: ", duplicate)
print("Missing: ",missing)
