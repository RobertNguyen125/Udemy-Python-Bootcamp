# 1: Create dict from the below lists

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer1 = {list1[i]:list2[i] for i in range(0,len(list1))}
print(answer1)

#2: list to dictionary
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer2 = {person[i][0]:person[i][1] for i in range(len(person))}
print(answer2)
answer2 = dict(person)
print(answer2)
answer2 =  {k:v for k,v in person}
print(answer2)

# 3: Vowel Dict Exercise
vowels = {}.fromkeys('aeiou', 0)
print(vowels)

answer4 = {k:chr(k) for k in range(65,91)}
print(answer4)
