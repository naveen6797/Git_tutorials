def fun():
    
        r=int(input("enter how many rows"))
        c=int(input("enter how many colums"))
        x=[]
        for i in range(r):
            a=[]
            
            for j in range(c):
                e=int(input("enter your values"))
                a.append(e)
            x.append(a)
        return(x)
        
       
Y=fun()
M=fun()
print(Y,M)



  
