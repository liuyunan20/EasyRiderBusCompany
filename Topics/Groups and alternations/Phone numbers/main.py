import re

string = input()
template = r'\+(\d+)[\s-]?(\d{3})[\s-]?(\d{3}[\s-]?\d{2}[\s-]?\d{2})'
result = re.match(template, string)
if result:
    print(f'''Full number: {string}
Country code: {result.group(1)}
Area code: {result.group(2)}
Number: {result.group(3)}
''')
else:
    print('No match')
