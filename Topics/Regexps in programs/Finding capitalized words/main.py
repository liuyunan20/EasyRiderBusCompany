import re

string = input()
cap_words = re.findall(r'[A-Z][A-Za-z]+', string)
numbers = re.findall(r'\d+', string)
print(f'Capitalized words: {", ".join(cap_words)}')
print(f'Digits: {", ".join(numbers)}')
