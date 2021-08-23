def binary_search(lists,find,end,start):
    if end >= start:
        mid = (start+end)//2
        if find == lists[mid]:
            return mid
        elif find < lists[mid]:
            return binary_search(lists,find,mid-1,start)
        else:
            return binary_search(lists,find,end,mid+1)
    return -1
lists =[1,4,5,6,7,8,10]
find=5.8
end=len(lists)-1

result = binary_search(lists,find,end,0)
if result != -1:
    print(find,"found at index",result)
else:
    print(find,"index not found")


