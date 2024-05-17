l1 =  [44,11,14,12]
print(l1)

l2 = [11,12,"ABC",11.13]
print(l2)


# print using forEach
for x in l1 : 
    print(x)

# add element at last
l1.append(22)
l1.append(44)
print(l1)

# give 0 or 1 If Element is available or not
print(l1.count(12))

# remove last element
l1.pop()
print(l1)

# return index number of element
print(l1.index(12))

# remove specific element in list
l1.remove(12)
print(l1)

# insert element at specified index
l1.insert(1,12)
print(l1)

# reverse list
l1.reverse()
print(l1)

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

# sort list
l1.sort()
print(l1)

# remove all elements from list
l1.clear()
print(l1)


