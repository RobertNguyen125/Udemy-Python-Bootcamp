# a special operator
# gather remaining arguments  as a Tuple
# just a parameter - can call it whenever you want

def sum_all_nums(num1, *args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(1,2,3,4))
print(sum_all_nums(3,4,5))

def ensure_correct_info(*args):
    if 'Colt' in args and "Steele" in args:
        return 'Welcome Colt'
    return 'Not sure who you are ...'

print(ensure_correct_info())
print(ensure_correct_info(1, True, 'Colt', 'Steele'))
