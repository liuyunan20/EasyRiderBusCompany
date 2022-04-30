import re 

pets = input()
print(re.findall(r'dog|cat|parrot|hamster', pets, flags=re.I))
