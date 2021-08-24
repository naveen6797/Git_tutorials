check_numbers = int(input('enter number:'))
for i in range(2 , check_numbers):
    if check_numbers % i == 0:
        print("it is not a prime number")
        break
else:
    print("it is a prime number")

