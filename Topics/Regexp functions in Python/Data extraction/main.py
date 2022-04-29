import re

string = input()
print(re.search(r'<START>.*<END>', string).group().strip('<START>').strip('<END>'))
