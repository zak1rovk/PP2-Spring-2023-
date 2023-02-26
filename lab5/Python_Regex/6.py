import re
pattern = re.compile(r'[ ,.]')
text = input()
replaced_text = pattern.sub(':', text)
print(replaced_text)