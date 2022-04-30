import re

string = input()
result = re.match(r'b.*l$', string, flags=re.I|re.S)
if result:
    print(result.group())
else:
    print("No match")
