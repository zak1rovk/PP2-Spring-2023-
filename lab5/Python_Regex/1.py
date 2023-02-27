import re
str = input()
pattern = re.compile(r'a+b*')
print(pattern.match(str))     
