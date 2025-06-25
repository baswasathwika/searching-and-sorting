def selection_sort(list):
    for phase in range(len(list)-1):
        min=phase
        for i in range(phase+1,len(list)):
            if list[i]<list[min]:
                min=i
        list[phase],list[min]=list[min],list[phase]
list=[5,1,8,13,3,57,0,-1,356,54]
selection_sort(list)
print(list)
