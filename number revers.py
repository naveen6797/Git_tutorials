number=123
result=0
while number>0:
    a=number%10
    result=(result*10)+a    
    number=number//10
print(result)

