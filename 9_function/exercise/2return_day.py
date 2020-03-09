def return_day(num):
    day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if num > 0 and num <= len(day):
        return day[num-1]
    return None

print(return_day(1))
print(return_day(23))
