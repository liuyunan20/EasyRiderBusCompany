import re

string = input()
print(*re.findall(r'(?<=<li>).*?(?=</li>)', string), sep='\n')
