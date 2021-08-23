num = int(input("enter number:"))
result = " "
for i in range(1,num+1):
    a=i%10
    result=(result*10)+a
    break
else:
    
     print(result)
