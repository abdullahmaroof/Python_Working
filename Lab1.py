x = 1
y = "abdullah"

#list
list1 = [122,32,43,54,"assab"]
print(list1)
#function
#length function len()
print(len(list1))
#APPEND function
list1.append("abdullah")
print('\n',list1)
#insert function
list1.insert(2,"6C")
print(list1)
#pop function
list1.pop(1)
print(list1)
#sort function
list2 = [12,3,5,65,23,543,21]
list2.sort(reverse=True)
print(list2)

list3 = list2.copy()
print(list3)

list2.extend(list1)
print(list2)



