def my_function(num):
    if num % 2 == 0:
        print("even", num)
    elif num % 2 == 1:
        print("odd", num)
    else:
        print("other", num)


num1 = float(input("enetr number"))
num2 = int(input("enetr number"))
my_function(num1)
my_function(num2)
