import re
str = input()
s1 = re.compile(r'a.+b$')
print(s1.match(str))    
