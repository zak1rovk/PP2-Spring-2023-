import re
def camel_to_snake_case(camel_str):
    snake_str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake_str).lower()
camel_case_str = input()
snake_case_str = camel_to_snake_case(camel_case_str)
print(snake_case_str)
