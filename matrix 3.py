def create_matrix():
    rows = int(input("enter how many rows"))
    columns = int(input("enter how many colums"))
    matrix = []
    for i in range(rows):
        each_row = []
        for j in range(columns):
            row_value=int(input("enter your values"))
            each_row.append(row_value)
        matrix.append(each_row)
    return matrix

A = create_matrix()
B = create_matrix()
print(A, B)
if len(A[0]) == len(B):
    R=[[0, 0], [0, 0]]
    print(R)
    for i in range (len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                R[i][j] += A[i][k] * B[k][j]
                print(i, j, R[i][j])
    print(R)   
else:
    print("not good matrix")
       



