def naveen(n):
    if n==1:
        return 1
    else:
        return n*naveen(n-1)
n = int(input("enter n value"))
result = naveen(n)
print(result)
