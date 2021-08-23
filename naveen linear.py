a = [7,5,9,4,12,1]
n = 12
y = len(a)
for i in range(0,y):
    if a[i] == n:
        print(n, "is present at index", i)
        break
    else:
        print("number is not present at index")
        
