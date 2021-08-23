def my_function(num):
    result = 0
    actual_num=num
    for i in range(num):
        if num>0:
            result1 = num%10
            result = (result*10)+result1
            num = num//10
        else:
            break
    print(result)
    
x = int(input("enter number"))
my_function(x)

