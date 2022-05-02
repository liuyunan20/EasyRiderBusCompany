import re

password = input()
result = re.match(r'^\S[\w\d]{5,14}\S$', password, flags=re.A)
if result:
    print('Thank you!')
else:
    print('Error!')
