def my_function(number):
    for x in range(2,number):
        if (number%x==0):
            print('not a prime number')
            break
    else:
        print('its prime number')


number=int(input('enter number:'))

