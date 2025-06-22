def linear_search(list,search):
    for i in range(len(list)):
        if list[i]==key:
            return f"{key} key found in the index"
    return "no data found"
list=[5,8,14,3,12]
key=14
print(linear_search(list,key))
