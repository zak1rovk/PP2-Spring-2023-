import re
str = re.compile(r'[a-z]+_[a-z]+')
text = input()
matches = str.findall(text)
print(matches)