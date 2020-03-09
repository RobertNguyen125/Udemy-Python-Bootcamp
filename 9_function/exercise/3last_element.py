def last_element(l):
    if l != []:
        return l.pop()
    return None
print(last_element([1,2,3]))
print(last_element([]))
