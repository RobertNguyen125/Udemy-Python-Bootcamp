# append(): add an element to the end of the list
first_list = [1,2,3,4]
first_list.append(5)
print(first_list)

# extend(): add all elements (in form of list) to the end of list
first_list.extend([5,6,7,8])
print(first_list)

# insert(index, element): add an element before the index
first_list.insert(3, 3)
print(first_list)

# insert() an element to the end of list
first_list.insert(len(first_list), 9)
print(first_list)


# clear(): get rid of everything in a list
# pop(): remove the item at given index and return it
print(first_list.pop())
print(first_list)

# remove(): remove the item 'x' from a list
