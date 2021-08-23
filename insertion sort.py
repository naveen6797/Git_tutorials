"""program written by naveen mateti"""
x = [85,12,59,45,72,51]
for i in range(1, len(x)):
    print(i)
    key = x[i]
    j = i-1
    while j >= 0 and x[j] > key:
        x[j+1] = x[j]
        j = j-1

    x[j+1] = key
    print("sorted array:",format(x))
