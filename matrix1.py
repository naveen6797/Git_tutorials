a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[10,11,12],[14,15,16],[17,18,19]]
r=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            r[i][j]+=a[i][k]*b[k][j]
            print(r)
            

