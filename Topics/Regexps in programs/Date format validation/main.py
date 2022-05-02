import re

string = input()
result = re.match(r'[0123]\d/[01]\d/\d{2,4}', string)
print('True') if result else print('False')
