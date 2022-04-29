import re

user_name = input()
if re.match(r'[a-zA-Z]', user_name):
    print('Thank you!')
else:
    print('Oops! The username has to start with a letter.')
