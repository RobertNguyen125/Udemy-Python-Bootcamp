def single_letter_count(word , letter):
    count = 0
    word =  word.lower()
    letter = letter.lower()
    for let in word:
        if let == letter:
            count += 1
            return count
        return None

print(single_letter_count('Ducnguwyne', 'h'))
