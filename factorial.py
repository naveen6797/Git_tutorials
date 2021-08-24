def factorial_num(num):
    if num==1:
        return 1
    else:
        return num*factorial_num(num-1)
num = int(input("enter n value"))
result = factorial_num(num)
print(result)
