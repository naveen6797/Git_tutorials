def my_function(x):
    if x%2 == 0:
        print("even", x)
    elif x%2==1:
        print("odd", x)
    else:
        print("other", x)


num1 = float(input("enetr number"))
num2 = int(input("enetr number"))
my_function(num1)
my_function(num2)
