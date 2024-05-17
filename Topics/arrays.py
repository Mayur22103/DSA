from array import *

#  Arrays
a1 = array('i',[1,45,11])
print(a1)

# print using forEach
for x in a1 : 
    print(x)

# add element at last
a1.append(22)
a1.append(44)
print(a1)

# give 0 or 1 If Element is available or not
print(a1.count(66))

# remove last element
a1.pop()

# return index number of element
print(a1.index(22))
print(a1)

# remove specific element in array
a1.remove(11)
print(a1)

# insert element at specified index
a1.insert(2,44)
print(a1)

# reverse array
a1.reverse()
print(a1)

# convert array to list
a2 = a1.tolist()
print(a2)

# add list elements to array
a3= array('i',[33,55,66])
a3.fromlist(a2)
print(a3)

# diffrence between extend and append
a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)

# add items of b to the a1 list
a1.extend(b) #  [1, 2, 3, 4]
print(a1)

# add b itself to the a1 list
a2.append(b)
print(a2)





