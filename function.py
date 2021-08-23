def my_function(x):
    if x%2 == 0:
        print("even", x)
    elif x%2==1:
        print("odd", x)
    else:
        print("other", x)


x = float(input("enetr number"))
y = int(input("enetr number"))
my_function(x)
my_function(y)
