a = [28,15,11,12,10]
for i in range(len(a)):
    x = i
    for j in range(i+1, len(a)):
        if a[x]>a[j]:
            x = j
            print(j)
