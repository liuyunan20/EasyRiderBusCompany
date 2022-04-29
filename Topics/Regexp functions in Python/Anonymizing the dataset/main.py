import re

string = input()
str_with_author = re.sub(r'@\w+\b', '<AUTHOR>', string, count=1)
print(re.sub(r'@\w+\b', '<HANDLE>', str_with_author))
