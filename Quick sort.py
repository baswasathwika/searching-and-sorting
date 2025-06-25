def Quick_sort(list,s,e):
    if s<e:
        mid=partition(list,s,e)
        Quick_sort(list,s,mid-1)
        Quick_sort(list,mid+1,e)
def partition(list,s,e):
    pivot=list[e]
    i=s
    j=e-1
    while i<=j:
        while i<len(list) and list[i]<pivot:
            i+=1
        while j>=0 and list[j]>pivot:
            j-=1
        if i<j:
            list[i],list[j]=list[j],list[i]
    list[i],list[e]=list[e],list[i]
    return i
list=[5,1,8,13,3,57,0,-1,356,54]
Quick_sort(list,0,len(list)-1)
print(list)
