def fun(a,n,x):
    for i in range(0,n):
        if a[i] == x:
            return i
    return 0




list_length = int(input("how many numbers"))
a = []
for y in range(list_length):
    temp_num = int(input("enter numbers:"))
    a.append(temp_num)
    print(a)
x=5
n = len(a)
result = fun(a,n,x)
if result == 0:
    print("element is not present at index")
else:
    print(x,"element is present at index", result)

