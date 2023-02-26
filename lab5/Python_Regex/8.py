import re
def split_at_uppercase(string):
    return re.findall('[A-Z][^A-Z]*', string)
string = input()
result = split_at_uppercase(string)
print(result)
