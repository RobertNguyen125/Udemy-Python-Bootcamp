def list_manipulation (list, command, location, value=None):
    if command == 'remove' and location == 'end':
        return list.pop()
    elif command == 'remove' and location == 'beginning':
        return list.pop(0)
    elif command == 'add' and location == 'end':
        list.insert(len(list), value)
        return list
    else:
        list.insert(0, value)
        return list

print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "end", 30))
