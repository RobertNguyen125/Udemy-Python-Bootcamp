def multi_letter_count(string):
    return {letter: string[letter].count() for letter in string}
