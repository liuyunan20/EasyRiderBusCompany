import re

string = input()
template = r'Good .{7,9}'
result = re.match(template, string)
if not result:
    print('No greeting!')
elif result.group() == 'Good afternoon':
    print('Good afternoon')
else:
    print(result.group()[0: 12])
