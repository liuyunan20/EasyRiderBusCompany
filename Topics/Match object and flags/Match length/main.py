import re

template = r'are you ready??.?.?'
string = input()
result = re.match(template, string)
print(len(result.group())) if result else print(0)
