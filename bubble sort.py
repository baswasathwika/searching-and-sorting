def bubble_sort(list):
    for phase in range(1,len(list)):
        for i in range(len(list)-phase):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
    print(list)
list=[5,1,8,13,3,57,0,-1,356,54]
bubble_sort(list)
