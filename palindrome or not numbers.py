number=4545489
b=number
result=0
while b>0:
    
    a=b%10       
    b=b//10
    result=(result*10)+a 
print(result)
if number == result:
      print('its a palindrome')
else:
      print('not a palindrome')



