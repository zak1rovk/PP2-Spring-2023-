import re
str = input()
str1 = re.compile(r'a{1}b{2,3}')
print(str1.match(str))       
