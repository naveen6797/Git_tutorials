number= 500
result=0
while (number>=2):
   is_divisible=0
   i=2
   while(number>i):
        if(number%i==0):
          is_divisible=1
        i=i+1
   if(is_divisible==0):
       
       print(number)
   number = number -1
   
