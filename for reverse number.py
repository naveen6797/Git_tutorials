number=int(input("enter number"))
result=0
for x in range(0,len(number)+1):
    a=x%10
    result=(result*10)+a    
    number=number//10
print(result)
