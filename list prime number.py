number=[15,67,89,90,61,7]
start=0
while (len(number)>start):
 is_divisible=0
 i=2
 while (number[start]>i):
    if(number[start]%i==0):
        is_divisible=1
    i=i+1
 if(is_divisible==0):
    print(number[start])
 start= start+1
    
