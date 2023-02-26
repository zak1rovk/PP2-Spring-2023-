import re
str = input()
str1 = re.compile(r'a+b*')
print(str1.match(str))     