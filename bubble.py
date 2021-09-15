def sort(list1):
    for i in range(len(list1)-1, 0,-1):
        for j in range(i):
            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp

list1 = [1,3,5,2,0,8,7]
sort(list1)
print(list1)