def snake_to_camel_case(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

snake_case_str = input()
camel_case_str = snake_to_camel_case(snake_case_str)
print(camel_case_str)