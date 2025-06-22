def Binary_search(list,key):
    s=0
    e=len(list)-1
    while s<=e:
        mid=(s+e)//2
        if list[mid]==key:return mid
        if list[mid]>key:e=mid-1
        else:s=mid+1
    return-1
list=[1,3,6,8,11,13,15]
key=11
print(Binary_search(list,key))
