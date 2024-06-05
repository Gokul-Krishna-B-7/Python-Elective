input_string = input("Enter a string: ")

vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

num_vowels = sum(1 for char in input_string if char in vowels)
num_consonants = sum(1 for char in input_string if char in consonants)
num_blanks = input_string.count(' ')

print("Total number of vowels:", num_vowels)
print("Total number of consonants:", num_consonants)
print("Total number of blanks:", num_blanks)
