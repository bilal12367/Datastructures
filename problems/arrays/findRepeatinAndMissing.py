arr = [3, 1, 2, 5, 3]
freqArr = []
duplicate = -1
missing = -1
for i, idx in enumerate(arr):
    if (idx+1) not in arr:
        missing = idx+1

    if i in freqArr:
        duplicate = i
    else:
        freqArr.append(i)

print("Duplicate: ", duplicate)
print("Missing: ",missing)
