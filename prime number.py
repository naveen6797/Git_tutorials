number = int(input('enter number:'))
for i in range(2,number):
    if number% i == 0:
        print("it is not a prime number")
        break
else:
    print("it is a prime number")

