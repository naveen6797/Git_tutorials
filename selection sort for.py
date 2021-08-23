a = [16,22,5,17,2,10,1]
for i in range(len(a)):
    x = i
    for j in range(i+1, len(a)):
        print(j)
        if a[x] > a[j]:
           x=j
           

    a[i],a[x] = a[x],a[i]
    print(a)
