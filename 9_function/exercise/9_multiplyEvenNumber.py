def multiply_even_number(lst):
    total = 1
    for num in lst:
        if num%2==0:
            total = total*num
    return total
