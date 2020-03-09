# index(): show the index of item in a list
numbers  = [5,6,7,8,9,10]
print(numbers.index(6)) # 1

numbers = [5,5,6,7,5,8,8,9,10]
print(numbers.index(5)) #0
print(numbers.index(5,2)) #4 because it is after index 2
print(numbers.index(8,6,8)) #6

# count(): count how many times an item occur in a list
# reverse(): reverse the order of the list
# sort(): sort items in a list
# join(): actually a string method

instructors = ['Colt', 'Blue', 'Lisa']
instructors.remove(instructors[-1])
print(instructors)
instructors.remove(instructors[0])
print(instructors)
instructors.insert(0, 'Done')
print(instructors)
