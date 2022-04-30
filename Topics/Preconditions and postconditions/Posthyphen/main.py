import re

string = input()
pattern = r'(?<=-).*\b'
result = re.search(pattern, string)
if result:
    print(result.group())
