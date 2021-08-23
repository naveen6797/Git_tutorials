a=[[1,2,3],[4,5,6]]
b=[[1,3],[2,3],[4,5]]
matrix=[]
for i in range(len(a)):
    m=[]
    for j in range(len(b[0])):
        m.append(0)
        matrix.append(m)
print(matrix)
