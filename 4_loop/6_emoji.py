for num in range(1,11):
    print('\U0001f600'*num)

times = 1
while times < 11:
    print('\U0001f600'*times)
    times +=1

# this is to do the same printing without the '*'
for num in range(1,11):
    count = 1
    smiley =''
    while count < num:
        smiley +='\U0001f600'
        count += 1
    print(smiley)

times = 1
while times < 20:
    print(' \U0001f600'*times)
    times +=2
