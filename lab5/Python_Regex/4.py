import re
str = re.compile(r'[A-Z][a-z]+')
text = input()
matches = str.findall(text)
print(matches)