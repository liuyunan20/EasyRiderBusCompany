import re

string = input()
expense = re.findall(r'(?<=\$)\d+', string)
print(f'This week you have spent: {sum([int(x) for x in expense])} dollars')
