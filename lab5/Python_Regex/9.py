import re
def insert_spaces(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)
string = input()
result = insert_spaces(string)
print(result)
