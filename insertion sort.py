def insertion_sort(list):
    for i in range(1,len(list)):
        j=i-1
        temp=list[i]
        while j>=0 and list[j]>temp:
            list[j+1]=list[j]
            j-=1
        list[j+1]=temp
list=[5,1,8,13,3,57,0,-1,356,54]
insertion_sort(list)
print(list)
