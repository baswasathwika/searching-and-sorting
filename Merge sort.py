def Merge_sort(list):
    if len(list)>1:
        left=list[ : len(list)//2]
        right=list[len(list)//2 : ]
        Merge_sort(left)
        Merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                list[k]=left[i]
                i+=1
            else:
                list[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            list[k]=left[i]
            k+=1
            i+=1
        while j<len(right):
            list[k]=right[j]
            k+=1
            j+=1
list=[5,1,8,13,3,57,0,-1,356,54]
Merge_sort(list)
print(list)
